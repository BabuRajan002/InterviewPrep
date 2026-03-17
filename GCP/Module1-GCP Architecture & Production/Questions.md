No worries at all! Here are all the interview questions from our BCE Group prep guide — clean and organised for you to read and practice:

---

# 🎯 BCE Group — GCP Interview Questions

---

## MODULE 1 — GCP Architecture & Production

**Q1: Walk me through how you would design a highly available GCP architecture for a production workload.**

Great effort Babu! Your answers have strong real experience behind them. Let me give you honest interviewer-style feedback on both.

---

## Q1 — Highly Available GCP Architecture

### What You Did Well ✅
- Starting with **clarifying questions** — excellent, senior engineers always do this
- **Real Rakuten example** — Tokyo + Osaka dual region is very impressive
- **GSLB failover** — shows you understand global load balancing
- **Cloud SQL with replicas** — good database HA mention

### What's Missing or Weak ⚠️

**1. You jumped straight to solution without structure**
Interviewers want to see your **thinking process** — not just the answer. Frame it in layers:
```
Networking layer → Compute layer → 
Database layer → Observability layer → Security layer
```

**2. GSLB explanation needs more depth**
You said *"configured two ingress IPs in GSLB as failover"* — interviewer will ask:
- What type of load balancer exactly?
- How does health checking work?
- What's the failover time?

**3. Missing key HA components:**
```
❌ Not mentioned:
- Cloud Armor (DDoS protection)
- Health checks configuration
- How traffic splits between regions (failover vs active-active)
- Observability / alerting
- RTO and RPO targets
```

**4. Cloud SQL HA vs Read Replica — conflated**
You said *"replicas configured in different regions"* — this needs clarification:
```
HA standby = same region, different zone, synchronous replication
             → automatic failover, zero data loss

Cross-region read replica = different region, asynchronous
                          → manual promotion, possible data loss
                          → used for DR, not HA
```

---

### Stronger Version of Your Answer

> *"Before answering I'd ask a few clarifying questions — what type of workload is it, what are the RTO/RPO requirements, and what regions are relevant. Based on that, I'll walk through my approach layer by layer.*
>
> *At the networking layer I'd use a Global HTTPS Load Balancer with Cloud Armor for DDoS protection — this gives us a single anycast IP that routes traffic to the nearest healthy region automatically. We implemented exactly this at Rakuten with Tokyo and Osaka regions as backends.*
>
> *At the compute layer I'd deploy GKE Autopilot clusters in both regions — each cluster spanning 3 zones within that region for zone-level resilience. Health checks on the GSLB backend services detect unhealthy regions and failover automatically — typically within 30–60 seconds.*
>
> *For the database layer I'd use Cloud SQL Enterprise Plus with High Availability enabled — this creates a synchronous standby in a different zone within the same region for automatic failover with zero data loss. For cross-region DR I'd add a read replica in the secondary region — which can be manually promoted if the primary region fails entirely. We migrated to Cloud SQL Enterprise Plus at Rakuten specifically for this capability.*
>
> *For observability I'd configure Cloud Monitoring with SLO-based alerting — tracking error rate and latency across both regions — and Cloud Logging with log sinks for audit trails.*
>
> *The result is an architecture with active-active compute, zero data loss database failover, and sub-60-second recovery time for most failure scenarios."*

---


Your **real Rakuten experience is gold** — Tokyo/Osaka dual region, 100Gbps interconnect, Cloud SQL Enterprise Plus — these details impress interviewers. The gap is just in structuring them into a clear narrative.

---

Ready to try **Q3 — Landing Zone** or move to **Security questions**? 💪

**Q2: How do you approach an on-premises to GCP migration?**

## Q2 — On-Premises to GCP Migration

### What You Did Well ✅
- **Network connectivity check first** — absolutely correct thinking
- **Dedicated Interconnect with dual connections** — impressive real detail
- **100Gbps line speed** — shows you know the actual infrastructure
- **DMS for database migration** — correct tool, correct reason
- **Data integrity monitoring** — good point

### What's Missing or Weak ⚠️

**1. No structured migration framework**
You jumped to specifics without a framework. Interviewers at senior level expect a phased approach:
```
❌ Your answer: jumped straight to network + database
✅ Expected: Assess → Plan → Migrate → Validate → Optimise
```

**2. "Migrate database first" needs justification**
You said always migrate database first — but this isn't always true and an interviewer will challenge it:
```
Actually the correct order depends on the workload:
- Stateless APIs → migrate first (easier, no data risk)
- Databases → migrate with CDC replication running in parallel
- Then cut over applications to new DB endpoint

The real answer is: run DB migration in parallel with 
application migration using DMS CDC replication
```

**3. Missing migration strategies**
```
❌ Not mentioned:
- Lift and shift vs re-architect decision
- How you handle cutover — maintenance window or zero downtime
- Rollback plan if migration fails
- How you validate post-migration (row counts, checksums)
- Strangler fig pattern for gradual traffic shifting
```

