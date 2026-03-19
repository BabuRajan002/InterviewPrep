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

Good answer — you have real experience here. Let me give you honest feedback.

---

## What You Did Well ✅

- **Real Rakuten example** — org → host project → service projects is correct
- **Shared VPC understanding** — host and service project model shows you know WHY not just WHAT
- **Interconnect connection** — good context on why Shared VPC was chosen

---

## What's Missing or Weak ⚠️

**The biggest problem — you described YOUR setup, not a Landing Zone**

An interviewer asking *"What is a Landing Zone"* expects you to first **define the concept** then walk through setup. Your answer jumped straight to your specific Rakuten topology.

```
What you answered:
"Here's how our Rakuten GCP is structured"

What was asked:
"What IS a Landing Zone and HOW would you SET ONE UP 
 from scratch for an enterprise"
```

**Missing components of a proper Landing Zone answer:**

```
1. Organisation structure      ❌ Not mentioned
   - Folders by environment/BU
   
2. Organisation Policies       ❌ Not mentioned
   - Restrict regions
   - Disable public IPs
   - Enforce labels
   
3. Billing setup               ❌ Not mentioned
   - Budget alerts per project
   - Billing export to BigQuery
   
4. Security baseline           ❌ Not mentioned
   - SCC enablement
   - Audit logging
   - VPC Service Controls
   
5. Centralised logging project ❌ Not mentioned

6. Identity & Access baseline  ❌ Not mentioned
   - Break glass accounts
   - Admin groups
```

---

## Stronger Version of Your Answer

> *"A Landing Zone is the foundational GCP environment structure that an enterprise sets up before deploying any workloads — it defines the governance, networking, security, and billing baseline that everything else builds on.*
>
> *I'd set it up in five layers:*
>
> *First — Organisation structure. I'd create a folder hierarchy under the org node — typically folders by environment like Production, Staging, and Development, or by business unit if it's a large enterprise. Each workload gets its own project within the appropriate folder — this gives billing isolation, IAM isolation, and quota isolation per workload.*
>
> *Second — Networking. I'd create a Shared VPC host project as the centralised networking hub. Service projects attach to this host and share its VPC — this gives centralised firewall management and routing. At Rakuten we did exactly this — our host project managed the Cloud Interconnect connections to Tokyo and Osaka, and all service projects including staging and production attached to it. This way on-premises connectivity is managed once, centrally.*
>
> *Third — Organisation Policies. I'd enforce policies at the org level — restrict resource locations to approved regions only, disable external IPs on GCE instances by default, enforce uniform bucket-level access on GCS, require OS login for GCE, and mandate labels for cost attribution.*
>
> *Fourth — Security baseline. I'd enable Security Command Centre at the org level, configure audit logging for all projects with log sinks routing to a centralised logging project, enable VPC Service Controls for projects handling sensitive data, and set up a break-glass process for emergency access.*
>
> *Fifth — Billing and FinOps. I'd configure billing export to BigQuery for cost analysis, set budget alerts per project and per folder, and enforce resource labelling — team, environment, application — so costs are attributable from day one.*
>
> *This is the structure I'd recommend for BCE Group's Bell Canada GDC — especially important since it sounds like a greenfield setup where getting the foundation right from the start prevents a lot of rework later."*

---

## Score

| Criteria | Your Answer | Target |
|---|---|---|
| **Defined what a Landing Zone is** | ❌ Missing | Required |
| **Organisation folder structure** | ⚠️ Partial | Required |
| **Shared VPC explanation** | ✅ Good | Required |
| **Org policies** | ❌ Missing | Required |
| **Security baseline** | ❌ Missing | Required |
| **Billing/FinOps setup** | ❌ Missing | Required |
| **Real experience connected** | ✅ Good | Good to have |
| **Overall** | **4/10** | **8/10** |

---

## Key Takeaway for This Question

```
Your Rakuten experience covers the NETWORKING layer well
But Landing Zone = Networking + Governance + Security + Billing + Identity

Think of it as:
"How do you set up GCP so it's enterprise-ready 
 BEFORE the first workload is deployed?"
```

---

## One Memory Framework — **NOPSB**

To never miss Landing Zone components:

```
N — Networking    (Shared VPC, Interconnect, subnets)
O — Org Policies  (region restriction, no public IPs, labels)
P — Projects      (folder hierarchy, workload isolation)
S — Security      (SCC, audit logs, VPC-SC, IAM baseline)
B — Billing       (export to BQ, budget alerts, labels)
```

Memorise **NOPSB** — cover all 5 in every Landing Zone answer.

---