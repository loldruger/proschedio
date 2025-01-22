from typing import Final

from proschedio.composer import Provider, Url

URL_ACCOUNT: Final[Url] = Url(Provider.VULTR).uri("account")
"""
- [Get] Get your Vultr account, permission, and billing information.
"""
URL_ACCOUNT_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("account/bandwidth")
"""
- [Get] Get your Vultr account bandwidth information.
"""
URL_APPLICATIONS: Final[Url] = Url(Provider.VULTR).uri("applications")
"""
- [Get] Get a list of all available Applications.
"""
URL_BACKUPS: Final[Url] = Url(Provider.VULTR).uri("backups")
"""
- [Get] Get information about Backups in your account.
"""
URL_BACKUPS_ID: Final[Url] = Url(Provider.VULTR).uri("backups/{backup-id}")
"""
- [Get] Get the information for the Backup.
"""
URL_BARE_METAL: Final[Url] = Url(Provider.VULTR).uri("bare-metals")
"""
GET: List all Bare Metal instances in your account.
POST: Create a new Bare Metal instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:

* `os_id`
* `snapshot_id`
* `app_id`
* `image_id`

Supply other attributes as desired.
"""

URL_BARE_METAL_ID: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}")
"""
GET: Get information for a Bare Metal instance.
PATCH: Update a Bare Metal instance. All attributes are optional. If not set, the attributes will retain their original values.

**Note:** Changing `os_id`, `app_id` or `image_id` may take a few extra seconds to complete.
DELETE: Delete a Bare Metal instance.
"""

URL_BARE_METAL_IPV4: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv4")
"""GET: Get the IPv4 information for the Bare Metal instance."""

URL_BARE_METAL_IPV6: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv6")
"""GET: Get the IPv6 information for the Bare Metal instance."""

URL_BARE_METAL_IPV4_REVERSE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv4/reverse")
"""POST: Create a reverse IPv4 entry for a Bare Metal Instance. The `ip` and `reverse` attributes are required."""

URL_BARE_METAL_IPV6_REVERSE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv6/reverse")
"""POST: Create a reverse IPv6 entry for a Bare Metal Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format."""

URL_BARE_METAL_IPV4_REVERSE_DEFAULT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv4/reverse/default")
"""POST: Set a reverse DNS entry for an IPv4 address."""

URL_BARE_METAL_IPV6_REVERSE_IPV6: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv6/reverse/{ipv6}")
"""DELETE: Delete the reverse IPv6 for a Bare metal instance."""

URL_BARE_METAL_START: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/start")
"""POST: Start the Bare Metal instance."""

URL_BARE_METAL_REBOOT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/reboot")
"""POST: Reboot the Bare Metal instance."""

URL_BARE_METAL_REINSTALL: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/reinstall")
"""POST: Reinstall the Bare Metal instance using an optional `hostname`.

**Note:** This action may take some time to complete.
"""

URL_BARE_METAL_HALT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/halt")
"""POST: Halt the Bare Metal instance."""

URL_BARE_METAL_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/bandwidth")
"""GET: Get bandwidth information for the Bare Metal instance.

The `bandwidth` object in a successful response contains objects representing a day in the month. The date is denoted by the nested object keys. Days begin and end in the UTC timezone. Bandwidth utilization data contained within the date object is refreshed periodically. We do not recommend using this endpoint to gather real-time metrics.
"""

URL_BARE_METALS_HALT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/halt")
"""POST: Halt Bare Metals."""

URL_BARE_METALS_REBOOT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/reboot")
"""POST: Reboot Bare Metals."""

URL_BARE_METALS_START: Final[Url] = Url(Provider.VULTR).uri("bare-metals/start")
"""POST: Start Bare Metals."""

URL_BARE_METALS_USER_DATA: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/user-data")
"""GET: Get the user-supplied, base64 encoded [user data] for a Bare Metal."""

URL_BARE_METALS_GET_AVAILABLE_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/upgrades")
"""GET: Get available upgrades for a Bare Metal.""" # Description from JSON

URL_BARE_METALS_GET_VNC: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vnc")
"""GET: Get the VNC URL for a Bare Metal.""" # Description from JSON

URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpcs/attach")
"""POST: Attach a VPC Network to a Bare Metal Instance.""" # Description from JSON

URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpcs/detach")
"""POST: Detach a VPC Network from an Bare Metal Instance.""" # Description from JSON

