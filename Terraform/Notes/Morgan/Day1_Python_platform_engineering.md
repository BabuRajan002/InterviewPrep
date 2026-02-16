### **The Basics You Need to Know**

1. **Google Cloud Python SDKs:** Specifically `google-cloud-compute`, `google-cloud-storage`, and `google-cloud-resourcemanager`.
2. **Authentication:** How to use `google.auth` and the `Client` classes.
3. **Data Structures:** Deep knowledge of **Dictionaries** and **Lists** (GCP API responses are essentially massive nested dictionaries).
4. **Error Handling:** Using `try-except` for API timeouts or "403 Forbidden" errors.
5. **Pagination:** Large projects have thousands of VMs; you must know how to iterate through pages of results using `list(request)`.

---

### **5 Critical Interview Questions (Day 5)**

#### **Q1: "We have a leak in our budget. How would you write a script to find all unattached 'zombie' Persistent Disks across 50 projects?"**

* **Approach:** You need to iterate through projects using the Resource Manager API, then check each disk's `users` attribute in the Compute API. If `users` is empty, the disk is unattached.
* **The Code:**

```python
from google.cloud import compute_v1

def find_zombie_disks(project_id):
    # Initialize the client
    client = compute_v1.DisksClient()
    # List all disks in all zones for the project
    request = compute_v1.AggregatedListDisksRequest(project=project_id)
    
    zombies = []
    for zone, response in client.aggregated_list(request=request):
        if response.disks:
            for disk in response.disks:
                # 'users' list is empty if the disk is not attached to a VM
                if not disk.users:
                    zombies.append(disk.name)
    return zombies

```

#### **Q2: "How do you handle API Rate Limiting (Quotas) in your Python automation?"**

* **Approach:** Mention **Exponential Backoff**.
* **Key Concept:** Use the `google-resumable-media` or built-in retry strategies in the SDK. Explain that you shouldn't just `time.sleep(1)`, but use a randomized increasing delay to avoid "Thundering Herd" problems.

In a banking environment, handling "Rate Limits" is about being a good citizen of the network. Imagine thousands of scripts running at once—if they all hit the GCP API at the same second, they will crash the service or get blocked.

Here is the simplest way to understand **Q2** (Rate Limiting and the Thundering Herd).

---

### **1. What is Rate Limiting?**

GCP (and every bank) has a limit on how many "requests per second" you can make. If you exceed this, the API returns an error: **`429: Too Many Requests`**.

### **2. The "Thundering Herd" Problem (The Simple Story)**

Imagine a grocery store that is closed for a 5-minute break.

* **The Problem:** 100 people are waiting outside. The second the door opens, all 100 people **run in at the exact same time**. They crash into the door, break the glass, and the store has to close again.
* **In Coding:** If a GCP service goes down for 10 seconds, and 1,000 of your Python scripts all retry the **exact second** it comes back up, you will crash the service again. This is the **Thundering Herd**.

### **3. The Solution: Exponential Backoff + Jitter**

To fix this, we don't just "retry." we use two tricks:

1. **Exponential Backoff:** Every time you fail, you wait **twice as long** as before.
* *Retry 1:* Wait 1 sec.
* *Retry 2:* Wait 2 sec.
* *Retry 3:* Wait 4 sec.


2. **Jitter (The Random Secret):** You add a small **random** amount of time so your 1,000 scripts don't all wake up at the exact same millisecond.
* *Script A:* Waits 2.1 sec.
* *Script B:* Waits 1.9 sec.
* *Script C:* Waits 2.3 sec.
* Now the "herd" is spread out, and the store (GCP) stays safe.



---

### **4. How the Code Looks (Simplified)**

You don't usually write this from scratch; you use the Google SDK's built-in tools. But here is the logic:

```python
import time
import random
from google.api_core import retry, exceptions

# 1. We define a "Retry" strategy
# 'initial' is the first wait time
# 'multiplier' is how much we increase (2.0 means double every time)
# 'maximum' caps the wait so we don't wait for hours
custom_retry = retry.Retry(
    initial=1.0, 
    multiplier=2.0, 
    maximum=60.0,
    predicate=retry.if_transient_error # Only retry if it's a 429 or 5xx error
)

def get_vm_status(instance_name):
    client = compute_v1.InstancesClient()
    
    # 2. We pass the 'retry' strategy into the API call
    # The SDK handles the Backoff and Jitter automatically!
    instance = client.get(
        project="my-project", 
        zone="us-central1-a", 
        instance=instance_name,
        retry=custom_retry 
    )
    return instance.status

```

