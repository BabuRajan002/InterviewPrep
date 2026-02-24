# resource "google_container_cluster" "primary" {
#   name     = var.cluster_name
#   location = var.region
#   project  = var.project_id

#   # We specify the Host Project's VPC and Subnet
#   network    = var.network_self_link
#   subnetwork = var.subnetwork_self_link

#   # Networking Mode: VPC Native is mandatory for Shared VPC
#   networking_mode = "VPC_NATIVE"

#   ip_allocation_policy {
#     cluster_secondary_range_name  = var.pods_range_name
#     services_secondary_range_name = var.services_range_name
#   }

#   # Private Cluster Config (Standard for Banking)
#   private_cluster_config {
#     enable_private_nodes    = true
#     enable_private_endpoint = false # Keep endpoint public but restricted by master_authorized_networks
#     master_ipv4_cidr_block  = "172.16.0.0/28"
#   }

#   master_authorized_networks_config {
#     cidr_blocks {
#       cidr_block   = var.admin_ip_range
#       display_name = "Office-VPN"
#     }
#   }

#   # Workload Identity (Morgan Stanley Best Practice)
#   workload_identity_config {
#     workload_pool = "${var.project_id}.svc.id.goog"
#   }

#   # We remove the default node pool to create a custom one later
#   remove_default_node_pool = true
#   initial_node_count       = 1
# }

# # Separated Node Pool for better lifecycle management
# resource "google_container_node_pool" "primary_nodes" {
#   name       = "${var.cluster_name}-node-pool"
#   location   = var.region
#   cluster    = google_container_cluster.primary.name
#   project    = var.project_id
#   node_count = var.node_count

#   node_config {
#     machine_type = var.machine_type
    
#     # Workload Identity Metadata
#     workload_metadata_config {
#       mode = "GKE_METADATA"
#     }

#     # Best Practice: Specific Service Account for Nodes
#     service_account = var.gke_service_account_email
#     oauth_scopes    = ["https://www.googleapis.com/auth/cloud-platform"]
#   }
# }