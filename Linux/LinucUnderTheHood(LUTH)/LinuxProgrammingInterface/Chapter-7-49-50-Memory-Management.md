# Chapter 7, 49, 50 Memory Management:

This is an ambitious and excellent goal. To complete the Linux study plan today, we are going to consolidate **Pillar 4: Memory Management** (Chapters 7, 49, and 50) into one powerhouse lesson.

In SRE interviews at Google/Meta, they don't care if you can define "RAM." They care if you can explain why a process with **20GB Virtual Memory** is only using **2GB of Physical RAM**, and why that process just got **OOMKilled**.

### Pillar 4: Memory Management & The OOM Killer

#### 1. The Virtual Memory Abstraction (The "Contract")

Every process in Linux thinks it has a flat, continuous range of memory starting from address zero. This is a "lie" told by the Kernel.

* **VSZ (Virtual Size):** The total amount of memory a process *thinks* it has. This includes shared libraries, memory-mapped files, and memory it allocated but hasn't touched yet.
* **RSS (Resident Set Size):** The "Real" memory. This is the portion of VSZ that is actually loaded into physical RAM chips.

**SRE Scenario:** You see a process with `VSZ=100GB` and `RSS=1GB`. Should you panic?
**Answer:** No. VSZ is just a promise. RSS is the actual debt. You only pay for what you touch.

#### 2. Paging and Demand Paging

The Kernel breaks memory into **Pages** (usually 4KB).

* **Demand Paging:** When a process asks for memory, the Kernel doesn't give it RAM immediately. It just updates the process's page table. Only when the process tries to *read or write* to that address does a **Page Fault** occur. The Kernel then finds a physical page and maps it.
* **Minor Page Fault:** The page is in RAM already (e.g., a shared library). Fast.
* **Major Page Fault:** The Kernel has to go to the disk (swap or file) to get the data. **Slow.** This is what causes "I/O Wait" on a busy server.

#### 3. The Page Cache (Why "Free" RAM is 0)

Linux hates wasted RAM. If you have 64GB of RAM and your apps only use 10GB, Linux uses the other 54GB to cache files you've recently read (the **Page Cache**).

* **SRE Command:** `free -m`.
* **Interpretation:** Look at the `available` column, not the `free` column. `available` = `free` + `cached/buffers`.

#### 4. The OOM Killer (The "Assassin")

When RAM and Swap are 100% full, the Kernel must kill a process to prevent the whole system from crashing.

* **How it chooses:** It calculates an `oom_score` for every process.
* High RAM usage = High score.
* Long-running (Old) processes = Slightly lower score (Kernel respects elders).
* Root processes = Lower score.


* **SRE Tuning:** You can protect a process (like your SSH daemon or Database) by writing to `/proc/PID/oom_score_adj`. A value of `-1000` makes it unkillable.

---

### 💼 Google SRE Interview Scenario: The "Leaking" Sidecar

**Interviewer:** *"You have a Kubernetes pod with a Java App and a Python Sidecar. The pod keeps restarting with `Reason: OOMKilled`. The Java App is the most important, but the Python sidecar is the one using 90% of the memory. How does the Kernel decide which one to kill, and how do you protect the Java App?"*

**Your Answer:**

1. **The Choice:** The OOM Killer will likely target the Python sidecar because its `oom_score` will be higher due to its massive RSS usage relative to its importance.
2. **The Investigation:** I would check `/var/log/syslog` or `dmesg` to find the "OOM Kill" message. It will list the `points` of the killed process.
3. **The Protection:** In a containerized environment, I would set **Memory Limits** in the Spec. In a raw Linux environment, I would adjust the Java App's `oom_score_adj` to `-1000` to ensure the Kernel kills the sidecar (or anything else) before touching the main App.

---

### 🛠️ Pillar 4: SRE Troubleshooting Toolkit (Commands to Save)

---

### 🚀 Completion Checklist

You have now covered:

1. **Process Lifecycle** (Signals, Fork, Exec, Zombies).
2. **Filesystems** (Inodes, Links, VFS, Atomic Ops, Over-mounting).
3. **Memory** (RSS vs VSZ, Page Cache, OOM Killer).

To master **Virtual Memory**, you have to stop thinking of RAM as a physical bucket of bits and start thinking of it as a **Mapping Table**.

### 1. Deep Dive: The Three "Sizes" of Memory

In a Google SRE interview, if you say "The process is using 5GB of RAM," they will ask: "Which 5GB?"