---

### **5. Why this matters for the Morgan Stanley Interview**

If they ask about Python automation, say this:

> "When I write automation scripts for thousands of resources, I never use simple loops. I always implement **Retry Strategies with Exponential Backoff and Jitter**. This prevents the **Thundering Herd** problem and ensures our automation respects GCP’s API quotas, especially during large-scale infrastructure deployments where hundreds of runners might be active simultaneously."

### **Quick Checklist for you:**

* **429 Error:** Means "Slow down."
* **503 Error:** Means "I'm busy/down, try later."
* **Exponential:** 
* **Jitter:** Adding `random.uniform(0, 1)` to the wait time.

#### **Q3: "How would you automate the labeling of resources that were created manually (not via Terraform)?"**

* **Approach:** This is a governance script. It should look for resources without a specific `managed_by: terraform` label and apply a `compliance_risk: high` label or an `owner` tag based on the creator's email (found in Cloud Audit Logs).

In a banking environment, **Governance** means ensuring that every single resource has a "Source of Truth." If a resource isn't in Terraform, it's a security and cost risk.

This question tests if you can build a system that **Detects** non-compliant resources and **Remediates** them (tags them for deletion or review).

---

### **1. The Logic (How to Approach It)**

To solve this at a Lead Architect level, you shouldn't just list VMs. You use the **Cloud Asset Inventory (CAI) API**, which is much faster than querying every service individually.

1. **Search:** Use CAI to find all resources in the Project/Org.
2. **Filter:** Identify resources missing the `managed_by: terraform` label.
3. **Action:** Apply a "Warning" label (e.g., `compliance: non-compliant`) so the Security team can find them in a dashboard.

---

### **2. The Code (Pseudo-code for the Interview)**

Explain that you'd use the `google-cloud-asset` and service-specific libraries (like `google-cloud-compute`).

```python
from google.cloud import asset_v1
from google.cloud import compute_v1

def audit_and_label_resources(project_id):
    # 1. Initialize Asset Client to SEARCH everything
    asset_client = asset_v1.AssetServiceClient()
    scope = f"projects/{project_id}"
    
    # We query for resources MISSING the 'managed_by' label
    # The query "-labels.managed_by:*" means "where label managed_by does NOT exist"
    query = "-labels.managed_by:*"
    asset_types = ["compute.googleapis.com/Instance"] # We can add GCS, SQL etc.

    response = asset_client.search_all_resources(
        request={
            "scope": scope,
            "query": query,
            "asset_types": asset_types
        }
    )

    compute_client = compute_v1.InstancesClient()

    for asset in response:
        print(f"Found non-compliant resource: {asset.name}")
        
        # 2. Extract resource details (name is usually a full URL)
        # asset.name format: //compute.googleapis.com/projects/P/zones/Z/instances/I
        parts = asset.name.split('/')
        instance_name = parts[-1]
        zone = parts[-3]

        # 3. Apply the 'Warning' Label
        # Note: In GCP, to update labels, you must provide the 'fingerprint'
        instance = compute_client.get(project=project_id, zone=zone, instance=instance_name)
        
        new_labels = dict(instance.labels)
        new_labels["compliance_status"] = "manual_creation_detected"
        
        request = compute_v1.SetLabelsInstanceRequest(
            project=project_id,
            zone=zone,
            instance=instance_name,
            instances_set_labels_request_resource={
                "labels": new_labels,
                "label_fingerprint": instance.label_fingerprint
            }
        )
        compute_client.set_labels(request=request)
        print(f"Labeled {instance_name} as non-compliant.")


```

---

### **3. Explaining the Code (The "Architect" Walkthrough)**

* **`search_all_resources` with Query:** Explain that using a query like `-labels.managed_by:*` is high-performance. It lets GCP do the filtering for you instead of downloading thousands of resources and filtering in Python memory.
* **`label_fingerprint`:** This is a critical detail. In GCP, you cannot just "add" a label. You must provide the current `fingerprint` (a hash of existing labels). This is **Optimistic Locking**—it prevents you from overwriting labels if another process changed them at the exact same time.
* **`asset_types`:** Mention that this script is extensible. You can add `storage.googleapis.com/Bucket` or `sqladmin.googleapis.com/Instance` to the list to audit the whole bank.

