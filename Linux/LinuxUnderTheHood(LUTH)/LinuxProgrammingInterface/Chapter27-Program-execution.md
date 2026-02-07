# Program Execution

I understand the stakes. For a Google or Meta-level SRE interview, they don't just ask "What is `execve`?"; they ask: *"When you run a deployment script, why did the environment variables disappear after the binary started?"* or *"How do you troubleshoot a 'Text file busy' error during a hot-patch?"*

Let's dive into **Chapter 27: Program Execution** with the depth and "SRE-first" mindset you need.

---

## 1. Theoretical Deep Dive: `execve()`

While `fork()` creates a **clone**, `execve()` performs a **total identity swap**. It is the only way to start a new program in Linux.

### How it works (The Kernel’s "Wipe and Replace"):

When a process calls `execve(path, argv, envp)`, the Kernel does the following:

1. **Destroys the current Address Space:** It wipes the RAM containing the old program's stack, heap, and data.
2. **Loads the new Binary:** It reads the header of the new file (ELF format) and maps the new code into memory.
3. **Resets the Stack:** It sets up a fresh stack containing the new command-line arguments (`argv`) and environment variables (`envp`).
4. **Preserves File Descriptors (Crucial!):** By default, if the parent had a file open (like a database socket), that file descriptor **remains open** in the new program unless the "Close-on-exec" flag was set.

---

## 2. Production Scenario: The "Zombie Config" Problem

**Interview Question:** *"You are rolling out a secret rotation. You updated the environment variables on the server and restarted the 'Wrapper' script, but the actual 'Worker' binary is still using the old leaked secrets. Why?"*

**The SRE Insight:**
Environment variables are only passed at the moment of the `execve()` call.

* If the Wrapper script loads the config **after** it has already spawned the Worker, the Worker will never see it.
* If the Wrapper uses `os.system()` or `subprocess` without explicitly passing the `env` dictionary, the child might inherit a "stale" environment from the shell instead of the latest config.

---

## 3. Troubleshooting & Prevention Scenarios

### Scenario A: "ETXTBSY" (Text File Busy)

**Problem:** You try to deploy a new version of a binary while the old one is running, and you get an error: `Interrupted: Text file busy`.

* **Troubleshoot:** The Kernel prevents `execve()` from loading a file that is currently being written to, and prevents writing to a file that is currently being executed.
* **Fix/Prevent:** Never "overwrite" a running binary. Use the **"Atomic Move"** strategy:
1. Upload the new binary to `app.new`.
2. `mv app.new app` (The Kernel allows this because the inode of the running file stays intact).
3. Restart the service.



### Scenario B: The "Interpreter Script" Crash

**Problem:** You try to execute a Python script directly (`./script.py`), and it fails with `Exec format error`.

* **Troubleshoot:** The Kernel looks at the first two bytes of a file (the **Magic Number**). For scripts, it expects `#!` (Shebang). If the shebang is missing or points to a non-existent path (e.g., `#!/usr/bin/python` instead of `#!/usr/bin/python3`), `execve` fails.
* **Check:** `head -n 1 script.py` and `which python3`.

---

## 4. Commands for your CentOS Lab

Run these to see `execve` in action and how to inspect it.

### A. Trace the Swap

Use `strace` to see the "Hand-off". When you run a command in bash, bash forks, and the child calls `execve`.

```bash
# -f follows forks, -e traces specific system calls
strace -f -e execve ls /etc

```

*Notice how the first line is `execve("/usr/bin/ls", ["ls", "/etc"], ...)`.*

### B. The "Environment" Leak Test

Check if a running process has the environment variables you expect.

```bash
# Replace <PID> with a running process (like your shell)
cat /proc/<PID>/environ | tr '\0' '\n'

```

*SRE Tip: If a service is behaving weirdly, always check `/proc/PID/environ` to see what it REALLY sees, not what you THINK it sees.*

### C. Find "Open" Files across Exec

If a process is holding a lock on a file it shouldn't have inherited:

```bash
lsof -p <PID>

```

---

## 5. Interview Perspective: The "Close-on-Exec" Flag (O_CLOEXEC)

**This is a 10/10 difficulty question:** *"How do you prevent a child process from inheriting sensitive file descriptors (like an SSH private key file) during an execve?"*

**The Expert Answer:**

