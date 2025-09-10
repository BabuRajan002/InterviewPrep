Got it 👍 — here’s your **10 DevOps-oriented file-handling practice problems** (Set 2) in clean **Markdown format** so you can copy it into your notes or GitHub repo directly.

---

# 🧪 DevOps Python File Handling Practice (Set 2)

## 1) Read & Preview Safely (Basic)

**File:** `http_access_small.log`
**Task:**

* Print the **first 5 lines** and **last 5 lines** without reading the whole file.
* Print the **total line count**.
* *Hint:* use iteration for head, `collections.deque` for tail.

---
Perfect ✅ — here’s how you can **document your solution + feedback** in Markdown (ready for your repo). I’ll show it for **Problem 1** using your code and my review.

---

# Problem 1: Read & Preview Safely

**File:** `notes.txt`

### 📜 My Solution

```python
with open('notes.txt', 'r') as note:
    lst = note.readlines()

for i in range(3):
    print(lst[i])

print(f'The total line count is {len(lst)}')
```

### 📝 Explanation

* Used `with open(...)` to safely manage the file.
* Read all lines with `readlines()`.
* Printed the first 3 lines and total count.
* `with open` is preferred because the file is **automatically closed** when the block exits, even on errors.

---

### ✅ Feedback

* ✔️ Correct use of `with open`.
* ✔️ Output is correct for small files.
* ⚠️ `readlines()` loads the whole file into memory → not ideal for **very large logs**.
* ⚠️ Could strip newlines (`.strip()`) for cleaner output.

---

### 🔧 Suggested Improvement

```python
from itertools import islice

# Print first 3 lines without reading full file
with open("notes.txt", "r") as note:
    for line in islice(note, 3):
        print(line.strip())

# Count lines efficiently (streaming)
with open("notes.txt", "r") as note:
    count = sum(1 for _ in note)
print(f"Total line count: {count}")
```

---

### 💡 Interview Tip

* Interviewers may ask: *“How do you get both head & tail of a large file efficiently?”*
* Use `collections.deque` for the last N lines without reading everything into memory.

```python
from collections import deque
from itertools import islice

with open("notes.txt") as f:
    head = list(islice(f, 3))      # first 3 lines
with open("notes.txt") as f:
    tail = deque(f, maxlen=3)      # last 3 lines
print("Head:", [h.strip() for h in head])
print("Tail:", [t.strip() for t in tail])
```

---

👉 This Markdown format will let you track:

* Your code
* Explanation
* Reviewer feedback
* Improved version

---

## 2) Status Class Tally (Basic)

**File:** `http_access_small.log`
**Task:**

* Count requests per **status class** (2xx, 3xx, 4xx, 5xx).
* Print the **top 3 endpoints** by request volume.
* Save results to `access_summary.json`.

---

## 3) Gzipped Log Scanning (Basic → Medium)

**File:** `app.log.1.gz`
**Task:**

* Stream the gz file and count lines at each log level: INFO / DEBUG / WARN / ERROR.
* Print the **first timestamp** and **last timestamp** seen.
* Explain why streaming gz is better than extracting it fully first.

---

## 4) CSV Filter & Size Math (Medium)

**File:** `s3_inventory.csv`
**Task:**

* Sum the total **size\_bytes** for keys under `db/backups/` and print **size in MB**.
* Output the **largest 5 objects** (key + size) to `largest_objects.csv`.
* Code should not break if CSV column order changes.

---

## 5) JSON Lines Audit (Medium)

**File:** `users.jsonl`
**Task:**

* List all **inactive users** (`active=false`).
* For role = `devops` or `sre`, print users whose `last_login` is **older than 60 days**.
* Save both lists into `users_report.json` with two arrays:

  ```json
  {
    "inactive_users": [...],
    "stale_privileged_users": [...]
  }
  ```

---

## 6) Container Event Analysis (Medium)

**File:** `docker_events.json`
**Task:**

* Count **non-zero exitCode** events grouped by `container`.
* Print the **top 5 containers** with the most failures.
* Save output as TSV `container_failures.tsv`:

  ```
  container_name<TAB>failures
  ```

---

## 7) NGINX Config Lint (Medium → Hard)

**File:** `nginx.conf`
**Task:**

* Detect common issues:

  * `proxy_pass` under `/api/` missing a trailing slash.
  * Empty `location = /40x.html {}` block.
* Print warnings for issues and exit with **code 1** if any found.

---

## 8) K8s Audit Watch (Hard)

**File:** `k8s_audit.jsonl`
**Task:**

* Count **Failure** actions grouped by `user`.
* Print users with **≥ 5 failures**, broken down by `resource` and `namespace`.
* Save to `audit_hotspots.json` in a compact JSON format.

---

## 9) Backup Sanity Checks (Hard)

**File:** `backups_manifest.yaml`
**Task:**

* Flag backups with **`size_mb == 0`** or **all-zero sha256**.
* Print the last 3 backup entries with a status: OK / EMPTY / CORRUPT.
* Exit with non-zero status if any invalid backups exist.

---

## 10) Host Health Snapshot (Hard)

**Files:** `processes.txt`, `disk_usage.txt`
**Task:**

* From `processes.txt`: list processes with **%CPU ≥ 10** or **%MEM ≥ 2**.
* From `disk_usage.txt`: list mount points with **Use% ≥ 90%**.
* Save combined results to `host_health.json`:

  ```json
  {
    "hot_processes": [...],
    "full_disks": [...]
  }
  ```

---

✅ That’s your **practice sheet** — formatted in Markdown for clean tracking.
Would you like me to also generate a **checklist version** (with ✅/☐ boxes) so you can mark progress as you solve each one?