---

### **4. Interviewer Follow-up: "Is this enough?"**

**Your Answer:** > "Labeling is the first step. In a production environment at Morgan Stanley, I would integrate this with **Cloud Audit Logs**. Instead of waiting for a script to run, we can use a **Log Sink** that triggers this Python script (via a Cloud Function) the *millisecond* a `compute.instances.insert` event occurs. This gives us **Real-time Governance**."

### **Basics You Must Know for this Code:**

* **Strings/Slicing:** How to get the instance name out of a long GCP resource URL (`split('/')`).
* **Dictionaries:** How to copy existing labels and add a new key (`dict(instance.labels)`).
* **API Structure:** Understanding that `compute_v1` is for actions, but `asset_v1` is for searching.

#### **Q4: "How do you parse a 100MB JSON Terraform State file to find all Public IP addresses?"**

* **Approach:** This tests your ability to handle local files and complex JSON.
* **Code Tip:** Use `json.load()` and a recursive function or list comprehension to dig through `resources` -> `instances` -> `attributes` -> `public_ip`.

In a banking environment, the **Terraform State file** is your source of truth. However, at Morgan Stanley's scale, a state file can easily reach **100MB+** if it contains thousands of resources.

This question tests two things:

1. **Technical Skill:** Can you handle large JSON files without crashing the server?
2. **Architectural Knowledge:** Do you understand the internal structure of Terraform state?

---

### **1. The Approach: Efficiency at Scale**

* **Memory Management:** Using `json.load()` on a 100MB file is fine for modern servers (it uses ~300-400MB of RAM), but in a constrained CI/CD runner, you must be careful.
* **Recursive Search:** Terraform state is deeply nested. Resources can be in the **root module** or inside multiple levels of **child modules**. A recursive function ensures you find `public_ip` no matter how deep it is hidden.

### **2. The Code: Recursive State Parser**

```python
import json

def find_public_ips(data, found_ips=None):
    """
    Recursively crawls the Terraform state JSON to find 'public_ip' keys.
    """
    if found_ips is None:
        found_ips = set()

    # If we find a dictionary, check its keys
    if isinstance(data, dict):
        for key, value in data.items():
            # In Terraform State, the actual IP is usually under 'attributes'
            if key == "public_ip" and value:
                found_ips.add(value)
            else:
                # If not the key we want, keep digging deeper
                find_public_ips(value, found_ips)
    
    # If we find a list (like the 'resources' or 'instances' list), check each item
    elif isinstance(data, list):
        for item in data:
            find_public_ips(item, found_ips)

    return found_ips

# Execution block
try:
    with open("terraform.tfstate", "r") as f:
        # json.load() is faster than line-by-line for 100MB 
        # because the file is one giant valid JSON object.
        state_data = json.load(f)
        
    public_ips = find_public_ips(state_data)
    
    print(f"✅ Found {len(public_ips)} unique Public IPs:")
    for ip in public_ips:
        print(f" - {ip}")

except FileNotFoundError:
    print("❌ Error: terraform.tfstate file not found.")
except json.JSONDecodeError:
    print("❌ Error: Failed to parse JSON. Is the state file corrupted?")

```

---

### **3. Explaining the Code to the Interviewer**

* **`isinstance(data, dict/list)`:** "I use these checks because Terraform state is a mix of nested objects and arrays. If I encounter a list (like the `instances` array), I iterate; if I encounter a dict, I search the keys."
* **`set()` vs `list()`:** "I store the IPs in a `set()` to automatically handle duplicates. In a large state, the same IP might appear in multiple metadata fields; a set ensures I only report unique values."
* **The "Recursive" Logic:** "Terraform stores resources in `module -> resources -> instances -> attributes`. Instead of writing four nested `for` loops, a recursive function handles any depth, including nested modules."

---

### **4. The "Architect" Level Bonus (The 10+ Year Pro Answer)**

If you want to really impress them, add this:

> "While parsing the raw JSON works, for a 100MB+ file in a production pipeline, I would actually use the command:
> `terraform show -json | jq -r '..|.public_ip? | select(. != null)'`
> This is more robust because `terraform show -json` normalizes the state format across different Terraform versions, ensuring my Python script doesn't break if HashiCorp changes the internal `.tfstate` schema."

