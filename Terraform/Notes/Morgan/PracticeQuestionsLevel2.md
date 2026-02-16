Great! You’ve built a strong foundation. Moving into **Level 2: Modules & Infrastructure Reusability** is where the "Platform Engineer" title really earns its keep.

At Morgan Stanley, they don't want you to write `google_compute_instance` 100 times. They want you to write a **Module** once that everyone else in the bank uses to stay compliant.

---

### **Level 2: Modules & Infrastructure Reusability (26-50)**

#### **Topic A: Module Structure & Interaction**

**26. Q: What is the difference between a Local Module and a Remote Module? When would you use each?**

* **A:** * **Local Module:** Stored in a sub-folder of your current repo (e.g., `source = "./modules/gke"`). Used for project-specific logic or when the code is still in development.
* **Remote Module:** Stored in a separate Git repo or the Terraform Registry (e.g., `source = "github.com/org/repo//modules/vpc"`). Used to **share standardized code** across the entire company (e.g., "The Morgan Stanley Standard VPC").



**27. Q: In a Host/Service setup, how do you pass the VPC ID from the Host Project module to a GKE module in a Service Project?**

* **A:** You use **Outputs** and **Variables**. The Host Project module "outputs" the VPC ID, and the root configuration passes that output as an "input variable" into the GKE module.
* **Configuration Logic:**
```hcl
# 1. Host Project Module Output
output "vpc_id" { value = google_compute_network.shared_vpc.id }

# 2. Root main.tf
module "vpc_host" { source = "./modules/vpc" }

module "gke_service" {
  source = "./modules/gke"
  network_id = module.vpc_host.vpc_id # Passing the value
}

```



**28. Q: How do you specify a specific version of a Remote Git-based module?**

* **A:** Use the `ref` argument in the source URL.
* **Config:**
```hcl
module "vpc" {
  source = "git::https://github.com/ms/tf-modules.git//vpc?ref=v2.1.0"
}

```


*In a bank, you NEVER use the 'main' branch; you always pin to a specific version/tag.*

**29. Q: Why should you avoid using "absolute paths" (e.g., `/home/user/code`) in your module source?**

* **A:** It breaks portability. If you use an absolute path, the CI/CD runner or another engineer will not be able to run `terraform init` because they won't have that exact folder structure. **Always use relative paths** (starting with `./` or `../`).

**30. Q: If you add a new required variable to a module, what happens to existing projects using that module?**

* **A:** They will break on the next `plan`. To avoid this, you should either provide a **default value** for the new variable or use **semantic versioning** (Git tags) so existing projects don't pull the breaking change until they are ready.

---

#### **Topic B: Module Composition & Advanced Logic**

**31. Q: What is the "Hidden" `.terraform/modules` folder?**

* **A:** When you run `terraform init`, Terraform downloads a copy of all remote modules into this local folder. If you change the code in the remote Git repo, you must run `terraform init -upgrade` to pull the latest version into this folder.

**32. Q: How do you make a module "optional"? (e.g., only create a Bastion Host if a variable is set to true).**

* **A:** Use `count` with a conditional expression.
* **Config:**
```hcl
resource "google_compute_instance" "bastion" {
  count = var.deploy_bastion ? 1 : 0
  name  = "ms-bastion"
  # ...
}

```
## Follow up: Explain about the optional module and how it will be used for sepcific environments? 

Let’s simplify this. Think of a **Module** as a "Lego Set" (like a Castle) and **Terraform** as the "Instructions."

### **The Basic Idea**

Usually, if you write a module in your code, Terraform thinks: *"Okay, I MUST build this."* But what if you want the Castle in your "Playroom" (Dev) but **not** in your "Living Room" (Prod)? You need an **"On/Off Switch."**

---

### **1. The Switch (The Variable)**

In your `variables.tf`, you create a simple True/False question:

```hcl
variable "want_a_bastion" {
  type    = bool
  default = false  # By default, don't build it.
}

```

---

### **2. The Logic (The "Count" Trick)**

In Terraform, there is a special word called `count`.

