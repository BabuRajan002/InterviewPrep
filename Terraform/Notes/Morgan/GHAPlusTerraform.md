To secure a role at a firm like Morgan Stanley, you must demonstrate more than just "knowing Terraform." You need to show that you understand **enterprise governance**, **security-first automation**, and **production-grade state management**.

Here is the comprehensive sample repository structure and the GitHub Actions (GHA) workflow designed with industry best practices for GCP.

---

### **1. The Industry-Standard Repo Structure**

In a professional setting, you never put all code in one folder. You separate **Modules** (the blueprints) from **Environments** (the actual deployments).

```text
ms-gcp-infrastructure/
├── .github/
│   └── workflows/
│       ├── terraform-plan.yml    # Runs on Pull Requests (Read-only)
│       └── terraform-apply.yml   # Runs on Merge to Main (Write access + Approval)
├── modules/
│   ├── vpc/                     # Reusable Networking module
│   └── gke/                     # Reusable GKE module
├── environments/
│   ├── dev/
│   │   ├── main.tf              # Calls modules with dev values
│   │   ├── backend.tf           # GCS bucket config for Dev state
│   │   └── terraform.tfvars     # Dev-specific variables
│   └── prod/
│       ├── main.tf              # Calls modules with prod values
│       ├── backend.tf           # GCS bucket config for Prod state
│       └── terraform.tfvars     # Prod-specific variables
└── scripts/
    └── tf-check.py              # Custom Python script for policy/naming checks

```

---

### **2. The Production GHA Workflow (OIDC/WIF Edition)**

**Interview Tip:** Do NOT use JSON keys. Tell the interviewer: *"We use Workload Identity Federation (WIF) to eliminate long-lived secrets."*

#### **The "Plan" Workflow (`terraform-plan.yml`)**

This workflow acts as a "Gatekeeper" on Pull Requests.

```yaml
name: "Terraform Plan"

on:
  pull_request:
    branches: [ "main" ]

permissions:
  id-token: write # Required for WIF
  contents: read
  pull-requests: write # To post plan results as comments

jobs:
  plan:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        env: [dev, prod] # Runs plans for all modified envs
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # 1. Authenticate via Workload Identity Federation
      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          workload_identity_provider: 'projects/123456/locations/global/workloadIdentityPools/github-pool/providers/github-provider'
          service_account: 'terraform-planner@my-project.iam.gserviceaccount.com'

      # 2. Setup Terraform
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3

      # 3. Code Quality Checks (Critical for Interviews)
      - name: Terraform Format & Init
        run: |
          terraform fmt -check
          terraform init
        working-directory: ./environments/${{ matrix.env }}

      # 4. Security Scan (Shows Senior-level thinking)
      - name: Run tfsec
        uses: aquasecurity/tfsec-action@v1.0.0

      # 5. Generate Plan
      - name: Terraform Plan
        id: plan
        run: terraform plan -no-color -out=tfplan
        working-directory: ./environments/${{ matrix.env }}

      # 6. Post Plan to PR (For team review)
      - name: Update PR
        uses: actions/github-script@v7
        with:
          script: |
            const output = `#### Terraform Plan for ${{ matrix.env }} 📖`;
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: output
            })