### **Why this matters for Morgan Stanley:**

A 100MB state file is a "Blast Radius" risk. If your script finds **any** Public IPs in a production state file, it should trigger an immediate security alert, as banks generally strictly forbid public-facing cloud instances unless they are behind a specific WAF or Load Balancer.

[Learn how to manage large Terraform state files](https://www.youtube.com/watch?v=th3vsCDhujo)

This video explains the performance impacts and memory management strategies when dealing with massive JSON state files in Python, which is a critical skill for an enterprise-level architect role.

#### **Q5: "How do you secure the credentials your Python script uses?"**

* **Approach:** **NEVER** mention JSON keys.
* **The "MS" Answer:** "If running on-prem, I use **Workload Identity Federation**. If running on a GCE VM or Cloud Function, I use the **Attached Service Account** (Application Default Credentials). The script never sees a password; it just calls `compute_v1.InstancesClient()` and the SDK handles the token exchange automatically."

---

In a banking environment like Morgan Stanley, Python automation shouldn't rely on **Service Account JSON keys** (which can be leaked or stolen). Instead, we use **Application Default Credentials (ADC)** and **Identity Impersonation**.

### **The Logic: "Identity, Not Keys"**

* **The Problem:** Storing a `key.json` file in a GitHub secret or a VM is a security risk. If that key is compromised, the attacker has permanent access.
* **The Solution:** Use the identity already attached to the resource (like a GHA Runner or a GCE VM). The script "asks" Google for a temporary token.

---

### **The Example: Auditing GCS Buckets**

Imagine you need a script that runs inside a **Google Cloud Function** to check if a bucket has "Public Access" enabled.

#### **The Code:**

```python
import google.auth
from google.cloud import storage

def audit_bucket_security():
    # 1. 'google.auth.default()' automatically finds the 
    # attached Service Account. NO JSON PATH REQUIRED.
    credentials, project_id = google.auth.default()
    
    # 2. Use the credentials to initialize the client
    storage_client = storage.Client(credentials=credentials, project=project_id)
    
    buckets = storage_client.list_buckets()
    
    for bucket in buckets:
        # 3. Check for Public Access Prevention (Uniform Bucket-Level Access)
        policy = bucket.get_iam_policy(requested_policy_version=3)
        
        # In a bank, we want 'uniform_bucket_level_access_enabled' to be True
        is_secure = bucket.iam_configuration.uniform_bucket_level_access_enabled
        
        if not is_secure:
            print(f"⚠️ SECURITY ALERT: Bucket {bucket.name} allows fine-grained ACLs!")
        else:
            print(f"✅ Bucket {bucket.name} is following MS Governance standards.")

# Call the function
audit_bucket_security()

```

---

### **Explaining the "Architect" Parts:**

* **`google.auth.default()`:** This is the most important line. It looks for credentials in this order:
1. Environment variable `GOOGLE_APPLICATION_CREDENTIALS` (used in local dev).
2. Metadata Server (used when running on **GCE, GKE, or Cloud Functions**).


* **`uniform_bucket_level_access_enabled`:** At a bank, we disable individual object ACLs. We want IAM to be the **only** way to grant access. This script verifies that policy.

---

### **How to Answer in the Interview:**

**Interviewer:** *"How do you handle Service Account keys for your Python scripts?"*

**Your Answer:**

> "Actually, I follow a **Zero-Key policy**. For any script running on GCP—like a Cloud Function or a GKE Pod—I use **Workload Identity**. I initialize my Python clients using `google.auth.default()`, which fetches a short-lived OIDC token from the Metadata Server. This ensures that even if our code is exposed, there are no long-lived secrets to steal, and the permissions are strictly tied to the Service Account's IAM roles."

---

### **Day 5 Summary: What to memorize**

1. **The Client Pattern:** `client = service.Client()` (always initialized without hardcoded keys).
2. **The "Try-Except" Block:** Always wrap API calls to handle `403 Forbidden` (IAM issues) or `429` (Rate limits).
3. **Resource Discovery:** Use the `list_` methods to iterate through resources.

**You've mastered the Python Governance Day! Shall we move to Day 6: GKE, Networking, and Troubleshooting?**