**4. Data security point was vague**
*"Data security can be confirmed using how it's connected"* — too vague for a senior role. Be specific:
```
Specific security measures during migration:
- Data encrypted in transit over Cloud Interconnect (MACsec)
- Data encrypted at rest in Cloud SQL (Google-managed keys or CMEK)
- IAM restricted to migration service accounts only during migration window
- VPC Service Controls to prevent data exfiltration
```

---

### Stronger Version of Your Answer

> *"I approach migration in four phases — Assess, Plan, Migrate, and Optimise.*
>
> *In the Assess phase I inventory all workloads — their dependencies, data volumes, compliance requirements, and current performance baselines. I categorise each workload as lift-and-shift, re-platform, or re-architect. For example at Rakuten we re-architected batch jobs as GKE CronJobs, re-platformed backend APIs to GKE, but lifted Redis to GCE to avoid code refactoring overhead.*
>
> *In the Plan phase I establish network connectivity first — at Rakuten we had dedicated Cloud Interconnect with dual 100Gbps connections to Tokyo and Osaka for private, high-bandwidth, low-latency connectivity. This is the foundation everything else depends on. I then define the migration sequence — typically stateless services first since they carry no data risk, then stateful services and databases.*
>
> *For the Migrate phase I use DMS with CDC replication for databases — this keeps the Cloud SQL target in continuous sync with on-premises while applications keep running. We validate data integrity throughout using row count comparisons and checksum verification. For cutover I prefer zero-downtime migration — switch application connection strings to Cloud SQL while DMS is still syncing, then stop replication. If anything fails the rollback is simply reverting the connection string.*
>
> *Throughout migration data security is enforced — traffic travels over private Cloud Interconnect, data is encrypted at rest using CMEK in Cloud SQL, and IAM is restricted to migration-specific service accounts.*
>
> *Post-migration I run the Optimise phase — rightsizing instances, enabling committed use discounts, configuring monitoring and alerting baselines."*

---

## Overall Score

| Criteria | Q1 | Q2 |
|---|---|---|
| **Real experience used** | ✅ Strong | ✅ Strong |
| **Structured framework** | ⚠️ Weak | ⚠️ Weak |
| **Technical depth** | ⚠️ Moderate | ✅ Good |
| **Edge cases covered** | ❌ Missing | ⚠️ Partial |
| **Confidence & clarity** | ✅ Good | ✅ Good |
| **Overall** | 6.5/10 | 7/10 |

---

## The Single Biggest Improvement for Both Answers

**Always use this structure:**
```
1. Clarifying question (30 seconds)
2. State your framework / phases (30 seconds)
3. Walk through each layer with real Rakuten examples (2-3 minutes)
4. Mention edge cases / failure scenarios (30 seconds)
5. Summarise the outcome (15 seconds)
```


**Q3: What is a GCP Landing Zone and how would you set one up?**

---

## MODULE 2 — GCP Security & Governance

**Q4: How do you implement least privilege IAM in GCP?**

**Q5: What are VPC Service Controls and when would you use them?**

**Q6: How would you use Security Command Centre (SCC) to improve security posture?**

---

## MODULE 3 — FinOps & Cost Optimisation

**Q7: How have you optimised GCP costs in production?**

**Q8: What is the difference between Committed Use Discounts and Sustained Use Discounts?**

---

## MODULE 4 — GCP Networking

**Q9: Explain the difference between VPC Peering, Shared VPC, and PSC — when would you use each?**

**Q10: How would you design networking for a multi-region GCP deployment?**

---

## MODULE 5 — Cloud Composer

**Q11: What is Cloud Composer and how does it differ from Cloud Functions or Pub/Sub for orchestration?**

---

## MODULE 6 — Databases & Data Migration

**Q12: You need to migrate a 2TB MySQL database from on-premises to GCP with minimal downtime. How do you approach it?**

---

## MODULE 7 — Monitoring, Logging & Observability

**Q13: How do you design an observability strategy for a GCP production environment?**

---

## MODULE 8 — Scenario Based & Edge Cases

**Scenario 1:** Your GKE cluster nodes are repeatedly running out of memory even though pod limits look fine. How do you debug?

**Scenario 2:** Your Cloud SQL instance is showing high CPU during business hours but queries look fast individually. What's happening?

**Scenario 3:** You need to ensure zero data loss during a Cloud SQL failover. How do you configure it?

**Scenario 4:** A developer accidentally deleted a production GCS bucket. How do you recover?

---

## MODULE 9 — Questions YOU Ask BCE Group

1. Is this role supporting Bell Canada's internal GCP infrastructure or building a platform for clients?
2. How large is the current Bangalore GDC team and what's the hiring plan?
3. Will this role have direct exposure to the Canadian parent team?
4. What GCP projects are currently running and what's the 12-month roadmap?
5. Is this a greenfield GCP setup or migration from existing infrastructure?

---

## 📋 How to Use These Questions

Here's my suggested approach:

| Step | Action |
|---|---|
| **Step 1** | Read each question and think about your answer |
| **Step 2** | Write your answer in your own words |
| **Step 3** | Share your answer here |
| **Step 4** | I'll give you feedback exactly like an interviewer |
| **Step 5** | We refine until the answer is strong |

---

**Start whenever you're ready** — just pick any question, write your answer, and I'll give you real interviewer-style feedback. Which question do you want to tackle first? 💪