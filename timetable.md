# Month 1 – DevOps/SRE Interview Preparation Plan

## 📌 Overview
- Duration: 4 weeks (Month 1)
- Focus: Python (daily), System Design (2 weeks), Linux + Networking
- Goal: Build strong foundations in scripting, system design, and troubleshooting

---

## Week 1: Python Foundations + Linux Core

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | Python – File Handling | Read/write files, CSV, JSON; parse logs, rotate backups |
| Tue | Python – OS Module | File/dir mgmt, permissions, env vars (`os`, `pathlib`) |
| Wed | Linux – Processes | ps, top, signals, background jobs, `/proc` |
| Thu | Python – Subprocess (Basics) | Run commands, capture output, error handling |
| Fri | Linux – Debugging | strace, lsof, dmesg, journalctl |
| Sat | Python + Linux Project | Build Linux health-check script (disk, CPU, uptime) |
| Sun | Review & Mock | Revise + script: "Check and restart service if down" |

---

## Week 2: Python Advanced + Networking Basics

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | Python – Advanced File Handling | Regex for log parsing, collections (`Counter`, `defaultdict`) |
| Tue | Networking – TCP/IP | Handshake, sockets, traceroute, MTU |
| Wed | Python – Subprocess (Advanced) | Popen, piping, parallel cmds |
| Thu | Networking – DNS & HTTP | DNS resolution, curl, headers, caching |
| Fri | Python – JSON/YAML Parsing | `json`, PyYAML; convert configs; safe_load |
| Sat | Networking Project | Write Python script → ping sweep + latency report |
| Sun | Review & Mock | Networking troubleshooting + Python log parser |

---

## Week 3: System Design (DevOps/SRE Focus, Part 1)

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | System Design Basics | CAP theorem, availability vs consistency, scalability patterns |
| Tue | CI/CD at Scale | Design pipelines for 10k engineers, zero-downtime deployments |
| Wed | Storage & Logging | Log aggregation (ELK/BigQuery), scaling ingestion pipelines |
| Thu | Monitoring Systems | Metrics pipeline (Prometheus, Grafana), alerting at scale |
| Fri | Python Practice | Script: Parse logs → push metrics into Prometheus |
| Sat | Design Case Study | "Design a logging system for 1M events/sec" |
| Sun | Review & Mock | Walk through CI/CD + monitoring design interview |

---

## Week 4: System Design (Part 2) + Networking Deep Dive

| Day | Topic | Sub-Topics / Practice |
|-----|-------|------------------------|
| Mon | Kubernetes at Scale | Multi-region clusters, HA API servers, etcd design |
| Tue | Networking in System Design | CDN, Anycast, load balancing (L4 vs L7) |
| Wed | Resiliency & Reliability | Failover, retries, circuit breakers, chaos testing |
| Thu | Hybrid Cloud & Security | VPN, Interconnect, IAM, service mesh |
| Fri | Python Practice | Script: Call Jenkins API, monitor job status |
| Sat | Design Case Study | "Design a multi-region K8s platform with HA" |
| Sun | Review & Mock | Full mock design interview + Python troubleshooting |

---

## ✅ End of Month 1 – Outcomes
- 14+ Python mini-projects (file handling, subprocess, APIs, logs, YAML/JSON).
- Strong Linux troubleshooting knowledge (processes, strace, lsof).
- Networking fundamentals (TCP/IP, DNS, HTTP, load balancing).
- 4 System Design case studies with DevOps/SRE flavor.