* If `count = 1`, Terraform builds **one** of that thing.
* If `count = 0`, Terraform builds **zero** (nothing).

We use a "shortcut" formula to tell Terraform: *"If the variable is true, count is 1. If it's false, count is 0."*

**The Code (`main.tf`):**

```hcl
module "my_bastion" {
  source = "./modules/bastion"

  # This is the magic line:
  # Is var.want_a_bastion true? If yes (?), set count to 1. If no (:), set count to 0.
  count = var.want_a_bastion ? 1 : 0
  
  project_id = "ms-project-123"
}

```

---

### **3. How it looks in Real Life**

**Scenario A: In your DEV folder (`terraform.tfvars`)**

```hcl
want_a_bastion = true

```

**Result:** Terraform runs `count = 1`. You get your Bastion host.

**Scenario B: In your PROD folder (`terraform.tfvars`)**

```hcl
want_a_bastion = false

```

**Result:** Terraform runs `count = 0`. It **completely skips** the module. It won't even try to check if the code inside is correct.

---

### **Why is this "better"?**

Instead of having two different versions of code (one with a bastion and one without), you have **one single piece of code** that is smart enough to change itself based on the environment.

### **The "Simple" Interview Answer:**

> "To make a module optional, I use the `count` parameter on the module call. I link it to a boolean variable using a conditional expression (e.g., `count = var.enabled ? 1 : 0`). This allows me to use the exact same code for all environments while toggling specific features—like a Bastion host or a Monitoring tool—on or off just by changing a value in the `.tfvars` file."

---

**33. Q: How do you prevent a module from being used in the 'us-central1' region for compliance reasons?**

* **A:** Use a `validation` block inside the module's `variables.tf` to check the `region` variable against an allowed list.

**34. Q: What are "Nested Modules" and are they a good idea?**

* **A:** A nested module is a module that calls another module. While possible, "deep nesting" (more than 2 levels) is discouraged because it makes troubleshooting very difficult and complicates the passing of variables/outputs.

**35. Q: How do you pass a whole list of subnets into a module?**

* **A:** Define the variable in the module as a `list(string)` or `map(object)`.
* **Config:**
```hcl
variable "subnet_ids" { type = list(string) }

```



---

#### **Topic C: Real-World Scenario Scoped to Your Resume (Host/Service Project)**

**36. Q: Your Host Project has the Shared VPC. Your Service Project needs a Private GKE Cluster. What is the most critical piece of networking information you need from the Host Project to make this work?**

* **A:** You need the **Secondary IP Ranges** (Alias IPs) for Pods and Services defined in the Host Project's subnet. Without these range names, GKE cannot allocate IPs to containers.

**37. Q: How do you handle IAM permissions across modules?**

* **A:** It is best practice to include an `iam.tf` inside your module. For example, a GKE module should automatically create its own Service Account and assign the minimum necessary roles (`roles/logging.logWriter`, etc.) within that module.

**38. Q: How do you use `outputs` to show the connection string of a Cloud SQL instance after a module is applied?**

* **A:** In the module's `outputs.tf`:
```hcl
output "connection_name" { value = google_sql_database_instance.master.connection_name }

```


*In the root main.tf, you must also "re-output" it:*
```hcl
output "db_link" { value = module.sql_db.connection_name }

```



**39. Q: What is a "Flat" vs. "Hierarchical" module structure?**

* **A:**
* **Flat:** All resources are at the same level. Easy to read, but messy at scale.
* **Hierarchical:** Small, specialized modules (Network, Security, App) combined by a "Wrapper" module. This is the **Morgan Stanley Standard** for platform engineering.

## Follow-up: Difference between the folder structure of Flat module and hierarchial Module? 

In a Platform Engineering context, especially at a bank like Morgan Stanley, the difference between these two is about **Scale** and **Control**.

Think of it like a **small startup (Flat)** vs. a **large corporation (Hierarchical)**.

---

### **1. Flat Module Structure**

In a flat structure, you have one single module that does "everything." All resources (VPC, Subnets, GKE, IAM) are defined inside one folder.

**Example Structure:**

