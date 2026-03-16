This is an excellent way to prepare. To make this realistic for **Morgan Stanley**, we will use your real-world architecture: a **Host Project** (Networking/Shared VPC) and **Service Projects** (Applications/GKE/DBs).

Let's start with **Level 1: The Core Fundamentals (Questions 1-25)**.

---

### **Level 1: Core Fundamentals & GCP Integration (1-25)**

#### **Topic A: The Lifecycle & State (Architecture Focus)**

1. **Q:** You are starting a new project in the `service-project-1`. What are the first three commands you run, and what files do they create?
* **A:** 1. `terraform init`: Downloads providers and initializes the backend. Creates `.terraform/` and `.terraform.lock.hcl`.
2. `terraform plan`: Generates an execution plan.
3. `terraform apply`: Deploys the infra and creates `terraform.tfstate`.

## Follow-up 

This is a great follow-up. Understanding these two components is critical for a **Platform Engineer** because they deal with **environment consistency** and **reproducibility**—two things a bank like Morgan Stanley cares about deeply.

---

### **1. The `.terraform/` Folder (The "Working Directory")**

When you run `terraform init`, Terraform creates this hidden directory. Think of it as the **"local engine room"** for that specific project.

* **What’s inside:**
* **Provider Binaries:** The actual `.exe` or binary files for the Google provider (e.g., `terraform-provider-google`). Terraform doesn't come with cloud code built-in; it downloads it here.
* **Module Code:** If you are calling a module from Git or a local path, a copy of that code is stored here.
* **Backend Configuration:** Information about where your state file is stored (e.g., your GCS bucket details).


* **The Use Case:** It allows Terraform to run locally.
* **Critical Rule:** **Never commit this to Git.** Every engineer (and the CI/CD runner) must create their own `.terraform/` folder by running `terraform init`.

---

### **2. The `.terraform.lock.hcl` File (The "Dependency Lock")**

This file was introduced in Terraform 0.14 to solve the "it works on my machine" problem. It is a **Dependency Lock File**.

* **What’s inside:**
* **Version Constraints:** The exact version of the Google provider used (e.g., `5.10.0`).
* **Hashes (H1/H2):** Cryptographic signatures of the provider binary. This ensures that the binary downloaded on your laptop is **identical** to the one downloaded in the Morgan Stanley production pipeline.


* **The Use Case (The "Why"):**
* **Prevents Accidental Upgrades:** If Google releases version `6.0.0` today and it has a bug, your code won't automatically download it. It will see the lock file and stay on `5.10.0`.
* **Security:** It prevents "Supply Chain Attacks." If a hacker somehow replaced the Google provider with a malicious version, the cryptographic hash wouldn't match, and Terraform would refuse to run.


* **Critical Rule:** **Always commit this to Git.** This ensures that the entire team is "locked" into the same provider versions.

---

### **Platform Engineer Scenario (Morgan Stanley Style)**

**Interviewer:** *"I see you've committed the `.terraform.lock.hcl` but ignored the `.terraform/` folder. Why?"*

**Your Answer:**

> "I ignore the `.terraform/` folder because it contains platform-specific binaries and cached data that should be unique to the execution environment. However, I commit the `.terraform.lock.hcl` file because it acts as a **checksum for our dependencies**. In a financial environment, we need to guarantee that our CI/CD pipeline uses the exact same provider version that was tested in Dev. This prevents 'provider drift' and protects us against supply chain vulnerabilities."

2. **Q:** In a team environment, two engineers try to run `apply` at the same time on the Host Project. How do you prevent state corruption?
* **A:** Use a **Remote Backend with Locking**.
* **Config (`providers.tf`):**
```hcl
terraform {
  backend "gcs" {
    bucket = "ms-tf-state-bucket"
    prefix = "host-project/networking"
  }
}

```


*GCS natively supports locking.*


3. **Q:** You manually deleted a Firewall Rule in the GCP Console to troubleshoot. How do you make Terraform aware of this without changing infrastructure?
* **A:** Run `terraform refresh`. It updates the state file to match the actual state of GCP.

