### Moving to Networking Scenario 2: The "Ghost" Latency

This scenario tests **DNS** and **Timeouts**, two things SREs deal with daily.

**The Symptom:**
You have a script that fetches data from an internal service: `curl http://internal-api.local/data`.

* Most of the time, it is lightning fast (10ms).
* Randomly, about 5% of the time, the exact same command takes **exactly 5.01 seconds** to finish, but the data it returns is correct.

**The Question:**

1. Why is the number **5 seconds** a "smoking gun" in Linux networking?
2. What is likely happening during those 5 seconds before the actual HTTP request even starts?
3. How would you use the `dig` command or check `/etc/resolv.conf` to investigate this?

**Hint:** Think about what happens if you have two `nameservers` listed in your configuration and the first one is flapping.

You are very close to the mark! The "flapping nameserver" is the perfect intuition. In a Google SRE interview, they want you to connect that "5.01 seconds" to the **default behavior of the Linux DNS resolver.**

### 1. The "5 Second" Smoking Gun

In Linux, the standard resolver library (glibc) has a default **timeout of 5 seconds**.

* **The Logic:** If you have two nameservers in `/etc/resolv.conf`, the resolver will try the first one. If that nameserver is down or "flapping," the resolver waits exactly 5 seconds for a response.
* **The Failover:** Once that 5-second timer hits, it gives up on the first server and tries the second one. The second one responds in 10ms.
* **Total Time:** 5 seconds (wait) + 10ms (success) = **~5.01 seconds**.

### 2. Why only 5% of the time?

If the first nameserver is "flapping" (intermittently failing), 95% of the time it works instantly. But 5% of the time, it's "dark," forcing that 5-second timeout.

### 3. Investigation & The `dig` Command

To prove this, you wouldn't just run a normal `dig`. You would test the nameservers **individually**:

* **Check the config:** `cat /etc/resolv.conf`
* *Result:* `nameserver 10.0.0.1` (Primary), `nameserver 10.0.0.2` (Secondary)


* **Test Primary:** `dig @10.0.0.1 internal-api.local`
* *Result:* If this hangs, you've found the broken server.


* **Check the "Search" path:** If your `/etc/resolv.conf` has multiple entries in the `search` line (e.g., `search prod.local dev.local`), the resolver might be trying to look up `internal-api.local.prod.local` first, failing, and then moving to the next one.

### 4. The SRE Fix

You can't always fix a flapping nameserver immediately, but you can make the application **more resilient**:

* **Options:** Add `options timeout:1 attempts:1` to `/etc/resolv.conf`.
* **Result:** Instead of waiting 5 seconds, it will wait 1 second before trying the next server. Your 5.01s delay becomes a 1.01s delay.

---

### Networking Scenario 3: The "MTU" Mystery (Advanced)

This is a "Hard" level scenario. It tests your knowledge of how packets are physically sized.

**The Symptom:**

* You can `ssh` into a remote server just fine. You can run small commands like `ls` or `whoami` and the output appears instantly.
* **However**, the moment you run a command with a large output (like `cat /var/log/syslog`) or try to `scp` a large file, the **session freezes**. No error message, it just stops moving.

**The Question:**

1. Why do **small** packets (like `ls`) get through, but **large** packets (like a file transfer) cause the connection to "hang"?
2. What is **MTU (Maximum Transmission Unit)**, and how does it relate to this "freeze"?
3. What is an **ICMP "Fragmentation Needed"** packet, and why is a firewall blocking it a disaster?

**Intuition Check:** Why would a "door" be big enough for a person but too small for a box?