```text
modules/
└── gcp_infra/
    ├── vpc.tf
    ├── gke.tf
    ├── database.tf
    ├── variables.tf
    └── outputs.tf

```

**The Scenario:** You call the module `gcp_infra`, and it builds the entire stack.

* **Pros:** Easy for one person to understand; everything is in one place.
* **Cons:** Very hard to reuse. If a team only wants a Database but not a GKE cluster, they can't use this module. It becomes a "Monolith."

---

### **2. Hierarchical Module Structure**

This is the "Lego" approach. You build small, specialized **"Component Modules"** and then combine them into a **"Wrapper Module"** (also called a Blueprint).

**Example Structure:**

```text
modules/
├── networking/        # Specialized: Just VPCs and Firewalls
├── kubernetes/        # Specialized: Just GKE and Node Pools
├── security/          # Specialized: Just IAM and Service Accounts
└── blueprints/
    └── web_app_stack/ # HIERARCHICAL WRAPPER
        └── main.tf    # Calls networking, kubernetes, and security

```

**How it looks in the Blueprint (`blueprints/web_app_stack/main.tf`):**

```hcl
module "network" {
  source = "../../networking"
  # ... network configs
}

module "gke" {
  source     = "../../kubernetes"
  vpc_id     = module.network.vpc_id # Passing output from one to another
  # ... gke configs
}

```

---

### **3. Why Morgan Stanley uses "Hierarchical"**

As a Platform Engineer, your job is to provide **Guardrails**.

1. **Shared Responsibility:** The Networking team can own and update the `networking` module, while you own the `kubernetes` module.
2. **Versioning:** You can update the `security` module to fix a vulnerability, and all `blueprints` using that module will get the fix when they upgrade.
3. **Flexibility:** If a team needs a custom setup, they don't have to use the "Blueprint." They can just take your `kubernetes` and `security` modules and combine them with their own custom code.

---

### **Summary Table for the Interview**

| Feature | Flat Structure | Hierarchical Structure |
| --- | --- | --- |
| **Complexity** | Low (Initially) | Higher (More files) |
| **Reusability** | Poor (All or nothing) | Excellent (Mix and match) |
| **Maintenance** | Hard (Giant files) | Easy (Small, focused files) |
| **Standardization** | Difficult to enforce | **The Gold Standard** for Enterprises |

---

### **Interview Answer for Morgan Stanley:**

**Interviewer:** *"Should we build one big Terraform module for our application teams or break it down?"*

**Your Answer:**

> "I prefer a **Hierarchical structure**. In a large organization, a flat structure quickly becomes a 'monolithic' block of code that is hard to test and even harder to reuse. By breaking infrastructure into specialized component modules (Networking, GKE, IAM), we can allow different teams to contribute to their areas of expertise. We then provide 'Blueprints'—which are essentially hierarchical wrappers—that combine these components into a standardized stack for developers. This gives us the perfect balance of **agility for developers** and **governance for the platform team**."

---

**40. Q: You have a module that creates a GCS bucket. How do you allow users to add their own custom labels without editing the module code?**

* **A:** Define a variable `custom_labels = map(string)` with a default value of `{}`. In the resource block, use `merge(local.standard_labels, var.custom_labels)`.

---

## Follow-up: Explain about the merge function. 

In a Platform Engineering role, you want your modules to be **flexible but standardized**. You want to provide some "Standard Labels" (like `managed_by = "terraform"`) but allow the end-user to add their own (like `team = "payments"`).

The best way to do this is using the **`merge()`** function.

---

### **1. The Module Definition (`modules/gcs/variables.tf`)**

You define a variable for the custom labels and set the default to an empty map `{}` so it’s optional.

```hcl
variable "bucket_name" { type = string }

variable "custom_labels" {
  type    = map(string)
  default = {} # User doesn't HAVE to provide these
}

```

---

### **2. The Module Logic (`modules/gcs/main.tf`)**

Inside the module, you combine your "Global/Standard" labels with the user's "Custom" labels.