URL_BARE_METALS_LIST_VPCS: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpcs")
"""GET: List the VPC networks for a Bare Metal Instance.""" # Description from JSON

URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpc2/attach")
"""POST: Attach a VPC 2.0 Network to a Bare Metal Instance.""" # Description from JSON

URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpc2/detach")
"""POST: Detach a VPC 2.0 Network from an Bare Metal Instance.""" # Description from JSON

URL_BARE_METALS_LIST_VPCS2: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpc2")
"""GET: List the VPC 2.0 networks for a Bare Metal Instance.""" # Description from JSON

URL_BILLING_LIST_HISTORY: Final[Url] = Url(Provider.VULTR).uri("billing/history")
"""- [Get] Retrieve list of billing history."""

URL_BILLING_LIST_INVOICES: Final[Url] = Url(Provider.VULTR).uri("billing/invoices")
"""- [Get] Retrieve a list of invoices."""

URL_BILLING_GET_INVOICE: Final[Url] = Url(Provider.VULTR).uri("billing/invoices/{invoice-id}")
"""- [Get] Retrieve specified invoice."""

URL_BILLING_GET_INVOICE_ITEMS: Final[Url] = Url(Provider.VULTR).uri("billing/invoices/{invoice-id}/items")
"""- [Get] Retrieve full specified invoice."""

URL_BILLING_LIST_PENDING_CHARGES: Final[Url] = Url(Provider.VULTR).uri("billing/pending-charges")
"""- [Get] Retrieve list of billing pending charges."""

URL_BLOCK_STORAGE: Final[Url] = Url(Provider.VULTR).uri("blocks")
"""
- [Get] List all Block Storage in your account.
- [Post] Create new Block Storage in a `region` with a size of `size_gb`. Size may range between 10 and 40000 depending on the `block_type`.
"""

URL_BLOCK_STORAGE_ID: Final[Url] = Url(Provider.VULTR).uri("blocks/{block-id}")
"""
- [Get] Get information for Block Storage.
- [Patch] Update information for Block Storage.
- [Delete] Delete Block Storage.
"""

URL_BLOCK_STORAGE_ATTACH: Final[Url] = Url(Provider.VULTR).uri("blocks/{block-id}/attach")
"""
- [Post] Attach Block Storage to Instance `instance_id`.
"""

URL_BLOCK_STORAGE_DETACH: Final[Url] = Url(Provider.VULTR).uri("blocks/{block-id}/detach")
"""
- [Post] Detach Block Storage.
"""

URL_CDN_LIST_PULL_ZONES: Final[Url] = Url(Provider.VULTR).uri("cdns/pull-zones")
"""[Get] List CDN Pull Zones."""

URL_CDN_GET_PULL_ZONE: Final[Url] = Url(Provider.VULTR).uri("cdns/pull-zones/{pullzone-id}")
"""
[Get] Get information about a CDN Pull Zones.
[Put] Update information for a CDN Pullzone. All attributes are optional. If not set, the attributes will retain their original values.
[Delete] Delete a CDN Pull Zone.
"""

URL_CDN_PURGE_PULL_ZONE: Final[Url] = Url(Provider.VULTR).uri("cdns/pull-zones/{pullzone-id}/purge")
"""
[Get] Clears cached content on server proxies so that visitors can get the latest page versions.

**Note:** This action may only be performed once every six hours.
**Note:** This action may take a few extra seconds to complete.
"""

URL_CDN_LIST_PUSH_ZONES: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones")
"""
[Get] List CDN Push Zones.
[Post] Create a new CDN Push Zone.
"""

URL_CDN_GET_PUSH_ZONE: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones/{pushzone-id}")
"""
[Get] Get information about a CDN Push Zone.
[Put] Update information for a CDN Pushzone. All attributes are optional. If not set, the attributes will retain their original values.
[Delete] Delete a CDN Push Zone.
"""

URL_CDN_LIST_PUSH_ZONE_FILES: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones/{pushzone-id}/files")
"""
[Get] Get a list of files that have been uploaded to a specific CDN Push Zones.
[Post] Create a presigned post endpoint that can be used to upload a file to your Push Zone.  After sending this request you must send a second POST request to the returned URL. Include all of the returned inputs as form-data fields using the same key and value.  You must also include a field named \"file\" that holds the file to be uploaded.
"""