## Follow-up: `terraform refresh` VS `terraform import`

This is a fantastic observation and hits on one of the most common points of confusion in Terraform. You are absolutely correct: **`terraform refresh` only updates the State, not your code.**

Let's break down the mechanics of how this works and the critical difference between `refresh` and `import`.

---

### **1. The "Manual Deletion" Scenario**

If you delete a firewall manually and then run `terraform refresh`:

* **The State File:** Now says "The firewall is gone."
* **The `.tf` Code:** Still says "I want a firewall."

**When you run `terraform apply` next:**
Terraform compares the **Code** (Desired State) to the **State File** (Current Reality). It sees that the Code wants a firewall but the State says it's missing. Therefore, Terraform will **re-create** the firewall.

> **Interviewer Hook:** If they ask, "How do you make Terraform aware of this **without changing infrastructure**?", the answer is actually a two-step process:
> 1. Run `terraform refresh` (updates state).
> 2. **Manually delete the resource block from your `.tf` file** (to match the new reality).
> 
> 
> Only then will `terraform plan` show "No changes."

---

### **2. Terraform Refresh vs. Terraform Import**

Think of these as two different "directions" of synchronization.

| Feature | **Terraform Refresh** | **Terraform Import** |
| --- | --- | --- |
| **Direction** | Remote  State | Remote  State |
| **Use Case** | The resource is **already tracked** in state, but its attributes (like a tag or a IP) changed manually. | The resource **exists in GCP** but is **not tracked** in your state file at all. |
| **Code Requirement** | You must already have a resource block in your `.tf` file. | You must **write** a resource block first, then run the command to link it. |
| **Does it update Code?** | No. | No (it only populates the state). |

---

### **3. Scenario Comparison**

#### **Scenario A: Using `refresh**`

You have a Cloud SQL instance managed by Terraform. Someone manually changes the machine type from `db-n1-standard-1` to `db-n1-standard-2`.

1. You run `terraform refresh`.
2. Your **state file** now reflects the larger machine size.
3. If you run `apply` now, Terraform will try to **downgrade** it back to `standard-1` because your **code** still says `standard-1`.

#### **Scenario B: Using `import**`

Your Network Admin manually created a "Management-VPC" in the **Host Project** through the Console. You want to start managing it via Terraform.

1. You write an empty block: `resource "google_compute_network" "mgmt_vpc" {}`.
2. You run: `terraform import google_compute_network.mgmt_vpc projects/host-project/global/networks/management-vpc`.
3. Terraform now "owns" that VPC. You then have to fill in the arguments in your code to match the actual VPC settings so that `plan` shows zero changes.

---

### **4. Summary for Morgan Stanley Interview**

**Interviewer:** *"If I manually delete a resource, why isn't `refresh` enough?"*

**Your Answer:**

> "Because Terraform is **declarative**. `refresh` only synchronizes the state file with the real world, but the `.tf` configuration files remain the 'Source of Truth' for the desired state. If I refresh a deleted resource, the state shows it as null, but the code still requests it. On the next `apply`, Terraform will satisfy that request by re-creating it. To truly 'forget' the resource, I must remove the code block as well. `import`, on the other hand, is used for onboarding existing 'shadow IT' into our controlled state."

---

4. **Q:** You have an existing GKE cluster in the Service Project created manually. How do you bring it under Terraform management?
* **A:** 1. Write the `google_container_cluster` resource code.
2. Run `terraform import google_container_cluster.my_cluster projects/service-id/locations/zone/clusters/cluster-name`.


5. **Q:** What is the purpose of the `.terraform.lock.hcl` file, and should it be in `.gitignore`?
* **A:** It pins the exact version and checksum of the GCP Provider. It **must not** be ignored; it ensures every engineer at Morgan Stanley uses the same provider version.



---

#### **Topic B: Variables, Locals & Logic**

