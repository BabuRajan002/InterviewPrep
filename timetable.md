# Month 1 – Python + System Design (DevOps/SRE Focus)

## 📌 Overview
- Duration: 4 weeks (Month 1)
- Focus: 
  - Weeks 1–2 → Python for DevOps
  - Weeks 3–4 → System Design (DevOps/SRE flavor)
- Goal: Build strong scripting skills and system design foundations before moving to Linux, Networking, Docker, K8s, etc.

---

## Week 1: Python Foundations for DevOps

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | File Handling | Open/read/write files, CSV/JSON parsing, log analysis |
| Tue | OS Module | File/dir mgmt, env vars, permissions (`os`, `pathlib`) |
| Wed | Subprocess Basics | Run Linux cmds, capture stdout/stderr, error handling |
| Thu | Advanced File Handling | Regex parsing, `collections.Counter`, `defaultdict` |
| Fri | Subprocess Advanced | Popen, piping, parallel commands |
| Sat | Mini Project | Linux health-check script (disk, CPU, uptime) |
| Sun | Review & Mock | Script: check a process → restart if not running |

---

## Week 2: Python Advanced for DevOps

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | JSON Handling | load, dump, pretty-print, merging configs |
| Tue | YAML Handling | PyYAML, safe_load, convert YAML↔JSON |
| Wed | Requests & APIs | GET/POST, headers, params, error handling |
| Thu | API Auth & Retry | Tokens, sessions, backoff, exceptions |
| Fri | Threading & Multiprocessing | Parallel health checks, API calls |
| Sat | Mini Project | Script: Trigger Jenkins job via API, poll until completion |
| Sun | Review & Mock | Script: Parse Nginx logs → top 5 IPs hitting 500 errors |

---

## Week 3: System Design (DevOps/SRE Focus – Part 1)

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | Foundations | CAP theorem, availability vs consistency, scalability patterns |
| Tue | CI/CD at Scale | Pipelines for 10k engineers, zero-downtime deployments |
| Wed | Logging Systems | Log aggregation (ELK, GCP Logging, BigQuery) |
| Thu | Monitoring Systems | Metrics pipeline (Prometheus, Grafana), alerting at scale |
| Fri | Python Tie-In | Script: Parse logs → push metrics into Prometheus |
| Sat | Case Study | Design a logging system handling 1M events/sec |
| Sun | Review & Mock | CI/CD + monitoring system design interview |

---

## Week 4: System Design (DevOps/SRE Focus – Part 2)

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | Kubernetes at Scale | Multi-region clusters, HA API servers, etcd design |
| Tue | Networking in Design | CDN, Anycast, L4 vs L7 load balancing |
| Wed | Resiliency & Reliability | Failover, retries, circuit breakers, chaos testing |
| Thu | Hybrid Cloud & Security | VPN, Interconnect, IAM, service mesh |
| Fri | Python Tie-In | Script: Call K8s API → export pod info to YAML |
| Sat | Case Study | Design a multi-region K8s platform with HA |
| Sun | Review & Mock | Full mock design interview (system design + Python task) |

---

## ✅ End of Month 1 – Outcomes
- 14+ Python mini-projects (file handling, subprocess, APIs, logs, YAML/JSON).
- Strong Python foundations in **automation, APIs, log parsing, monitoring integration**.
- 4+ System Design case studies focused on **CI/CD, monitoring, K8s, hybrid infra**.
- Ready to move into Linux + Networking in Month 2 with solid Python + design base.