1. **VSZ (Virtual Size):** The total address space the process *requested*. It costs nothing. It’s a "reservation."
2. **RSS (Resident Set Size):** The physical RAM pages actually allocated. This is what shows up in `free -m`.
3. **PSS (Proportional Set Size):** **The "SRE Choice."** If 10 processes share a 100MB library, RSS says each uses 100MB (1GB total). PSS says each uses 10MB (100MB total). **PSS is the true cost of a process.**

---

### 2. Lab Exercise: VSZ vs. RSS (The "Empty Promise")

We will write a small Python script that "allocates" 1GB of memory but doesn't touch it, then we will "touch" it and watch the Kernel scramble to find physical RAM.

#### How to run the lab:

1. Run `python3 mem_demo.py &`
2. **During Step 1:** Run `ps -o pid,vsz,rss,command -p $(pgrep -f mem_demo.py)`
* *Result:* VSZ will be ~1,000,000 (1GB), but RSS will be very small (~10MB).


3. **During Step 3:** Run the same `ps` command.
* *Result:* RSS will now jump to ~1,000,000 (1GB).



---

### 3. Production Scenario: The "Memory Overcommit" Outage

**The Situation:**
You are running a cluster of 10 servers, each with 32GB of RAM. You have configured your Java applications to have a `MaxHeap` of 24GB.

* Total "Promises" (VSZ): 240GB.
* Total "Physical RAM": 320GB.
Everything looks fine.

**The Outage:**
Suddenly, a "Cyber Monday" sale starts. All 10 Java apps start processing heavy traffic. They all start "touching" their 24GB of heap at the same time.
Suddenly, servers start crashing. SSH stops responding. The `dmesg` log shows **OOM Killer** is going wild.

**The SRE Root Cause:**
This is **Overcommit**. The Linux Kernel allows you to allocate more memory than you have, assuming not everyone will use it at once. When everyone "called in their debt" at the same time, the Kernel ran out of physical pages and started the "assassinations."

---

This is perhaps the most frequent topic in Google SRE "Nonalgorithmic" interviews. Understanding the **Page Cache** is the difference between an admin who panics when they see "0MB Free RAM" and an SRE who knows the system is performing perfectly.

### 1. The Theory: What is the Page Cache?

The Kernel treats RAM as a fast buffer for the Disk.

* **The Rule:** Any time you read a file from disk, the Kernel keeps those blocks in RAM.
* **The Benefit:** If you (or any other process) read that same file again, the Kernel serves it from RAM at **nanosecond** speeds instead of **millisecond** disk speeds.
* **The "Available" Metric:** This memory is technically "used," but the Kernel can **instantly evict** it if an application needs RAM for its Heap (RSS). This is why we look at the `available` column in `free -m`.

---

### 2. Lab Exercise: The "Warm" vs. "Cold" Cache

We will use a large file to prove that the Page Cache makes file access 100x-1000x faster.

#### Step 1: Create a large file (The "Cold" state)

```bash
# Create a 500MB file
dd if=/dev/urandom of=testfile bs=1M count=500

```

#### Step 2: Clear the Cache (The "SRE Reset")

To see the "Cold" performance, we must tell the Kernel to throw away its Page Cache.

```bash
# Sync disk and drop caches (Requires root)
sync; echo 3 > /proc/sys/vm/drop_caches

```

#### Step 3: Timed Read (Cold Read)

```bash
time cat testfile > /dev/null
# Output: Should take ~1.0 to 2.0 seconds (depending on disk speed)

```

#### Step 4: Timed Read (Warm Read)

Now that the file is in the Page Cache, read it again.

```bash
time cat testfile > /dev/null
# Output: Should take ~0.05 seconds! (The data never touched the disk)

```

#### Step 5: Observe `free -m`

```bash
free -m
# You will see the 'buff/cache' column has increased by ~500MB.

```

---

### 3. Production Scenario: The "Cold Start" Latency Spike

**The Situation:**
You just deployed a new version of a high-traffic Go service to 1,000 servers. You performed a "Rolling Restart."

**The Outage:**
Immediately after the restart, the **P99 Latency** spikes from 50ms to 500ms. The CPU is not high, and the Network is fine. After 5 minutes, the latency drops back to normal automatically.

**The SRE Root Cause:**
This is a **Cold Cache** issue.

1. The new service relies on reading several large configuration files or static assets from disk.
2. Because the servers were restarted (or the process was new), those files were not in the **Page Cache**.
3. Every initial request triggered a **Major Page Fault** (Disk I/O), causing the latency spike.
4. As the service "warmed up," the Kernel filled the Page Cache, and subsequent requests were served from RAM.

**The SRE Fix:**
Implement a **Warm-up Script** in the deployment pipeline:

```bash
# 'Warm' the cache before directing traffic to the service
cat /app/data/*.json > /dev/null

```