6. **Q:** You need to deploy the same API to `dev` and `prod` projects. How do you handle the project ID dynamically?
* **A:** Use **Input Variables**.
* **Config (`variables.tf`):**
```hcl
variable "gcp_project_id" { type = string }

```

## Follow-up:

In a real-world enterprise environment like Morgan Stanley, you would never keep all your code in one giant file. Instead, you use a **Directory-per-Environment** structure combined with **`.tfvars`** files.

This ensures that a mistake in the `dev` environment's code cannot accidentally destroy the `prod` environment, as they have completely separate state files.

### **1. Real-World Directory Structure**

Here is how your repository would look on your laptop and in Git:

```text
ms-migration-repo/
├── modules/
│   └── networking/          # Reusable code for VPCs
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── environments/
│   ├── dev/
│   │   ├── backend.tf       # Points to dev-state-bucket
│   │   ├── main.tf          # Calls the networking module
│   │   ├── variables.tf     # Declares gcp_project_id
│   │   └── terraform.tfvars # THE VALUES for DEV
│   └── prod/
│       ├── backend.tf       # Points to prod-state-bucket
│       ├── main.tf          # Calls the same module
│       ├── variables.tf     # Declares gcp_project_id
│       └── terraform.tfvars # THE VALUES for PROD

```

---

### **2. The Configuration Files (Step-by-Step)**

#### **Step A: The Module (`modules/networking/main.tf`)**

The module is generic. It doesn't know about "Dev" or "Prod" yet. It just uses a variable.

```hcl
# modules/networking/main.tf
resource "google_compute_network" "vpc" {
  name                    = "ms-shared-vpc"
  project                 = var.project_id # Pass the variable here
  auto_create_subnetworks = false
}

# modules/networking/variables.tf
variable "project_id" {
  type        = string
  description = "The GCP Project ID where the VPC will be created"
}

```

#### **Step B: The Environment Calling Code (`environments/dev/main.tf`)**

Now, in the `dev` folder, you "call" that module and pass the environment-specific project ID.

```hcl
# environments/dev/main.tf
module "network_dev" {
  source     = "../../modules/networking"
  project_id = var.gcp_project_id # Connects the local var to the module
}

# environments/dev/variables.tf
variable "gcp_project_id" {
  type = string
}

```

#### **Step C: The Secret Sauce (`environments/dev/terraform.tfvars`)**

This is where the actual hardcoded Project ID lives. **This is what changes between folders.**

```hcl
# environments/dev/terraform.tfvars
gcp_project_id = "ms-finance-dev-12345"

```

```hcl
# environments/prod/terraform.tfvars
gcp_project_id = "ms-finance-prod-99999"

```

---

### **3. The Execution Flow (Real-Time)**

When you are ready to deploy, your terminal workflow looks like this:

1. **Navigate to the environment:**
`cd environments/dev/`
2. **Initialize (Downloads the GCS state):**
`terraform init`
3. **Plan (Terraform automatically reads `terraform.tfvars`):**
`terraform plan`
*Output:* `Terraform will create 1 resource: google_compute_network.vpc in project "ms-finance-dev-12345"`
4. **Apply:**
`terraform apply -auto-approve`

---

### **4. Why Morgan Stanley asks this (The "Architect" perspective)**