URL_CDN_DELETE_PUSH_ZONE_FILE: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones/{pushzone-id}/files/{file-name}")
"""
[Get] Get information about a CDN Push Zone file.
[Delete] Delete a CDN Push Zone file.
"""

URL_CONTAINER_LIST: Final[Url] = Url(Provider.VULTR).uri("registries")
"""
[Get] List All Container Registry Subscriptions for this account."""

URL_CONTAINER: Final[Url] = Url(Provider.VULTR).uri("registry")
"""
[Post] Create a new Container Registry Subscription."""

URL_CONTAINER_ID: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}")
"""
[Get] Get a single Container Registry Subscription.
[Put] Update a Container Registry Subscription.
[Delete] Deletes a Container Registry Subscription.
"""

URL_CONTAINER_REPOSITORY: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repositories")
"""
[Get] List All Repositories in a Container Registry Subscription."""

URL_CONTAINER_REPOSITORY_IMAGE: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repository/{repository-image}")
"""
[Get] Get a single Repository in a Container Registry Subscription.
[Put] Update a Repository in a Container Registry Subscription.
[Delete] Deletes a Repository from a Container Registry Subscription.
"""

URL_CONTAINER_DOCKER_CREDENTIALS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/docker-credentials")
"""
[Options] Create a fresh set of Docker Credentials for this Container Registry Subscription."""

URL_CONTAINER_KUBERNETES_DOCKER_CREDENTIALS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/docker-credentials/kubernetes")
"""
[Options] Create a fresh set of Docker Credentials for this Container Registry Subscription and return them in a Kubernetes friendly YAML format."""

URL_CONTAINER_ROBOTS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/robots")
"""
[Get] List All Robots in a Conainer Registry Subscription."""

URL_CONTAINER_ROBOT: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/robot/{robot-name}")
"""
[Get] Get a single Robot in a Container Registry Subscription.
[Put] Update the description, disable, duration, and add or remove access, in a Container Registry Subscription Robot.
[Delete] Deletes a Robot from a Container Registry Subscription.
"""

URL_CONTAINER_ARTIFACTS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repository/{repository-image}/artifacts")
"""
[Get] List All Artifacts in a Container Registry Repository."""

URL_CONTAINER_ARTIFACT: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repository/{repository-image}/artifact/{artifact-digest}")
"""
[Get] Get a single Artifact in a Container Registry Repository.
[Delete] Deletes an Artifact from a Container Registry Repository.
"""

URL_CONTAINER_LIST_REGIONS: Final[Url] = Url(Provider.VULTR).uri("registry/region/list")
"""[Get] List All Regions where a Container Registry can be deployed."""

URL_CONTAINER_LIST_PLANS: Final[Url] = Url(Provider.VULTR).uri("registry/plan/list")
"""[Get] List All Plans to help choose which one is the best fit for your Container Registry."""

URL_DATABASE_LIST_PLANS: Final[Url] = Url(Provider.VULTR).uri("databases/plans")
"""[Get] List all Managed Databases plans."""

URL_DATABASE_LIST: Final[Url] = Url(Provider.VULTR).uri("databases")
"""[Get] List all Managed Databases in your account.
[Post] Create a new Managed Database in a `region` with the desired `plan`. Supply optional attributes as desired.
"""

URL_DATABASE_GET: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}")
"""[Get] Get information about a Managed Database.
[Put] Update information for a Managed Database. All attributes are optional. If not set, the attributes will retain their original values.
[Delete] Delete a Managed Database.
"""

URL_DATABASE_USAGE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/usage")
"""[Get] Get disk, memory, and vCPU usage information for a Managed Database."""

URL_DATABASE_USERS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/users")
"""[Get] List all database users within the Managed Database.
[Post] Create a new database user within the Managed Database. Supply optional attributes as desired.
"""

URL_DATABASE_USER: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/users/{username}")
"""[Get] Get information about a Managed Database user.
[Put] Update database user information within a Managed Database.
[Delete] Delete a database user within a Managed Database.
"""

URL_DATABASE_USER_ACCESS_CONTROL: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/users/{username}/access-control")
"""[Put] Configure access control settings for a Managed Database user (Valkey and Kafka engine types only)."""

URL_DATABASE_LOGICAL_DATABASES: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/dbs")
"""[Get] List all logical databases within the Managed Database (MySQL and PostgreSQL only).
[Post] Create a new logical database within the Managed Database (MySQL and PostgreSQL only).
"""

