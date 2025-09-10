# Python for DevOps: Key Areas to Master

## 1. The Basics: Your Foundation
Before you can automate the cloud, you need to know how to build a solid script. This is your foundation.  

**Topics:** Variables, conditionals, loops, functions, lists  

**Use case:** Writing a cleanup script that loops through files in a directory and removes logs older than 30 days.  

**Interview focus:** Can you write readable, working code under pressure? They want to see that you can think logically and structure a simple program.  

---

## 2. File & OS Automation: The Ground Game
So much of DevOps is about managing files and processes on a server. Your trusty terminal is great, but Python gives you more power and control.  

**Topics:** `os`, `shutil`, `subprocess`, `open()`  

**Use case:** A script that automates deployment by copying build artifacts to specific folders, running shell commands to restart services, and logging the output.  

**Interview focus:** How would you write a script to check if a service is running, restart it if it has failed, and log the result to a file?  

---

## 3. REST API Automation: Connecting Your Tools
Modern infrastructure is a collection of services that talk to each other via APIs. Being able to script these interactions is non-negotiable.  

**Topics:** `requests`, handling headers, auth tokens, parsing JSON  

**Use case:** Polling the GitHub Actions API to check the status of a build or writing a script that triggers custom alerts to a Slack channel when a deployment completes.  

**Interview focus:** Can you authenticate with an API (like a CI/CD tool), fetch the deployment