* **Isolation:** If you run `terraform destroy` inside the `dev/` folder, the `prod/` folder is completely safe because they use different **backend buckets**.
* **DRY (Don't Repeat Yourself):** You wrote the networking code **once** in the `/modules` folder, but you deployed it to **two** different projects.
* **Auditability:** A manager can look at the `prod/terraform.tfvars` file and see exactly which project is being managed without reading complex code.

*Pass via `dev.tfvars` or `prod.tfvars`.*


7. **Q:** You want to ensure that every resource name starts with `ms-finance-`. How do you enforce this internally?
* **A:** Use a **Local Value**.
* **Config:**
```hcl
locals {
  prefix = "ms-finance-${var.env}"
}
resource "google_compute_network" "vpc" {
  name = "${locals.prefix}-vpc"
}

```




8. **Q:** How do you create 5 different Subnets in a Shared VPC using a single resource block?
* **A:** Use `for_each` with a map of subnet configurations.
* **Example:**
```hcl
resource "google_compute_subnetwork" "subnets" {
  for_each = var.subnet_map
  name     = each.key
  ip_cidr_range = each.value
  network  = google_compute_network.main.id
}

```

## Follow-up: Explain the different configuration files

In an enterprise environment like Morgan Stanley, the "Standard" is to avoid hardcoding. You want to define your subnets in a **Map** and use the `for_each` meta-argument. This makes your code scalable; if you need a 6th subnet tomorrow, you just add one line to your `.tfvars` file instead of writing new code.

Here is how you would structure this across your **Host Project** (where the Shared VPC lives).

---

### **1. Define the Variables (`variables.tf`)**

Instead of a simple string, we define a `map` of objects. This allows us to pass different CIDRs and regions for each subnet.

```hcl
variable "subnets" {
  type = map(object({
    cidr   = string
    region = string
  }))
  description = "A map of subnet names to their CIDR and region"
}

```

---

### **2. The Resource Block (`main.tf`)**

This is the "single block" that creates all 5 subnets.

```hcl
resource "google_compute_subnetwork" "shared_subnets" {
  # This loops through the map provided in terraform.tfvars
  for_each = var.subnets

  name          = each.key         # The key (e.g., "api-subnet")
  ip_cidr_range = each.value.cidr  # The value's cidr (e.g., "10.0.1.0/24")
  region        = each.value.region
  network       = google_compute_network.shared_vpc.id
  
  # Best practice for Shared VPCs
  private_ip_google_access = true 
}

```

---

### **3. The Data Input (`terraform.tfvars`)**

This is where you actually define the 5 subnets. This file is what you change when requirements grow.

```hcl
subnets = {
  "api-subnet" = {
    cidr   = "10.0.1.0/24"
    region = "us-east1"
  }
  "db-subnet" = {
    cidr   = "10.0.2.0/24"
    region = "us-east1"
  }
  "management-subnet" = {
    cidr   = "10.0.3.0/24"
    region = "us-east1"
  }
  "gke-nodes-subnet" = {
    cidr   = "10.10.0.0/20"
    region = "us-east1"
  }
  "proxy-only-subnet" = {
    cidr   = "10.0.4.0/24"
    region = "us-east1"
  }
}

```

---

### **Why this is the "Morgan Stanley Standard"**

1. **Immutability of the Key:** By using `for_each`, Terraform identifies each subnet by its **Name** (e.g., `google_compute_subnetwork.shared_subnets["api-subnet"]`). If you delete the 2nd item in the list, Terraform only deletes that specific subnet. (If you used `count`, deleting the 2nd item would cause Terraform to rename and shift every subnet after it, potentially causing a massive outage).
2. **Clean Code:** You have one resource block to maintain. If you want to add "Flow Logs" to all subnets, you add it once in `main.tf`, and it applies to all 5.
3. **Separation of Concerns:** Your logic (How to build a subnet) stays in `main.tf`, while your data (Which subnets to build) stays in `.tfvars`.

### **Interview Follow-up Question:**

**Interviewer:** *"What happens if I change the CIDR of one subnet in the `.tfvars` file and run apply?"*

**Your Answer:**

> "GCP does not allow changing the primary IP range of an existing subnet in-place. Terraform will detect the change in the `.tfvars` file, compare it to the state, and show a **'Force New Resource'** (Destroy and Recreate) in the plan. To prevent a production outage, I would advise against changing CIDRs on live subnets without a migration plan (like creating a new subnet and migrating workloads)."

9. **Q:** What is the difference between `count` and `for_each`?
* **A:** `count` is index-based (0,1,2). If you delete item 0, Terraform shifts everything. `for_each` is key-based; deleting one item doesn't affect others. **Always use `for_each` for GCP resources like VMs or Disks.**


10. **Q:** How do you handle a sensitive value like a Database password so it doesn't show up in the terminal logs?
* **A:** Mark the variable as `sensitive = true`.
* **Config:**
```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

```





---

#### **Topic C: Resource Dependencies & Lifecycle**

11. **Q:** You need to create a GKE cluster, but it **must** wait for a specific Service Account to be created first. How do you force this?
* **A:** Use the `depends_on` meta-argument inside the GKE resource block.


12. **Q:** How do you update a VM's machine type without deleting the VM if GCP allows it?
* **A:** Terraform handles this automatically via the Provider. If the API allows an "In-place" update, it will simply modify it. If not, it will show `-/+` (destroy and recreate) in the `plan`.


13. **Q:** How do you prevent an accidental `terraform destroy` from deleting your Production Cloud SQL instance?
* **A:** Use the `lifecycle` block.
* **Config:**
```hcl
lifecycle {
  prevent_destroy = true
}

```




14. **Q:** You are replacing a VM. You want the new VM to be created **before** the old one is deleted to ensure zero downtime. How?
* **A:** `lifecycle { create_before_destroy = true }`.


15. **Q:** Your Network team manually added tags to your instances for a security audit. How do you prevent Terraform from removing them?
* **A:** Use `lifecycle { ignore_changes = [tags] }`.



---

#### **Topic D: Providers & Data Sources**

16. **Q:** How do you configure Terraform to use two different GCP projects (Host and Service) in the same file?
* **A:** Use **Alias Providers**.
* **Config:**
```hcl
provider "google" { alias = "host" project = "host-id" }
provider "google" { alias = "service" project = "service-id" }

```
---

17. **Q:** You need the ID of a VPC that was created by another team. You don't manage the code. How do you get it?
* **A:** Use a **Data Source**.
* **Config:**
```hcl
data "google_compute_network" "shared_vpc" {
  name    = "ms-shared-vpc"
  project = "host-project-id"
}

```
## Follow-up: Explain the about the files

This is a crucial question for a **Platform Engineer** because it touches on **IAM (Identity and Access Management)** and **Cross-Project communication**, which are the bread and butter of working at a place like Morgan Stanley.

In a **Host/Service Project** architecture, the authentication isn't just "magic"—it relies on the **Service Account** running Terraform having the correct permissions in the other project.

---

### **1. How it Authenticates (The IAM Piece)**

When you run Terraform, you are usually authenticated as a **Service Account** (e.g., `terraform-runner@service-project-1.iam.gserviceaccount.com`).

For the `data` source to work across projects:

1. The Service Account from your **Service Project** must be granted the **`roles/compute.networkViewer`** role (or similar) on the **Host Project**.
2. Without this permission, the `data` source will return a "403 Forbidden" error, and Terraform will fail during the `plan` phase.

---

### **2. How the Configuration Looks**

Even if you don't own the code for the VPC, you use the `data` block to "query" the Google API for that specific resource's details using its name and project ID.

```hcl
# This tells Terraform: "Go ask the GCP API for information about this VPC"
data "google_compute_network" "shared_vpc" {
  name    = "ms-shared-vpc-prod"      # The name the other team gave it
  project = "ms-host-project-999"     # The PROJECT ID where it lives
}

# Now you can use the ID of that VPC in your own resource
resource "google_compute_subnetwork" "my_app_subnet" {
  name          = "app-subnet"
  project       = "ms-service-project-123" # Your project
  network       = data.google_compute_network.shared_vpc.id # Link to the discovered ID
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-east1"
}

```

---

### **3. The "Platform Engineer" Advanced Method (Remote State)**

The `data` source (above) queries the **GCP API** directly. However, in sophisticated environments, we often use a different data source called `terraform_remote_state`.

Instead of asking the Cloud API, you ask the **Terraform State File** of the other team.

* **Pros:** You get access to "outputs" that the other team explicitly shared (like a Subnet ID or a CIDR range).
* **Cons:** You need read-access to their **GCS Bucket** where their state is stored.

```hcl
data "terraform_remote_state" "network_team" {
  backend = "gcs"
  config = {
    bucket = "ms-terraform-state-host-project"
    prefix = "networking/vpc"
  }
}

# Usage:
# network = data.terraform_remote_state.network_team.outputs.vpc_id

```
---

### **4. Interview Answer for Morgan Stanley**

**Interviewer:** *"How does your Service Project Terraform code know about the VPC in our Host Project?"*

**Your Answer:**

> "We have two main ways. The most direct way is using a **GCP Data Source**. I provide the VPC name and the Host Project ID. For this to work, the Service Account executing our pipeline must have the **Compute Network Viewer** role assigned at the Host Project level. Alternatively, if the Network team has established a contract with us, we use **Terraform Remote State** to read their outputs directly from their GCS backend. This is often safer as it ensures we are using values that have already been validated by their state."

18. **Q:** What is the command to format your code to Morgan Stanley's standards?
* **A:** `terraform fmt -recursive`.


19. **Q:** How do you validate that your code is syntactically correct without running a plan?
* **A:** `terraform validate`.


20. **Q:** How do you view the current state file in a human-readable format via CLI?
* **A:** `terraform show`.



---

#### **Topic E: Output & Provisioners**

21. **Q:** After creating a GKE cluster, you need the endpoint IP to be used by a CI/CD script. How do you do this?
* **A:** Use an `output` block.
* **Config:** `output "cluster_endpoint" { value = google_container_cluster.primary.endpoint }`.


22. **Q:** Why is it a "Bad Practice" to use `local-exec` to run gcloud commands inside Terraform?
* **A:** It makes the code non-portable (requires gcloud on the runner) and Terraform cannot track the state of those commands.


23. **Q:** How do you remove a single resource from the state file without deleting it from GCP?
* **A:** `terraform state rm <resource_address>`.

## Follow-up: Explain it in real use case 

Spot on. You have the logic perfectly.

If you only run `terraform state rm`, you have "orphaned" the code. Here is the exact sequence of events and why each step matters for your interview:

### **The 2-Step Process**

1. **`terraform state rm <address>`**: This tells Terraform, *"Forget this resource exists. I don't want you to manage it anymore."* However, the resource **still exists** in the Google Cloud Console.
2. **Remove the Code**: You must then manually delete (or comment out) the `resource` block from your `.tf` file.

---

### **What happens if you forget Step 2?**

If you remove the resource from the **State** but keep the **Code**:

* On the next `terraform plan`, Terraform looks at your code and sees you want a resource (e.g., a specific VM).
* It checks the State and sees nothing there.
* It assumes the resource needs to be created from scratch.
* **The Error:** When you run `apply`, it will try to create the resource, but the GCP API will return an error: **"Resource already exists"** (because it's still physically there in the project).

---

### **Real-Time Scenario: Why would a Platform Engineer do this?**

At **Morgan Stanley**, you might use this in a **Migration** or **Refactoring** scenario.

**Scenario:** You have a GKE cluster that was managed in a monolithic "All-In-One" Terraform state. You want to move it to a new, dedicated "GKE-Only" state file without destroying the cluster (because people are using it!).

**The Workflow:**

1. Run `terraform state rm google_container_cluster.primary` in the **old project**.
2. Remove the code from the **old project**.
3. Write the code in the **new project**.
4. Run `terraform import google_container_cluster.primary <resource_id>` in the **new project**.

> **Interview Tip:** If the interviewer asks, *"How do you move a resource between two different state files without downtime?"*, the answer is exactly this: **`state rm`** from the source and **`import`** into the destination.

---

24. **Q:** What happens if you change the name of a resource in the `.tf` file but not the physical resource in GCP?
* **A:** Terraform will think the old resource was deleted and try to create a new one.


25. **Q:** How do you verify the version of the Terraform binary and the GCP provider you are using?
* **A:** `terraform version`.
