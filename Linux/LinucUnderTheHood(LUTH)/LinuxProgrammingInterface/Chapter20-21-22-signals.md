# Chapter 20, 21, 22 Signals

This is a perfect way to learn. At companies like Google, this is called a **"Case Study"** or **"Production Post-Mortem"** interview.

Let’s look at a classic, high-severity incident involving Signals and Process Control.

---

## 1. The Incident: The "Ghost" Memory Leak & The Zombie Apocalypse

**The Scenario:**
You are the SRE on-call for a massive **Image Processing Service**. The service works by spawning a "Worker" process for every image upload.

* Suddenly, monitoring alerts you that **PID Exhaustion** is occurring on several nodes.
* New processes cannot start (`fork: retry: Resource temporarily unavailable`).
* Looking at `top`, you see thousands of processes marked as `<defunct>`.

---

## 2. Analysis: Why did this happen?

You investigate the "Parent" process (the Image Manager).

* The developer recently updated the code to handle `SIGTERM` for graceful shutdowns.
* However, they **blocked all signals** at the start of the program to "ensure the shutdown logic isn't interrupted."
* **The Root Cause:** By blocking `SIGCHLD`, the Parent process never received the "Push" notification from the Kernel that a child had finished. Because the Parent didn't "reap" the children (by calling `wait()`), the Kernel kept the children in the Process Table as **Zombies** to preserve their exit status.

**Impact:** Even though the children "finished" their work, they are taking up a slot in the Process Table. Eventually, the system hits `pid_max`, and the entire node stops accepting new work.

---

## 3. Troubleshooting Steps & Commands

### Step A: Verify PID Exhaustion

First, confirm that you aren't out of RAM, but out of PIDs.

```bash
# Check current PID count vs Limit
cat /proc/sys/kernel/pid_max
ps -eLf | wc -l

```

### Step B: Identify the "Zombie" State

Look for processes in the `Z` state.

```bash
# Find the top 10 parents with the most zombie children
ps -A -ostat,ppid,pid,cmd | grep -e '^[Zz]' | awk '{print $2}' | sort | uniq -c | sort -nr | head -n 10

```

### Step C: Inspect the Signal Mask

This is the "Senior SRE" move. You want to see if the Parent is actually "listening" to the Kernel.

```bash
# Replace <PPID> with the Parent PID found in Step B
grep '^Sig' /proc/<PPID>/status

```

You will see `SigBlk` (Blocked signals). If you decode that hex and see bit 17 (SIGCHLD) is set, you've found the bug.

### Step D: Emergency Mitigation

You cannot "kill" a zombie. You must **kill the Parent**.

```bash
# Sending SIGKILL to the parent forces the Kernel to re-parent the zombies to PID 1
kill -9 <PARENT_PID>

```

*The Kernel's PID 1 (systemd) will immediately reap them.*

---

## 4. Lab Exercise: Reproduce the Incident

Run this on your CentOS setup to see exactly how a "Blocked Signal" creates an outage.

**Create `zombie_factory.py`:**

```python
import os
import signal
import time

# 1. MISTAKE: We block SIGCHLD (Signal 17)
# This prevents the parent from being 'interrupted' when a child dies.
signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGCHLD})

print(f"Parent PID: {os.getpid()} - Blocking SIGCHLD. Creating 5 zombies...")

for i in range(5):
    pid = os.fork()
    if pid == 0:
        # CHILD: Dies immediately
        os._exit(0)

# 2. PARENT: Sleeps forever, never calling wait()
print("Zombies created. Check 'ps aux | grep Z'. I will sleep for 60s.")
time.sleep(60)

```

**Testing in Lab:**

1. Run `python3 zombie_factory.py &`.
2. Watch the zombies: `watch -n 1 "ps -ef | grep defunct"`.
3. Check the signal mask: `cat /proc/$(pgrep -f zombie_factory)/status | grep SigBlk`.

---

## 5. Prevention (The "Google" Way)

How do we stop this from happening again?

1. **Never block SIGCHLD globally:** Only block signals for the absolute minimum time required for a "Critical Section" of code.
2. **Use `SA_NOCLDWAIT`:** If you don't care about the exit status, tell the Kernel:
```c
struct sigaction sa;
sa.sa_handler = SIG_IGN;
sa.sa_flags = SA_NOCLDWAIT; // This prevents zombies entirely!
sigaction(SIGCHLD, &sa, NULL);

```


3. **Monitoring:** Set alerts for `pid_max` usage at 70% and 90% thresholds.

---

### Follow-up Questions for You:

1. Does the **Zombie** process consume RAM?
2. If you see a process in the **'D' state** (Uninterruptible Sleep), can you kill it with `kill -9`? Why or why not?
3. In the lab above, why did killing the **Parent** fix the problem instead of leaving the zombies there forever?

**Which one would you like to tackle first?**

This is a great place to drill down. Understanding the **'D' state** and **Signal architecture** is fundamental to "Incident Response" at scale.

---

### 1. The 'D' State (Uninterruptible Sleep): Deep Dive