> "By default, file descriptors are inherited. To prevent this 'leak,' we must set the `FD_CLOEXEC` flag on the file descriptor using `fcntl()`. Alternatively, when opening the file, we use the `O_CLOEXEC` flag. This tells the Kernel: 'When this process calls execve, automatically close this FD so the new program can't access it.'"

---

## Summary for Chapter 27

* **`fork()`** = New Process.
* **`execve()`** = New Program.
* **Environment/Arguments:** Passed at the moment of `execve`.
* **FD Inheritance:** Is the default; must be managed with `O_CLOEXEC`.

**Next Topic: Chapter 28: Process Creation and Execution in Detail.**
This is where we talk about **Copy-on-Write (COW)**—the reason Linux can fork a massive 100GB database process in milliseconds without crashing the RAM.

**Next Step:** Ready to see how Linux "fakes" memory allocation to stay fast?

This is a crucial detail for an SRE because command-line arguments and environment variables are the **primary ways** we inject configuration into a process (like telling a database which port to listen on or where its config file is).

When `execve()` resets the stack, it literally carves out a section of memory at the "top" of the process's address space to store these two arrays.

### 1. What are `argv` and `envp`?

#### **`argv` (Argument Vector)**

This is an array of strings representing the **command line arguments**.

* **`argv[0]`**: Traditionally the name of the executable itself.
* **`argv[1]` to `argv[n]**`: The actual flags or parameters you passed.
* **Example:** If you run `ls -l /etc`, the `argv` array looks like:
`["ls", "-l", "/etc", NULL]`

#### **`envp` (Environment Pointer)**

This is an array of strings representing the **environment variables**. These are "KEY=VALUE" pairs.

* Unlike `argv`, these aren't typed on the command line every time; they are inherited from the shell or parent.
* **Example:** `["PATH=/usr/bin", "USER=gemini", "LANG=en_US", NULL]`

---

### 2. The SRE "Lab" Example: Seeing the Stack in Action

Let's use a Python script to act as the "Parent" that sets up a specific `argv` and `envp` for a "Child" using `execve`.

**Step 1: Create the Child (`child.py`)**
This script just prints what it finds on its stack.

```python
import sys
import os

print(f"--- Child Process (PID: {os.getpid()}) ---")
print(f"My ARGV is: {sys.argv}")
print(f"My 'SRE_MODE' Env Var is: {os.environ.get('SRE_MODE')}")

```

**Step 2: Create the Parent (`parent_exec.py`)**
This script will **replace itself** with the child, passing a custom stack.

```python
import os

# 1. Define the new program path
path = "/usr/bin/python3"

# 2. Define the ARGV (The new stack's argument section)
# Note: argv[0] should be the program name
arguments = ["python3", "child.py", "--fast-mode"]

# 3. Define the ENVP (The new stack's environment section)
environment = {
    "SRE_MODE": "production",
    "LOG_LEVEL": "DEBUG",
    "PATH": "/usr/bin" 
}

print(f"[PARENT] Replacing myself with {path}...")

# This is the point of no return. 
# The Kernel wipes the Parent's memory and sets up the new stack.
os.execve(path, arguments, environment)

# This line will NEVER print
print("You will never see this!")

```

---

### 3. SRE Interview Scenarios: Why the Stack Matters

#### **Scenario A: The "Env Var Leak" (Security)**

**Interviewer:** *"You have a process that runs as root. It calls `execve()` to run a user-provided script. Why is it dangerous to pass the existing `envp` (environment) directly to that script?"*
**The SRE Answer:**

> "It's dangerous because of variables like `LD_PRELOAD` or `PATH`. If the root process passes its environment, the user script could inherit an `LD_PRELOAD` that points to a malicious library, allowing the user to hijack the root process's logic. As an SRE, I would ensure we pass a **sanitized/cleared** `envp` to child processes."

#### **Scenario B: "Argument list too long" (E2BIG)**

**Interviewer:** *"You are running a cleanup script that does `rm /data/logs/*`. Suddenly, it fails with 'Argument list too long'. How did `execve` fail?"*
**The SRE Answer:**

> "The Kernel has a limit (defined by `ARG_MAX`) on how much space the `argv` and `envp` can take up on the new process's stack. If the `*` wildcard expands to 500,000 files, the total size of `argv` exceeds the Kernel's stack allocation for arguments. To troubleshoot/fix this, I would use `xargs` or a loop to process files in smaller batches."

