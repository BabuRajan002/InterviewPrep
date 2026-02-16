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