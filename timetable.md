# Month 1 – Python + System Design (DevOps/SRE Focus)

## 📌 Overview
- Duration: 4 weeks (Month 1)
- Focus: 
  - Weeks 1–2 → Python for DevOps
  - Weeks 3–4 → System Design (DevOps/SRE flavor)
- Goal: Build strong scripting skills and system design foundations before moving to Linux, Networking, Docker, K8s, etc.

---

## Week 1: Python Foundations for DevOps

| Day | Topic | Sub-Topics / Practice | References | My Notes/Refs |
|-----|-------|------------------------|------------|---------------|
| Mon | File Handling | Open/read/write files, CSV/JSON parsing, log analysis | [RealPython – File Handling](https://realpython.com/read-write-files-python/) | |
| Tue | OS Module | File/dir mgmt, env vars, permissions (`os`, `pathlib`) | [GeeksforGeeks – os module](https://www.geeksforgeeks.org/os-module-python-examples/) | |
| Wed | Subprocess Basics | Run Linux cmds, capture stdout/stderr, error handling | [RealPython – Subprocess](https://realpython.com/python-subprocess/) | |
| Thu | Advanced File Handling | Regex parsing, `collections.Counter`, `defaultdict` | [Python Docs – re](https://docs.python.org/3/library/re.html), [collections](https://docs.python.org/3/library/collections.html) | |
| Fri | Subprocess Advanced | Popen, piping, parallel commands | [DataCamp – Subprocess](https://www.datacamp.com/tutorial/python-subprocess) | |
| Sat | Mini Project | Linux health-check script (disk, CPU, uptime) | Combine refs above | |
| Sun | Review & Mock | Script: check a process → restart if not running | Practice session | |

---

## Week 2: Python Advanced for DevOps

| Day | Topic | Sub-Topics / Practice | References | My Notes/Refs |
|-----|-------|------------------------|------------|---------------|
| Mon | JSON Handling | load, dump, pretty-print, merging configs | [Python Docs – JSON](https://docs.python.org/3/library/json.html) | |
| Tue | YAML Handling | PyYAML, safe_load, convert YAML↔JSON | [RealPython – YAML](https://realpython.com/python-yaml/) | |
| Wed | Requests & APIs | GET/POST, headers, params, error handling | [Requests Docs](https://requests.readthedocs.io/en/latest/), [FreeCodeCamp API tutorial](https://www.youtube.com/watch?v=tb8gHvYlCFs) | |
| Thu | API Auth & Retry | Tokens, sessions, backoff, exceptions | [Medium – API Requests & JSON Parsing](https://medium.com/%40themathlab/api-requests-json-parsing-in-python-a-guide-in-data-collection-31e985981ea3) | |
| Fri | Threading & Multiprocessing | Parallel health checks, API calls | [RealPython – Concurrency](https://realpython.com/python-concurrency/) | |
| Sat | Mini Project | Script: Trigger Jenkins job via API, poll until completion | Jenkins API Docs | |
| Sun | Review & Mock | Script: Parse Nginx logs → top 5 IPs hitting 500 errors | Practice | |

---

## Week 3: System Design (DevOps/SRE Focus – Part 1)

| Day | Topic | Sub-Topics / Practice | References | My Notes/Refs |
|-----|-------|------------------------|------------|---------------|
| Mon | Foundations | CAP theorem, availability vs consistency, scalability patterns | [System Design Primer](https://github.com/donnemartin/system-design-primer) | |
| Tue | CI/CD at Scale | Pipelines for 10k engineers, zero-downtime deployments | [Google SRE Book – CI/CD](https://sre.google/sre-book/monitoring-distributed-systems/) | |
| Wed | Logging Systems | Log aggregation (ELK, GCP Logging, BigQuery) | [Elastic Stack Docs](https://www.elastic.co/what-is/elk-stack), [GCP Logging](https://cloud.google.com/logging/docs) | |
| Thu | Monitoring Systems | Metrics pipeline (Prometheus, Grafana), alerting at scale | [Prometheus Docs](https://prometheus.io/docs/introduction/overview/), [Grafana Docs](https://grafana.com/docs/) | |
| Fri | Python Tie-In | Script: Parse logs → push metrics into Prometheus | [Prometheus Python Client](https://github.com/prometheus/client_python) | |
| Sat | Case Study | Design a logging system handling 1M events/sec | [High Scalability Blog](http://highscalability.com/) | |
| Sun | Review & Mock | CI/CD + monitoring system design interview | Mock interview | |

---

## Week 4: System Design (DevOps/SRE Focus – Part 2)

| Day | Topic | Sub-Topics / Practice | References | My Notes/Refs |
|-----|-------|------------------------|------------|---------------|
| Mon | Kubernetes at Scale | Multi-region clusters, HA API servers, etcd design | [K8s Docs – High Availability](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/) | |
| Tue | Networking in Design | CDN, Anycast, L4 vs L7 load balancing | [Cloudflare Blog – Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/), [NGINX LB](https://www.nginx.com/learn/load-balancing/) | |
| Wed | Resiliency & Reliability | Failover, retries, circuit breakers, chaos testing | [Netflix Chaos Engineering](https://netflixtechblog.com/tagged/chaos-engineering) | |
| Thu | Hybrid Cloud & Security | VPN, Interconnect, IAM, service mesh | [GCP Hybrid Connectivity](https://cloud.google.com/architecture/hybrid-and-multi-cloud), [Istio Docs](https://istio.io/latest/docs/) | |
| Fri | Python Tie-In | Script: Call K8s API → export pod info to YAML | [Kubernetes Python Client](https://github.com/kubernetes-client/python) | |
| Sat | Case Study | Design a multi-region K8s platform with HA | [Google SRE Case Studies](https://sre.google/workbook/) | |
| Sun | Review & Mock | Full mock design interview (system design + Python task) | Mock interview | |

---

## ✅ End of Month 1 – Outcomes
- 14+ Python mini-projects (file handling, subprocess, APIs, logs, YAML/JSON).
- Strong Python foundations in **automation, APIs, log parsing, monitoring integration**.
- 4+ System Design case studies focused on **CI/CD, monitoring, K8s, hybrid infra**.
- Ready to move into Linux + Networking in Month 2 with solid Python + design base.