```hcl
locals {
  # These are labels that Morgan Stanley requires on EVERY bucket
  standard_labels = {
    provisioner = "terraform"
    org         = "ms-finance"
  }
}

resource "google_storage_bucket" "bucket" {
  name     = var.bucket_name
  location = "US"

  # merge() takes two maps and combines them into one.
  # If a key exists in both, the second map (custom_labels) wins.
  labels = merge(local.standard_labels, var.custom_labels)
}

```

---

### **3. The End-User Implementation (`environments/dev/main.tf`)**

The developer calling your module can now pass their specific labels without ever touching your module's code.

```hcl
module "app_bucket" {
  source      = "../../modules/gcs"
  bucket_name = "ms-dev-payments-assets"

  # User adds their specific labels here
  custom_labels = {
    team        = "payments-api"
    cost_center = "cc-1234"
    pii_data    = "false"
  }
}

```

---

### **The Result in GCP**

When you run `terraform apply`, the GCS bucket will end up with **5 labels**:

1. `provisioner = "terraform"` (From your local)
2. `org = "ms-finance"` (From your local)
3. `team = "payments-api"` (From the user)
4. `cost_center = "cc-1234"` (From the user)
5. `pii_data = "false"` (From the user)

---

### **Interview Answer for Morgan Stanley**

**Interviewer:** *"How do you handle metadata like labels or tags in a shared module?"*

**Your Answer:**

> "I use a combination of **local values** and the **`merge()` function**. I define a map of 'standard labels' within the module's locals to ensure every resource carries mandatory corporate metadata (like the provisioner and organization). I then expose a `custom_labels` variable as a map of strings. By using `labels = merge(local.standard_labels, var.custom_labels)`, I provide a flexible interface where users can add their own context without modifying the core module logic."

---

**41-50: Quickfire Scenario Round**
41. **Q:** Can a module return a sensitive value? (Yes, but the output must be marked `sensitive = true`).

## Follow-up: How it would have been defined in the output block? 

In a banking environment like Morgan Stanley, you often deal with sensitive data—like **Database passwords**, **Service Account keys**, or **API secrets**.

If you don't mark these as sensitive, Terraform will print them in plain text in your terminal and CI/CD logs (like Jenkins or GitHub Actions) during a `terraform apply`.

Here is how you handle this across your configuration files.

---

### **1. The Module Definition (`modules/db/outputs.tf`)**

Imagine your module creates a Cloud SQL user. You want to output the password so the application can use it, but you don't want it visible in the logs.

```hcl
# modules/db/main.tf
resource "random_password" "db_password" {
  length  = 16
  special = true
}

# modules/db/outputs.tf
output "db_password" {
  value     = random_password.db_password.result
  sensitive = true  # <--- This is the magic flag
}

```

---

### **2. The Root Configuration (`environments/dev/main.tf`)**

When you call the module, Terraform knows the output is sensitive. However, if you want to see it in your "Root" outputs, you **must also** mark the root output as sensitive.

```hcl
module "my_database" {
  source = "../../modules/db"
}

# You must repeat the sensitive flag here!
output "final_db_password" {
  value     = module.my_database.db_password
  sensitive = true
}

```

---

### **3. The "Real-Time" Terminal Experience**

When you run `terraform apply`, instead of seeing the password `P@ssw0rd123!`, you will see:

```text
Outputs:

final_db_password = <sensitive>

```

---

### **Important Warning for the Interview**

**Interviewer:** *"Does marking a value as `sensitive = true` encrypt it in the State file?"*

**Your Answer (The "Pro" Answer):**

> "No. It is a common misconception. The `sensitive` flag only prevents the value from being printed to the **console/logs**. The value is still stored in **plain text** inside the `terraform.tfstate` file. This is why, at Morgan Stanley, we must protect our state files using GCS buckets with restricted IAM permissions and ensure the bucket itself is encrypted at rest."

---

### **How do you actually see the value if you need it?**

If you genuinely need to see the password for a manual task, you can run:
`terraform output -json`
This will reveal the raw values. This is why access to the terminal where Terraform runs is a high-security privilege.

---

42. **Q:** How do you move a resource from the root main.tf into a module without destroying it? (Use `moved` blocks or `terraform state mv`).