URL_DATABASE_LOGICAL_DATABASE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/dbs/{db-name}")
"""[Get] Get information about a logical database within a Managed Database (MySQL and PostgreSQL only).
[Delete] Delete a logical database within a Managed Database (MySQL and PostgreSQL only).
"""

URL_DATABASE_TOPICS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/topics")
"""[Get] List all topics within the Managed Database (Kafka engine types only).
[Post] Create a new topic within the Managed Database (Kafka engine types only).
"""

URL_DATABASE_TOPIC: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/topics/{topic-name}")
"""[Get] Get information about a Managed Database topic (Kafka engine types only).
[Put] Update topic information within a Managed Database (Kafka engine types only).
[Delete] Delete a topic within a Managed Database (Kafka engine types only).
"""

URL_DOMAIN_LIST: Final[Url] = Url(Provider.VULTR).uri("domains")
"""
[Get] List all DNS Domains in your account.
[Post] Create a DNS Domain for `domain`. If no `ip` address is supplied a domain with no records will be created.
"""

URL_DOMAIN: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}")
"""
[Get] Get information for the DNS Domain.
[Put] Update the DNS Domain.
[Delete] Delete the DNS Domain.
"""

URL_DOMAIN_SOA: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/soa")
"""
[Get] Get SOA information for the DNS Domain.
[Patch] Update the SOA information for the DNS Domain. All attributes are optional. If not set, the attributes will retain their original values.
"""

URL_DOMAIN_DNSSEC: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/dnssec")
"""
[Get] Get the DNSSEC information for the DNS Domain."""

URL_DOMAIN_RECORDS: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/records")
"""
[Get] Get the DNS records for the Domain.
[Post] Create a DNS record.
"""

URL_DOMAIN_RECORD: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/records/{record-id}")
"""
[Get] Get information for a DNS Record.
[Patch] Update the information for a DNS record. All attributes are optional. If not set, the attributes will retain their original values.
[Delete] Delete the DNS record.
"""

URL_FIREWALL_GROUP_LIST: Final[Url] = Url(Provider.VULTR).uri("firewalls")
"""
[Get] Get a list of all Firewall Groups.
[Post] Create a new Firewall Group.
"""

URL_FIREWALL_GROUP_GET: Final[Url] = Url(Provider.VULTR).uri("firewalls/{firewall-group-id}")
"""
[Get] Get information for a Firewall Group.
[Put] Update information for a Firewall Group.
[Delete] Delete a Firewall Group.
"""

URL_FIREWALL_GROUP_RULES: Final[Url] = Url(Provider.VULTR).uri("firewalls/{firewall-group-id}/rules")
"""[Get] Get the Firewall Rules for a Firewall Group.
[Post] Create a Firewall Rule for a Firewall Group. The attributes `ip_type`, `protocol`, `subnet`, and `subnet_size` are required.
"""

URL_FIREWALL_GROUP_RULE: Final[Url] = Url(Provider.VULTR).uri("firewalls/{firewall-group-id}/rules/{firewall-rule-id}")
"""
[Get] Get a Firewall Rule.
[Delete] Delete a Firewall Rule.
"""

URL_INFERENCE_LIST: Final[Url] = Url(Provider.VULTR).uri("inference")
"""
[Get] List all Serverless Inference subscriptions in your account.
[Post] Create a new Serverless Inference subscription.
"""

URL_INFERENCE_GET: Final[Url] = Url(Provider.VULTR).uri("inference/{inference-id}")
"""
[Get] Get information about a Serverless Inference subscription.
[Patch] Update information for a Serverless Inference subscription.
[Delete] Delete a Serverless Inference subscription.
"""

URL_INFERENCE_USAGE: Final[Url] = Url(Provider.VULTR).uri("inference/{inference-id}/usage")
"""[Get] Get usage information for a Serverless Inference subscription."""

URL_INSTANCE_LIST: Final[Url] = Url(Provider.VULTR).uri("instances")
"""[Get] List all VPS instances in your account."""

URL_INSTANCE_CREATE: Final[Url] = Url(Provider.VULTR).uri("instances")
"""[Post] Create a new VPS Instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:

* `os_id`
* `iso_id`
* `snapshot_id`
* `app_id`
* `image_id`

Supply other attributes as desired.
"""

URL_INSTANCE_GET: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}")
"""
[Get] Get information about an Instance.
[Patch] Update information for an Instance. All attributes are optional. If not set, the attributes will retain their original values.
**Note:** Changing `os_id`, `app_id` or `image_id` may take a few extra seconds to complete.
[Delete] Delete an Instance.
"""

