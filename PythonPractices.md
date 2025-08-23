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