## Follow-up: Can you explain how it can be achieved? 

This is a common "day-to-day" task for a Platform Engineer at a bank like Morgan Stanley. When you decide to "clean up" your code by moving a resource (like a VPC) into a module, Terraform’s default behavior is to think you deleted the old VPC and want a brand new one.

To prevent this (and avoid deleting production resources), you have two options: **The Modern Way (`moved` blocks)** and **The Legacy Way (`terraform state mv`)**.

---

### **Option 1: The Modern Way (Recommended for Terraform 1.1+)**

The `moved` block is code-based. It’s safer because it’s version-controlled and peer-reviewed.

#### **Step 1: Move the code**

Cut the resource from your `main.tf` and paste it into your module’s `main.tf`.

* **Old location:** `google_compute_network.my_vpc`
* **New location inside module:** `module.network_wrapper.google_compute_network.my_vpc`

#### **Step 2: Add the `moved` block**

In your root `main.tf`, add this block. It tells Terraform: "The thing that was *here* is now *there*."

```hcl
moved {
  from = google_compute_network.my_vpc
  to   = module.network_wrapper.google_compute_network.my_vpc
}

```

#### **Step 3: Run Plan**

When you run `terraform plan`, instead of seeing `1 to add, 1 to destroy`, you will see:
`Plan: 0 to add, 1 to change, 0 to destroy.`
Terraform will show a message: **"Resource moved"**.

#### **Step 4: Apply**

Once you apply, the state is updated. You can now delete the `moved` block from your code.

---

### **Option 2: The Legacy Way (Manual CLI)**

If you are on an older version of Terraform or need to do a quick fix, you use the CLI.

#### **Step 1: Identify the Addresses**

* Old Address: `google_compute_network.my_vpc`
* New Address (where it will be in the module): `module.network_wrapper.google_compute_network.my_vpc`

#### **Step 2: Run the command**

```bash
terraform state mv google_compute_network.my_vpc module.network_wrapper.google_compute_network.my_vpc

```

#### **Step 3: Verify**

Run `terraform plan`. It should show **"No changes"** because the state now perfectly matches your new code structure.

---

### **Summary Table for Comparison**

| Feature | **`moved` Block** | **`terraform state mv`** |
| --- | --- | --- |
| **Safety** | High (Code is reviewed) | Moderate (Manual CLI errors possible) |
| **History** | Recorded in Git | Not recorded |
| **Best for** | Large refactors and teams | Quick, one-off fixes |

---

### **Interview Answer for Morgan Stanley**

**Interviewer:** *"We have a flat structure but want to move to modules. How do you do this without causing a production outage?"*

**Your Answer:**

> "I would use the **`moved` block** feature introduced in Terraform 1.1. First, I refactor the code by moving the resource blocks into the new module. Then, I define a `moved` block in the root configuration to map the old resource address to the new module address. This allows Terraform to update the state file metadata without actually destroying or recreating the physical cloud resource. This is far superior to the old `terraform state mv` command because the 'move' logic is part of the code and can be peer-reviewed by the team."

---

### **Level 2 Quickfire Round: Q41, 43-50**

We covered 40 and 42. Here are the rest of the "reflex" answers:

43. **Q:** Where do you store the `providers.tf`? (In the Root environment folder, NOT inside the module).
44. **Q:** What is `terraform graph`? (Generates a visual map of resource dependencies).
45. **Q:** How do you handle multiple regions in one module call? (Use `for_each` on the module call itself).
46. **Q:** What is the `terraform get` command? (Downloads/Updates modules defined in the code).
47. **Q:** If a module source is `git::https://...`, can you use SSH instead? (Yes, use `git@github.com:...`).
48. **Q:** How do you test a module in isolation? (Create a `/examples` folder in the module repo with a test configuration).
49. **Q:** Can a module access a variable defined in the root if it isn't explicitly passed? (No, modules are encapsulated).
50. **Q:** How do you ensure a module only runs on Terraform version 1.5.0 or higher? (Use `required_version = ">= 1.5.0"` in a `terraform` block inside the module).