URL_INSTANCE_REINSTALL: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/reinstall")
"""
[Post] Reinstall an Instance using an optional `hostname`.

**Note:** This action may take a few extra seconds to complete.
"""

URL_INSTANCE_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/bandwidth")
"""
[Get] Get bandwidth information about an Instance.

The `bandwidth` object in a successful response contains objects representing a day in the month. The date is denoted by the nested object keys. Days begin and end in the UTC timezone. The bandwidth utilization data contained within the date object is refreshed periodically. We do not recommend using this endpoint to gather real-time metrics.
"""

URL_INSTANCE_NEIGHBORS: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/neighbors")
"""[Get] Get a list of other instances in the same location as this Instance."""

URL_INSTANCE_PRIVATE_NETWORKS: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/private-networks")
"""[Get] **Deprecated**: use [List Instance VPCs](#operation/list-instance-vpcs) instead.<br><br>List the private networks for an Instance."""


URL_INSTANCE_VPCS: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpcs")
"""[Get] List the VPCs for an Instance."""

URL_INSTANCE_VPC2S: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpc2")
"""[Get] List the VPC 2.0 networks for an Instance."""

URL_INSTANCE_ISO: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/iso")
"""[Get] Get the ISO status for an Instance."""

URL_INSTANCE_ISO_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/iso/attach")
"""[Post] Attach an ISO to an Instance."""

URL_INSTANCE_ISO_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/iso/detach")
"""[Post] Detach the ISO from an Instance."""

URL_INSTANCE_PRIVATE_NETWORKS_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/private-networks/attach")
"""[Post] Attach Private Network to an Instance.<br><br>**Deprecated**: use [Attach VPC to Instance](#operation/attach-instance-vpc) instead."""

URL_INSTANCE_PRIVATE_NETWORKS_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/private-networks/detach")
"""[Post] Detach Private Network from an Instance.<br><br>**Deprecated**: use [Detach VPC from Instance](#operation/detach-instance-vpc) instead."""

URL_INSTANCE_VPCS_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpcs/attach")
"""[Post] Attach a VPC to an Instance."""

URL_INSTANCE_VPCS_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpcs/detach")
"""[Post] Detach a VPC from an Instance."""

URL_INSTANCE_VPC2_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpc2/attach")
"""[Post] Attach a VPC 2.0 Network to an Instance."""

URL_INSTANCE_VPC2_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpc2/detach")
"""[Post] Detach a VPC 2.0 Network from an Instance."""
URL_INSTANCE_IPV4: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv4")
"""
[Get] List the IPv4 information for an Instance.
[Post] Create an IPv4 address for an Instance.
"""

URL_INSTANCE_IPV6: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv6")
"""[Get] Get the IPv6 information for an VPS Instance."""

URL_INSTANCE_IPV4_REVERSE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv4/reverse")
"""[Post] Create a reverse IPv4 entry for an Instance. The `ip` and `reverse` attributes are required."""

URL_INSTANCE_IPV6_REVERSE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv6/reverse")
"""
[Get] List the reverse IPv6 information for an Instance.
[Post] Create a reverse IPv6 entry for an Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format.
"""

URL_INSTANCE_IPV4_REVERSE_DEFAULT: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv4/reverse/default")
"""[Post] Set a reverse DNS entry for an IPv4 address."""

URL_INSTANCE_IPV6_REVERSE_IPV6: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv6/reverse/{ipv6}")
"""[Delete] Delete the reverse IPv6 for an Instance."""

URL_INSTANCE_START: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/start")
"""[Post] Start an Instance."""

URL_INSTANCE_REBOOT: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/reboot")
"""[Post] Reboot an Instance."""

URL_INSTANCE_HALT: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/halt")
"""[Post] Halt an Instance."""

URL_INSTANCE_USER_DATA: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/user-data")
"""[Get] Get the user-supplied, base64 encoded user data for an Instance."""

URL_INSTANCES_HALT: Final[Url] = Url(Provider.VULTR).uri("instances/halt")
"""[Post] Halt Instances."""

URL_INSTANCES_REBOOT: Final[Url] = Url(Provider.VULTR).uri("instances/reboot")
"""[Post] Reboot Instances."""

