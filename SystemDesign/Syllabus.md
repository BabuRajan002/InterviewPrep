Preparing for an SRE/DevOps role at a Tier-1 company like Google or Uber with 13 years of experience requires a shift from "how to build" to "how to scale and sustain."

Here is a 10-day intensive syllabus designed to take you from a standard system design mindset to the **NALSD (Non-Abstract Large Scale Design)** framework.

---

## Part 1: The 10-Day Technical Syllabus

### Days 1-2: Foundations of NALSD & The "SRE Mindset"

* **Focus:** Understanding the difference between abstract design (boxes and arrows) and non-abstract design (machines and math).
* **Topics:** * **The Iterative Design Process:** Feasibility phase (can it work?) vs. Reliability phase (can it survive?).
* **Hardware Limits:** Memorize "Latency Numbers Every Programmer Should Know" (L1 cache vs. Disk vs. Network).
* **SLIs/SLOs:** How to define "success" (e.g., 99.9% availability, <200ms latency).


* **Resource:** Read the [Google SRE Workbook: Chapter 12 on NALSD](https://sre.google/workbook/non-abstract-design/).

### Days 3-4: The Bill of Materials (BOM) & Math

* **Focus:** Back-of-the-envelope calculations.
* **Topics:** * **Throughput & Storage:** Calculating QPS, bandwidth saturation, and disk TB per year.
* **Provisioning:** If you need 10GB/s bandwidth and a server has 1Gbps NIC, you need 10 servers + 2 for redundancy ().
* **Calculations:** Practice converting 100k requests/sec into daily storage and required CPU cores.



### Days 5-7: Reliability Patterns & Trade-offs

* **Focus:** Designing for failure.
* **Topics:**
* **Failure Domains:** What happens when a rack, a datacenter, or a region fails?
* **Patterns:** Load balancing (L4 vs L7), Caching (TTL, Eviction), Circuit Breakers, and Retries with Exponential Backoff.
* **Storage Sharding:** How to partition data so a single node doesn't become a "hot spot."



### Days 8-10: Mock Problems & Refinement

* **Focus:** Full system walkthroughs.
* **Practice Problems:**
* Design a **distributed logging system** (LPS = 10M).
* Design a **global rate limiter**.
* Design a **metrics collection system** (Prometheus style).


* **Peer Review:** Try to explain your design to a peer, focusing on why you chose a specific number of machines.

---

## Part 2: The "Art of the Interview" (Communication)

With 13 years of experience, you are expected to **lead the conversation**. The interviewer will be intentionally vague.

### 1. How to Start: The Clarification Phase

Never start drawing immediately. Spend the first 5-8 minutes asking:

* **Scope:** "Are we designing the global ingestion or just the regional storage?"
* **Functional:** "Does the system need to support real-time searches or is 5-minute latency okay?"
* **Non-functional:** "What is our target availability? Three nines or five?"

### 2. How to Think Aloud (The "Verbal Stream")

Avoid silence. If you are doing math, say it:

> *"I'm calculating the storage now. 1 million writes per second at 1KB each is 1GB/s. Over a day, that's roughly 86TB. To keep this for a week, we need 600TB. I'll probably recommend 10TB SSDs, so we need at least 60 nodes just for storage."*

### 3. How to Pivot

If the interviewer says, *"What if the network between Europe and the US goes down?"* do not panic.

* **Good response:** *"That's a great point. Currently, my design has a single point of failure there. To fix this, I would introduce asynchronous replication and a local buffer in the Europe region to store logs until the link is restored."*

---

## Part 3: Confidence & "Seniority" Signals

* **Be Opinionated (with Reason):** Don't just say "I'll use a database." Say, "I'll use BigTable here because we need high-throughput writes and can tolerate eventual consistency."
* **Admit Trade-offs:** Every design has a weakness. Point it out before they do. *"This design is highly available but might have higher latency during peak hours."*
* **Ask for Feedback:** Periodically ask, *"Does this level of detail work for you, or should I dive deeper into the storage layer?"*

### Next Step for You

To get started on Day 1, I recommend watching a real Google SRE explain this process.

[SRE Classroom: How to Design a Distributed System](http://www.youtube.com/watch?v=ohtqI3AHR0k)

This video is a recorded workshop by Google SREs that walks through a real-world design problem (Distributed ImageServer) using the exact NALSD principles you need to master.