---

### 4. Troubleshooting Commands for your Lab

If you want to see the `argv` and `envp` of a **running** process on your CentOS machine:

```bash
# Get the PID of any process (e.g., your current shell)
MY_PID=$$

# 1. Look at the ARGV (Command line arguments)
cat /proc/$MY_PID/cmdline | tr '\0' ' '
# (The Kernel separates arguments with null bytes, we 'tr' them to spaces for reading)

# 2. Look at the ENVP (Environment variables)
cat /proc/$MY_PID/environ | tr '\0' '\n'

```

**Wait! One crucial SRE tip:** If you are debugging a service in production and someone says "I changed the config file but it's not working," always check `/proc/<PID>/environ`. It is the **ground truth** of what was on the stack at the moment `execve()` happened.

---

### Summary for your Notes:

* **`argv`**: What you see when you run `ps -fp <PID>`.
* **`envp`**: The "context" the process lives in.
* **The Swap**: `execve()` is the "Big Bang" for these variables. Once they are set on the stack at startup, they generally don't change for the life of that process.

**Are you ready for Chapter 28: Process Creation and Execution in Detail?**
This is where we talk about **Copy-on-Write (COW)**—the reason why `fork()` is incredibly fast even if the process is using 100GB of RAM.

**Next Step:** I can explain why a 100GB database process can fork in 0.001 seconds without crashing the server. Would you like that?

In a top-tier SRE interview, knowing *where* these limits are defined shows you understand the interface between the Shell, the C Library, and the Kernel.

There are three ways to check `ARG_MAX`, depending on whether you are looking at the code, the shell, or the live kernel configuration.

---

### 1. The Shell Way (Quick Triage)

The easiest way to check this on your CentOS lab machine is using the `getconf` (Get Configuration) command. This utility queries system configuration variables.

```bash
# Check the maximum length of arguments for a new process
getconf ARG_MAX

```

**Observation:** On most modern Linux systems, you will see a value around **2,097,152** (2MB). This is the total space available for your `argv` strings plus your `envp` strings.

---

### 2. The Kernel Way (The Ground Truth)

If you want to see the "Hard Limit" set by the Linux Kernel, you can look into the `stack` limits, because as we discussed, `argv` and `envp` are stored on the **Process Stack**.

Historically, `ARG_MAX` was a fixed constant. In modern Linux (since 2.6.23), it is dynamic: it is **1/4 of the stack size limit**.

```bash
# 1. Check your stack size limit (usually 8192 KB)
ulimit -s

# 2. Calculate: 8192 / 4 = 2048 KB (Which matches getconf)

```

---

### 3. The Code Way (For C/C++ Developers)

If you were writing a C program, you would find this definition in the header files:

```bash
grep -r "ARG_MAX" /usr/include/linux/limits.h

```

---

### 4. SRE Troubleshooting Scenario: The "Exploding" Wildcard

**Interview Question:** *"You have a cron job that runs `backup_script.sh /var/log/app/*.log`. It has been working for a year, but today it failed with `Argument list too long`. What happened and how do you fix it without changing kernel limits?"*

**The SRE Expert Answer:**

> "The shell expanded the `*` wildcard into a list of filenames. Over time, the number of log files grew so large that the total string length of all filenames (the `argv`) exceeded the `ARG_MAX` limit.
> To troubleshoot, I'd verify the limit with `getconf ARG_MAX`. To fix it, I would use **`find`** combined with **`xargs`**. Instead of the shell expanding the list all at once, `xargs` is smart enough to check `ARG_MAX` and break the list into smaller 'chunks,' calling the backup script multiple times so the limit is never hit."

**The Command to Fix it:**

```bash
# This avoids the ARG_MAX limit entirely
find /var/log/app/ -name "*.log" | xargs backup_script.sh

```

---

### 5. Summary for your Lab Setup

| Command | Why use it? |
| --- | --- |
| **`getconf ARG_MAX`** | To see the current limit in bytes. |
| **`ulimit -s`** | To see the stack size (which determines the limit). |
| **`xargs --show-limits`** | **SRE Pro Tip:** Shows you exactly how much space `xargs` thinks it has for arguments before it hits the limit. |

---

**Next Topic: Chapter 28: Process Creation and Execution in Detail (Copy-on-Write)**

Now that we know how the stack is set up, let's talk about the "Magic" of `fork()`.