URL_INSTANCES_START: Final[Url] = Url(Provider.VULTR).uri("instances/start")
"""[Post] Start Instances."""

URL_INSTANCE_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/upgrades")
"""[Get] Get available upgrades for an Instance."""

URL_INSTANCE_BACKUP_SCHEDULE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/backup-schedule")
"""
[Get] Get the backup schedule for an Instance.
[Post] Set the backup schedule for an Instance in UTC. The `type` is required.
"""

URL_INSTANCE_RESTORE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/restore")
"""[Post] Restore an Instance from either `backup_id` or `snapshot_id`."""

URL_ISO: Final[Url] = Url(Provider.VULTR).uri("iso")
"""
[Get] Get the ISOs in your account.
[Post] Create a new ISO in your account from `url`.
"""

URL_ISO_ID: Final[Url] = Url(Provider.VULTR).uri("iso/{iso-id}")
"""
[Get] Get information for an ISO.
[Delete] Delete an ISO.
"""

URL_ISO_PUBLIC: Final[Url] = Url(Provider.VULTR).uri("iso-public")
"""[Get] List all Vultr Public ISOs."""


URL_KUBERNETES_LIST: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters")
"""
[Get] List all Kubernetes clusters currently deployed.\n
[Post] Create Kubernetes Cluster.
"""

URL_KUBERNETES_GET: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}")
"""
[Get] Get Kubernetes Cluster.
[Put] Update Kubernetes Cluster.
[Delete] Delete Kubernetes Cluster.
"""

URL_KUBERNETES_DELETE_WITH_LINKED_RESOURCES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/delete-with-linked-resources")
"""[Delete] Delete Kubernetes Cluster and all related resources."""

URL_KUBERNETES_RESOURCES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/resources")
"""[Get] Get the block storage volumes and load balancers deployed by the specified Kubernetes cluster."""

URL_KUBERNETES_AVAILABLE_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/available-upgrades")
"""[Get] Get the available upgrades for the specified Kubernetes cluster."""

URL_KUBERNETES_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/upgrades")
"""[Post] Start a Kubernetes cluster upgrade."""

URL_KUBERNETES_NODEPOOLS: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools")
"""
[Get] List all available NodePools on a Kubernetes Cluster.
[Post] Create NodePool for a Existing Kubernetes Cluster.
"""

URL_KUBERNETES_NODEPOOL: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}")
"""
[Get] Get Nodepool from a Kubernetes Cluster.
[Patch] Update a Nodepool on a Kubernetes Cluster.
[Delete] Delete a NodePool from a Kubernetes Cluster.
"""

URL_KUBERNETES_NODEPOOL_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}")
"""[Delete] Delete a single nodepool instance from a given Nodepool."""

URL_KUBERNETES_NODEPOOL_INSTANCE_RECYCLE: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}/recycle")
"""[Post] Recycle a specific NodePool Instance."""

URL_KUBERNETES_CONFIG: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/config")
"""[Get] Get Kubernetes Cluster Kubeconfig."""

URL_KUBERNETES_VERSIONS: Final[Url] = Url(Provider.VULTR).uri("kubernetes/versions")
"""[Get] Get a list of supported Kubernetes versions."""


URL_LOAD_BALANCER_LIST: Final[Url] = Url(Provider.VULTR).uri("load-balancers")
"""[Get] List the Load Balancers in your account."""

URL_LOAD_BALANCER_CREATE: Final[Url] = Url(Provider.VULTR).uri("load-balancers")
"""[Post] Create a new Load Balancer in a particular `region`."""

URL_LOAD_BALANCER_GET: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}")
"""
[Get] Get information for a Load Balancer.
[Patch] Update information for a Load Balancer. All attributes are optional. If not set, the attributes will retain their original values.
[Delete] Delete a Load Balancer.
"""

URL_LOAD_BALANCER_SSL: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/ssl")
"""[Delete] Delete a Load Balancer SSL."""

URL_LOAD_BALANCER_AUTO_SSL: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/auto_ssl")
"""[Delete] Remove a Load Balancer Auto SSL. This will not remove an ssl certificate from the load balancer."""

URL_LOAD_BALANCER_FORWARDING_RULES: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/forwarding-rules")
"""
[Get] List the fowarding rules for a Load Balancer.
[Post] Create a new forwarding rule for a Load Balancer.
"""

URL_LOAD_BALANCER_FORWARDING_RULE: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id}")
"""
[Get] Get information for a Forwarding Rule on a Load Balancer.
[Delete] Delete a Forwarding Rule on a Load Balancer.
"""

