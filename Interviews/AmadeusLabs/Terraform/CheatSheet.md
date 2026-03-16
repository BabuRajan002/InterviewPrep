Since you have already used Terraform to save **$2M in infrastructure costs** at Rakuten and are proficient in **Terraform state management** , we will skip the "What is a provider?" basics and dive into **Intermediate Scenario & Troubleshooting** questions suitable for a **Technical Lead/Platform Engineer** role.

Here are the first **5 of 50** questions focused on state, modularity, and environment consistency.

---

### **Scenario 1: The Corrupted State File**

**The Scenario:** You are applying a Terraform configuration in a shared environment. Suddenly, the network drops, and the process is killed. The next time you run `terraform plan`, you get an error stating that the **state file is locked** or potentially corrupted.

* **Troubleshooting Question:** How do you safely recover and ensure no "ghost" resources are left in GCP?
* **How to Approach:** Focus on state locking mechanisms and the risk of manual intervention.
* **The Solution/Commands:**
* **Check the lock:** If using a GCS backend (standard for GCP), identify the `Lock Info` ID from the error message.
* **Force Unlock:** Only after verifying no other team member is running a process, use:
`terraform force-unlock <LOCK_ID>`
* 
**State Verification:** Run `terraform refresh` to sync the state with real-world GCP resources.


* **Plan:** Run `terraform plan` to see if Terraform wants to "re-create" things that already exist.



### **Scenario 2: Importing Untracked Resources**

**The Scenario:** A developer manually created a **GCP Cloud Armor policy** and several **GKE Autopilot** clusters  through the Console. You need to bring these under Terraform management without destroying them.

* **Troubleshooting Question:** What is the step-by-step process to manage these via code?
* **How to Approach:** Emphasize that Terraform needs both the *code* and the *state entry* to match.
* **The Solution/Commands:**
1. **Write the Resource Block:** Create a `resource "google_compute_security_policy" "manual_policy" {}` in your `.tf` file.
2. **Import:** `terraform import google_compute_security_policy.manual_policy project-id/policy-name`
3. **Align:** Run `terraform plan`. It will show a "mismatch." Update your code attributes until the plan shows **"0 to add, 0 to change, 0 to destroy."**



### **Scenario 3: Modularizing for Scale**

**The Scenario:** Your current Terraform code is a single "monolith" file. You need to refactor it into **Modular Python-like structures** so that the **Bengaluru and Pune** teams can reuse the GKE networking logic.

* **Scenario Question:** How do you structure the modules and handle the "outputs" from a Networking module to a GKE module?
* **How to Approach:** Discuss the "Contract" between modules.
* **The Solution/Commands:**
* **Structure:** Create a `/modules/networking` and `/modules/gke` directory.
* **Passing Data:** Use `outputs.tf` in the networking module to export the `network_self_link`.
* **Consumption:**
```hcl
module "vpc" { source = "./modules/networking" }
module "cluster" { 
  source = "./modules/gke"
  vpc_id = module.vpc.network_id  # Reference the output
}

```


* **Command:** `terraform get` or `terraform init` to initialize the new module structure.



### **Scenario 4: Handling Secret Management**

**The Scenario:** You previously integrated **Fortanix** but have transitioned to **GCP Secret Manager**. You need to pass a database password to a GKE application via Terraform without hardcoding the secret in your version control (Bitbucket).

* **Troubleshooting Question:** How do you fetch an existing secret and pass it into a Kubernetes Secret resource?
* **How to Approach:** Use **Data Sources** to read existing infrastructure.
* **The Solution/Commands:**
* **Fetch Secret:**
```hcl
data "google_secret_manager_secret_version" "db_pass" {
  secret = "my-db-password"
}

```


* **Inject to K8s:**
```hcl
resource "kubernetes_secret" "app_secret" {
  data = { password = data.google_secret_manager_secret_version.db_pass.secret_data }
}

```


* **Security:** Ensure your `.tfstate` is stored in a secured GCS bucket with encryption, as state files store secrets in plain text.



### **Scenario 5: State "Drift" and Versioning**

**The Scenario:** A junior engineer changed the machine type of a GKE node pool in the GCP Console to "save money," but didn't update the Terraform code.

* **Troubleshooting Question:** How do you detect this "drift" and revert it to the "source of truth"?
* **How to Approach:** Explain that `plan` is a comparative tool.
* **The Solution/Commands:**
* **Detection:** `terraform plan -refresh-only` (In newer versions) or simply `terraform plan`.
* **Analyze:** Terraform will show that the real-world resource is `e2-medium` but the code says `n1-standard-1`.
* **Revert:** Simply run `terraform apply`. Terraform will see the mismatch and force the GCP API to change the machine type back to what is defined in your code.



---

**Would you like to proceed with the next 5 questions (6-10), perhaps focusing on Advanced CI/CD Integration with Cloud Build and Skaffold?**