```

---

### **3. Critical "Edge Case" Scenarios for the Interview**

Be prepared to answer these specific GHA + Terraform scenarios:

#### **Scenario A: The "Race Condition"**

**Q:** *"What happens if two PRs are merged at the same time? How do you prevent state corruption?"*

* **Answer:** *"First, the **GCS Backend** handles state locking natively. However, at the GHA level, I use **concurrency groups** in the workflow file. This ensures that only one 'Apply' runs at a time for a specific environment, queuing the others."*

#### **Scenario B: Failed Apply & State Lock**

**Q:** *"If a GHA runner crashes during an 'Apply', the state remains locked. How do you fix this?"*

* **Answer:** *"I would first verify that no processes are actually running in GCP. Then, I would use `terraform force-unlock <LOCK_ID>` using the ID provided in the failed GHA logs. In a bank, I’d ensure this is documented in a break-glass incident ticket."*

#### **Scenario C: Multi-Project Deployments**

**Q:** *"How does your GHA runner handle deploying to Project A and Project B?"*

* **Answer:** *"We use **Service Account Impersonation**. The GHA runner authenticates as a base identity, which then assumes different roles (using `google_service_account_iam_member`) for the target project's Service Account. This maintains a clear audit trail and follows the principle of least privilege."*

---

### **4. "Senior" Touches to mention in the Interview**

If you mention these 3 things, you will stand out from other candidates:

1. **Drift Detection:** Mention that you have a **scheduled GHA cron job** (e.g., every night) that runs `terraform plan` to check if someone manually changed something in the GCP Console.
2. **OIDC Conditionals:** Mention that your WIF provider is restricted *only* to the `main` branch for production deployments.
3. **Artifacts for 'Apply':** Explain that you don't run `plan` and `apply` separately. You run `plan -out=tfplan`, upload it as an **Action Artifact**, and then download that *exact* file for the `apply` step. This ensures what you saw in the PR is exactly what gets deployed.

**Would you like to deep-dive into the "Drift Detection" workflow or the "GCP Service Account Impersonation" logic?**

That is a perfect pivot. Morgan Stanley values the "Enterprise Reality" of your work at Rakuten—how you manage scale, speed, and safety in a high-traffic environment.

In this round, let’s focus on the **CI/CD Pipeline Architecture** (GitHub Actions), **Multi-Project Management**, and the **"Secure Supply Chain"** of your Terraform modules.

---

### **GCP & GitHub Actions: Round 2 (The Rakuten Scenarios)**

#### **Q11: In your GitHub Actions workflow, how do you authenticate to GCP without using long-lived Service Account JSON keys?**

**Answer:** I use **Workload Identity Federation (WIF)**.

* **Why:** JSON keys are a security risk (they can be leaked/stolen). WIF allows GitHub Actions to exchange a short-lived OIDC token for a temporary GCP access token.
* **Architecture:** I configure a Workload Identity Pool in GCP and map the GitHub repository (subject) to a specific Service Account with the required IAM roles.

#### **Q12: How do you handle the "Plan vs. Apply" consistency problem in a CI/CD pipeline?**

**Answer:** I use the **`-out` flag**.

* **The Workflow:** The `plan` job runs `terraform plan -out=tfplan`. This binary file is uploaded as a **GitHub Artifact**.
* **The Apply:** The `apply` job (which triggers only after PR merge or manual approval) downloads that specific artifact and runs `terraform apply tfplan`.
* **Benefit:** This ensures that the *exact* changes reviewed in the PR are what get deployed, preventing "race conditions" where someone merges a second PR in between your plan and apply.

#### **Q13: If a GitHub Action job fails halfway through a `terraform apply`, how do you handle the "Locked State"?**

**Answer:** First, I check the GCS bucket to see if the `.tflock` file exists.

* **In the Interview:** I would explain that I never manually delete the lock unless I've verified the GitHub runner has truly crashed. I would use `terraform force-unlock <LOCK_ID>`.
* **Pro Tip:** To prevent this, I recommend setting a `concurrency` group in the GitHub YAML so only one workflow can run on a specific state file at a time.

#### **Q14: How do you structure your Terraform repository for multiple GCP projects? One Repo per project or a Monorepo?**

**Answer:** At Rakuten (and preferred by MS), we often use a **Monorepo with a directory-per-project** or **Terragrunt**.

* **Structure:** ```text
/environments
/prod
/project-billing-a
/project-data-b
/modules (or a separate repo for shared modules)
```

```


* **Reason:** It allows for cross-project dependency management (e.g., Project B's firewall needs the IP output from Project A's Load Balancer).

#### **Q15: How do you ensure that "Sensitive" values (like DB passwords) don't appear in the GitHub Action logs?**

**Answer:** 1. I mark the variable as `sensitive = true` in Terraform.
2. I use **GitHub Secret Masking**. If a value is stored in a GitHub Secret, GitHub automatically redacts it from the logs.
3. **Advanced:** I prefer fetching the secret at *runtime* from **GCP Secret Manager** using a data source, rather than passing it as a GitHub Action environment variable.

#### **Q16: How do you implement "Policy as Code" in your GitHub Actions before the code reaches GCP?**

**Answer:** I integrate tools like **Checkov**, **TFLint**, or **Terrascan** as a "Pre-Plan" step.

* **Scenario:** If a developer tries to create a GCS bucket without "Uniform Bucket Level Access" enabled, the GitHub Action job fails immediately, even before `terraform plan` runs.

#### **Q17: How do you manage different "Environments" (Dev, Staging, Prod) in GitHub Actions?**

**Answer:** I use **GitHub Environments**.

* **The Setup:** I create three environments in the repo settings: `dev`, `stage`, and `prod`.
* **The Protection:** The `prod` environment is configured with a **Required Reviewer**. The GitHub Action will pause at the `apply` step until a Lead Architect (like myself) clicks "Approve."

#### **Q18: What is the "Remote State Data Source" strategy, and why is it crucial for cross-project collaboration?**

**Answer:** It’s how we share data without hardcoding.

* **Example:** The Network Team manages the VPC in Project A. My App Team in Project B needs to know the Subnet ID.
* **The Code:** I use `data "terraform_remote_state"` to read the output of the Network Team's state file (stored in a shared GCS bucket). This creates a "read-only" link between our projects.

#### **Q19: How do you handle "Module Versioning" when you need to push a breaking change to a shared module used by 5 different teams?**

**Answer:** I use **Git Tags** (Semantic Versioning).

1. I release the new version as `v2.0.0`.
2. Teams continue to use `v1.x.x` (pinned in their source) so they don't break.
3. I send a "Deprecation Notice" and the teams migrate to `v2.0.0` on their own sprint schedule.

#### **Q20: How do you optimize GitHub Action runners for Terraform in a large-scale GCP environment?**

**Answer:** I use **Self-Hosted Runners** on **GKE (Google Kubernetes Engine)**.

* **Why:** GitHub-hosted runners are slow and have limited access. By running the "Actions Runner Controller" (ARC) on GKE within our VPC, the runner has direct, high-speed private access to our GCP resources without needing to go over the internet.

---

### **Ready for Round 3?**

The next 10 will focus on **State File Refactoring (`moved` blocks), "Tainted" resources, and deep-dive GCP Networking with Terraform.**

**Any of these 10 (Q11-Q20) you'd like me to expand on? Specifically regarding your experience with WIF or GKE runners?**