URL_LOAD_BALANCER_FIREWALL_RULES: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{loadbalancer-id}/firewall-rules")  # Note: Inconsistent hyphenation with other URLs. Consider changing to load-balancer-id for consistency.
"""[Get] List the firewall rules for a Load Balancer."""


URL_LOAD_BALANCER_FIREWALL_RULE: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{loadbalancer-id}/firewall-rules/{firewall-rule-id}") # Note: Inconsistent hyphenation with other URLs. Consider changing to load-balancer-id for consistency.
"""[Get] Get a firewall rule for a Load Balancer."""
URL_MARKET_PLACE_APP_VARIABLE: Final[Url] = Url(Provider.VULTR).uri("marketplace/apps/{image-id}/variables")
"""[Get] List all user-supplied variables for a Marketplace App."""
URL_OS: Final[Url] = Url(Provider.VULTR).uri("os")
"""[Get] List the OS images available for installation at Vultr."""

URL_PLAN: Final[Url] = Url(Provider.VULTR).uri("plans")
URL_PLAN_METAL: Final[Url] = Url(Provider.VULTR).uri("plans-metal")

URL_REGION: Final[Url] = Url(Provider.VULTR).uri("regions")
URL_REGION_ID_AVAILABLE: Final[Url] = Url(Provider.VULTR).uri("regions/{region-id}/availability")

URL_RESERVED_IP: Final[Url] = Url(Provider.VULTR).uri("reserved-ips")
URL_RESERVED_IP_ID: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/{reserved-ip}")
URL_RESERVED_IP_ATTACH: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/{reserved-ip}/attach")
URL_RESERVED_IP_DETACH: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/{reserved-ip}/detach")
URL_RESERVED_IP_CONVERT: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/convert")

URL_SNAPSHOT: Final[Url] = Url(Provider.VULTR).uri("snapshots")
URL_SNAPSHOT_ID: Final[Url] = Url(Provider.VULTR).uri("snapshots/{snapshot-id}")
URL_SNAPSHOT_CREATE_FROM_URL: Final[Url] = Url(Provider.VULTR).uri("snapshots/create-from-url")

URL_SSH_KEY_LIST: Final[Url] = Url(Provider.VULTR).uri("ssh-keys")
URL_SSH_KEY: Final[Url] = Url(Provider.VULTR).uri("ssh-keys/{ssh-key-id}")

URL_STARTUP_SCRIPT_LIST: Final[Url] = Url(Provider.VULTR).uri("startup-scripts")
URL_STARTUP_SCRIPT: Final[Url] = Url(Provider.VULTR).uri("startup-scripts/{startup-id}")

URL_SUB_ACCOUNT_LIST: Final[Url] = Url(Provider.VULTR).uri("subaccounts")
URL_SUB_ACCOUNT_CREATE: Final[Url] = Url(Provider.VULTR).uri("subaccounts")

URL_USER_LIST: Final[Url] = Url(Provider.VULTR).uri("users")
URL_USER: Final[Url] = Url(Provider.VULTR).uri("users/{user-id}")

URL_VPC_LIST: Final[Url] = Url(Provider.VULTR).uri("vpcs")
URL_VPC_GET: Final[Url] = Url(Provider.VULTR).uri("vpcs/{vpc-id}")

URL_VPC2_LIST: Final[Url] = Url(Provider.VULTR).uri("vpc2")
URL_VPC2_GET: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}")
URL_VPC2_NODES: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}/nodes")
URL_VPC2_ATTACH_NODES: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}/nodes/attach")
URL_VPC2_DETACH_NODES: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}/nodes/detach")

URL_VFS_REGIONS: Final[Url] = Url(Provider.VULTR).uri("vfs/regions")
URL_VFS_LIST: Final[Url] = Url(Provider.VULTR).uri("vfs")
URL_VFS_CREATE: Final[Url] = Url(Provider.VULTR).uri("vfs")
URL_VFS_GET: Final[Url] = Url(Provider.VULTR).uri("vfs/{vfs_id}")
URL_VFS_ATTACHMENTS: Final[Url] = Url(Provider.VULTR).uri("vfs/{vfs_id}/attachments")
URL_VFS_ATTACHMENT: Final[Url] = Url(Provider.VULTR).uri("vfs/{vfs_id}/attachments/{vps_id}")