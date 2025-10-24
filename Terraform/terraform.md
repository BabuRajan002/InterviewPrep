# Terraform commands

- `terraform validate` -> It checks the configurations everthing related to terraform files. 
- `terraform fmt` -> Scans the configuration file in current working directory format it in correct format.
- `terraform show` -> current state the infra 
- `terraform show json` -> Displays the current state of infra in a json format
- `terraform providers` -> shows all the providers used in the providers config file
- `terraform output` -> Displays all the output variables used in the terraform config file
- `terraform apply refresh-only` -> If any changes made outside the terraform control it will pick up the changes and update the state file. This will not modify any infra resources. IT WILL ONLY MODIFY THE STATE FILE.

## Terraform State commands
- `terraform state list` - Will display all the resources which are recorded inside the state file
- `terraform state show <resource_name>` - Will display all the attributes related to the single resource
- `terraform state mv <SOURCE> <DESTINATION>` - Will rename the resource present in the state file
- `terraform state pull` - which will pull the remote state file to locally
- `terraform rm ADDRESS` - Which will remove the resource from the state file it will NOT destroy the actual resource.
- `terraform state push ./terraform.tfstate` - used to push the local state file to the remote backend
- `terraform taint` - resource will be tainted and terraform will try to recreate the resource during the next apply command.

## Terraform workspace commands
- `terraform workspace list` - Lists workspaces 
- `terraform workspace new development` - It will create a new worksopace and switch into that! 
- `terraform workspace select production` - Used to switch to another workspace