In Linux, most processes sleep in **'S' state (Interruptible)**. They are waiting for something (like a keyboard press or a network packet), but if you send them a signal, they "wake up" to handle it.

The **'D' state** is different. The process is waiting for **Hardware I/O** (Disk, NFS, or a specialized driver) and is currently executing inside the **Kernel**.

#### Why is it "Uninterruptible"?

The Kernel designers decided that if a process is in the middle of a critical hardware operation (like updating a file system's metadata), interrupting it with a signal could leave the hardware or the filesystem in a **corrupted state**. Therefore, the process is shielded from all signals until the I/O returns.

#### Lab Example: How to simulate a 'D' state

The easiest way to see a 'D' state is to use a "broken" network mount (NFS) or a slow disk operation. On your CentOS lab:

```bash
# 1. We use 'vfork' which often puts the parent in a short D-state 
# or use a disk-heavy command:
dd if=/dev/sda of=/dev/null & 

# 2. Check the status:
ps -eo pid,stat,cmd | grep " D "

```

**Production Scenario:** You have a web server where the `/var/www/html` folder is mounted via **NFS**. If the NFS server crashes, every process trying to `ls` or `read` from that folder will immediately enter **'D' state**. They will stay there until the NFS server comes back or the network timeout (usually 15-30 mins) expires.

---

### 2. User Space vs. Kernel Space: The Signal Barrier

| Feature | User Space Process | Kernel Space "Process" (Threads) |
| --- | --- | --- |
| **Visibility** | Seen in `ps` and `top`. | Seen in `ps` (usually in brackets like `[kworker]`). |
| **Signal Handling** | Can define custom handlers (e.g., Python `signal.signal`). | **Cannot** handle signals. They ignore everything. |
| **Transitions** | Moves between User/Kernel space via **System Calls**. | Always stays in Kernel space. |
| **The 'D' State** | A User process *enters* Kernel space via a syscall and gets stuck there (looks like 'D' state). | Kernel threads can enter 'D' state if waiting for hardware. |

**The Interview Answer:** *"A User Space process only processes signals when it is about to leave the Kernel and return to User Space. If it's stuck in 'D' state, it never 'leaves' the Kernel, so the signal is never checked."*

---

### 3. Signal Types and Production Use Cases

At Google/Meta, they expect you to know more than just `kill -9`. Here are the signals used in high-level SRE automation:

| Signal | Name | Production Use Case (The "Why") |
| --- | --- | --- |
| **1** | **SIGHUP** | **Reload Config:** Tell Nginx or Apache to read the new config file without dropping active connections. |
| **2** | **SIGINT** | **Interrupt:** Equivalent to `Ctrl+C`. Used in dev environments to stop a foreground process. |
| **9** | **SIGKILL** | **The Hammer:** Used by the **OOM Killer**. It cannot be caught. Use it only as a last resort (data corruption risk). |
| **10/12** | **SIGUSR1/2** | **App-Specific:** Developers use these for custom triggers (e.g., tell an app to rotate its log files or dump its internal state to a file). |
| **15** | **SIGTERM** | **Graceful Shutdown:** The standard signal sent by Kubernetes or `systemctl stop`. Allows the app to close DB connections. |
| **17** | **SIGCHLD** | **Reaping:** Sent to a parent when a child dies. Critical for preventing **Zombies**. |

---

### 4. SRE Scenario: The "Zombie Container" (PID 1 Problem)

**The Incident:** You run a Java app in a Docker container. You notice that when you run `docker stop`, it takes exactly 10 seconds every time, and the app doesn't shut down gracefully.

**The Analysis:**

1. In Linux, **PID 1** (the init process) is special. It does not have "Default Actions" for signals like SIGTERM.
2. If your Dockerfile is `CMD ["java", "-jar", "app.jar"]`, Java becomes **PID 1**.
3. If Java hasn't explicitly written code to "Catch" SIGTERM, it will **ignore** it because it's PID 1.
4. Docker waits 10 seconds for the app to die, then sends **SIGKILL (9)**.

**The Fix:** Use an init-wrapper like `tini` or `dumb-init` in your container to properly proxy signals to the Java app.

---

### Lab Exercise: Decoding Signal Masks

On your CentOS machine, let's see which signals a process is currently "ignoring" or "catching."

1. **Find a process (e.g., your shell):**
```bash
grep "^Sig" /proc/$$/status

```


2. **You will see hex values:**
* `SigPnd`: Pending (Waiting to be delivered)
* `SigBlk`: Blocked (Held in the "waiting room")
* `SigIgn`: Ignored
* `SigCgt`: Caught (Has a custom handler)


3. **Convert Hex to Human Readable:**
```bash
# Use this trick to see which signals are caught (SigCgt)
kill -l 0x$(grep SigCgt /proc/$$/status | awk '{print $2}')

```



---

### Summary Checklist for Interview

* **D-State:** Unkillable, stuck in Kernel, waiting for I/O.
* **SIGTERM vs SIGKILL:** Always 15 then 9.
* **PID 1:** Does not have default signal handlers; must catch them explicitly.
* **Zombies:** Result of ignored `SIGCHLD`.

**Next Topic: Chapter 13 & 14: File I/O Buffering and File Systems.**
**The SRE Question:** *"What happens to your data if the power goes out? Is it in the Disk cache, the Kernel cache, or the Application buffer?"*

**Ready to move to I/O or do you have more questions on Signals?**

This is one of the most common "aha!" moments in Linux SRE training. To understand why a process gets **PID 1** inside a container, you have to understand how Linux **Namespaces** work.

### 1. The Concept: Nested Realities (Namespaces)

In Linux, a **Namespace** is a feature that wraps a global system resource in an abstraction. To the processes inside the namespace, it looks like they have their own isolated instance of that resource.

When Docker starts a container, it creates a new **PID Namespace**.

* **Outside the container (Host):** Your Java app might have a PID like `45021`.
* **Inside the container:** That same process is assigned **PID 1**.

Think of it like an apartment building. The building address is "123 Main St" (Host), but inside the building, there is an "Apartment 1" (Container). To the person living in Apartment 1, they are at the "first" door, even though they are the 100th person in the whole city.

---

### 2. The Incident Analysis: Why PID 1 is "Immune"

In a standard Linux OS (like your CentOS lab), **PID 1** is `systemd` or `init`. The Kernel treats PID 1 differently than any other process:

1. **No Default Handlers:** For a normal process, if you send `SIGTERM`, the Kernel kills it by default. For **PID 1**, the Kernel **refuses** to kill it unless the process has explicitly written code to handle that signal.
2. **The "Safety" Rule:** This is a safety feature. If the Kernel allowed PID 1 to be killed easily, the entire OS would crash instantly.

**The Docker Problem:**
When you run `CMD ["java", "-jar", "app.jar"]`, the Java Virtual Machine (JVM) becomes PID 1 inside that container's namespace.

* **Docker stop:** Sends `SIGTERM` to PID 1.
* **The JVM:** Since it’s PID 1 and usually doesn't have a specific "Signal Listener" configured for `SIGTERM`, it **ignores** the signal.
* **The Kernel:** Sees that PID 1 ignored the signal and does nothing.
* **The Result:** Docker waits for its default timeout (10 seconds), gets frustrated, and sends `SIGKILL` (which cannot be ignored).

**This is a "Dirty Shutdown"**—your app didn't close database connections or finish writing to logs; it just vanished.

---

### 3. Troubleshooting & Verification (Lab Exercise)

You can see this happening on your CentOS machine using a simple container.

**Step 1: Run a container that does nothing**

```bash
docker run -d --name stubborn-container alpine sleep 1000

```

**Step 2: Check the PID inside the container**

```bash
docker exec stubborn-container ps aux

```

*You will see `sleep 1000` is **PID 1**.*

**Step 3: Try to stop it and time it**

```bash
time docker stop stubborn-container

```

*You will see it takes exactly **10.xxx seconds**.*

---

### 4. The SRE Fix: `tini` or `dumb-init`

To fix this, we use a "tiny" init process. This process is designed to:

1. Be PID 1.
2. Actually **listen** to signals like `SIGTERM`.
3. **Forward (Proxy)** those signals to your Java app.
4. **Reap Zombies** (since PID 1 is also responsible for cleaning up defunct processes).

**The Correct Dockerfile Pattern:**

```dockerfile
# Add tini
RUN apk add --no-cache tini
# Use tini as the entrypoint
ENTRYPOINT ["/sbin/tini", "--"]
# Now Java runs as a child of tini, NOT as PID 1
CMD ["java", "-jar", "app.jar"]

```

---

### 5. Interview Perspective: The Google "Drill-Down"

**Interviewer:** *"If I don't want to use an init-wrapper, is there another way to make sure Java isn't PID 1?"*

**The Expert Answer:**

> "Yes. If you use the **Shell form** of CMD instead of the **Exec form**, the shell becomes PID 1.
> * **Exec form:** `CMD ["java", "-jar", "app.jar"]` -> Java is PID 1.
> * **Shell form:** `CMD java -jar app.jar` -> `/bin/sh -c` is PID 1, and Java is its child.
> 
> 
> **However**, this is actually **worse**. Most shells (like `/bin/sh`) do not forward signals to their children. So when Docker stops the container, the shell gets the `SIGTERM`, ignores it, and you still wait 10 seconds for the `SIGKILL`. This is why using `tini` or `dumb-init` is the industry standard for reliable SRE operations."

---

### Next Step: Phase 3 - File I/O (Chapters 13 & 14)

We've mastered how processes live, die, and handle signals. Now we must look at how they talk to the disk.

**The SRE Scenario:** Your application writes a log file. You run `ls -l` and see the file size is 1GB. You run `rm logs.txt`. The file is gone from the folder, but `df -h` still says the disk is 99% full.

**Would you like to analyze this "Invisible Disk Usage" incident next?** (This is a Tier-1 SRE interview question).