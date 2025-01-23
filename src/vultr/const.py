from typing import Final

from proschedio.composer import Provider, Url

URL_ACCOUNT: Final[Url] = Url(Provider.VULTR).uri("account")
"""
### Request Methods

- `Get`: Get your Vultr account, permission, and billing information.
"""

URL_ACCOUNT_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("account/bandwidth")
"""
### Request Methods

- `Get`: Get your Vultr account bandwidth information.
"""

URL_APPLICATIONS: Final[Url] = Url(Provider.VULTR).uri("applications")
"""
### Request Methods

- `Get`: Get a list of all available Applications.

### Query parameters
- `Get`:
    - `type` - Filter the results by type.

| Type | Description |
| --- | --- |
| all | All available aplication types |
| marketplace | Marketplace applications |
| one-click | Vultr one-click applications |

    - `per_page` - Number of applications per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.
"""

URL_BACKUPS: Final[Url] = Url(Provider.VULTR).uri("backups")
"""
### Request Methods

- `Get`: Get information about Backups in your account.

### Query parameters
- `Get`:
    - `instance_id` - Filter the backups list by Instance id.
    - `per_page` - Number of items requested per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.
"""

URL_BACKUPS_ID: Final[Url] = Url(Provider.VULTR).uri("backups/{backup-id}")
"""
### Request Methods

- `Get`: Get the information for the Backup.

### Path parameters

- `backup_id` - The Backup id.
"""

URL_BARE_METAL: Final[Url] = Url(Provider.VULTR).uri("bare-metals")
"""
### Request Methods

- `GET`: List all Bare Metal instances in your account.
- `POST`: Create a new Bare Metal instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:
    - `os_id`
    - `snapshot_id`
    - `app_id`
    - `image_id`

Supply other attributes as desired.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and Max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.

### Request Body Schema
- `POST`:

```js
{
    "region": String, // The [Region id](#operation/list-regions) to create the instance.
    "plan": String, // The [Bare Metal plan id](#operation/list-metal-plans) to use for this instance.
    "script_id": Optional<String>, // The [Startup Script id](#operation/list-startup-scripts) to use for this instance.
    "enable_ipv6": Optional<Boolean>, // Enable IPv6. * true
    "sshkey_id": Optional<Array<Strings>>, // The [SSH Key id](#operation/list-ssh-keys) to install on this instance.
    "user_data": Optional<String>, // The user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for this Instance.
    "label": Optional<String>, // The user-supplied label.
    "activation_email": Optional<Boolean>, // Notify by email after deployment. * true * false (default)
    "hostname": Optional<String>, // The user-supplied hostname to use when deploying this instance.
    "reserved_ipv4": Optional<String>, // The [Reserved IP id](#operation/list-reserved-ips) for this instance.
    "os_id": Optional<Integer>, // If supplied, deploy the instance using this [Operating System id](#operation/list-os).
    "snapshot_id": Optional<String>, // If supplied, deploy the instance using this [Snapshot ID](#operation/list-snapshots).
    "app_id": Optional<Integer>, // If supplied, deploy the instance using this [Application id](#operation/list-applications).
    "image_id": Optional<String>, // If supplied, deploy the instance using this [Application image_id](#operation/list-applications).
    "persistent_pxe": Optional<Boolean>, // Enable persistent PXE. * true * false (default)
    "attach_vpc2": Optional<Array<Strings>>, // An array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance.
    "detach_vpc2": Optional<Array<Strings>>, // An array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance.
    "enable_vpc2": Optional<Boolean>, // If `true`, VPC 2.0 support will be added to the new server.
    "tags": Optional<Array<Strings>>, // Tags to apply to the instance.
    "user_scheme": Optional<String>, // Linux-only: The user scheme used for logging into this instance. * root * limited
    "mdisk_mode": Optional<String>, // The RAID configuration used for the disks on this instance. * raid1 * jbod * none (default)
    "app_variables": Optional<Object> // The [app variable inputs](#operation/list-marketplace-app-variables) for configuring the marketplace app (name/value pairs).
}
```
"""

URL_BARE_METAL_ID: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}")
"""
### Request Methods

- `GET`: Get information for a Bare Metal instance.
- `PATCH`: Update a Bare Metal instance. All attributes are optional. If not set, the attributes will retain their original values.
- `DELETE`: Delete a Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `PATCH`:
```js
{
    "user_data": String,
    "label": String,
    "os_id": Integer,
    "app_id": Integer,
    "enable_ipv6": Boolean,
    "attach_vpc2": Array<Strings>,
    "detach_vpc2": Array<Strings>,
    "enable_vpc2": Boolean,
    "tags": Array<Strings>,
    "user_scheme": String,
    "mdisk_mode": String
}
```
"""

URL_BARE_METAL_IPV4: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv4")
"""
### Request Methods

- `GET`: Get the IPv4 information for the Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_IPV6: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv6")
"""
### Request Methods

- `GET`: Get the IPv6 information for the Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_IPV4_REVERSE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv4/reverse")
"""
### Request Methods

- `POST`: Create a reverse IPv4 entry for a Bare Metal Instance. The `ip` and `reverse` attributes are required.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:
```js
{
    "ip": String, // The IPv4 address.
    "reverse": String // The IPv4 reverse entry.
}
```
"""
URL_BARE_METAL_IPV6_REVERSE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv6/reverse")
"""
### Request Methods

- `POST`: Create a reverse IPv6 entry for a Bare Metal Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:
```js
{
    "ip": String, // The IPv6 address in full, expanded format.
    "reverse": String // The IPv6 reverse entry.
}
```
"""
URL_BARE_METAL_IPV4_REVERSE_DEFAULT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv4/reverse/default")
"""
### Request Methods

- `POST`: Set a reverse DNS entry for an IPv4 address.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:
```js
{
    "ip": String // The IPv4 address.
}
```
"""

URL_BARE_METAL_IPV6_REVERSE_IPV6: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/ipv6/reverse/{ipv6}")
"""
### Request Methods

- `DELETE`: Delete the reverse IPv6 for a Bare metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.
- `ipv6` - The IPv6 address.
"""

URL_BARE_METAL_START: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/start")
"""
### Request Methods

- `POST`: Start the Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_REBOOT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/reboot")
"""
### Request Methods

- `POST`: Reboot the Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_REINSTALL: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/reinstall")
"""
### Request Methods

- `POST`: Reinstall the Bare Metal instance using an optional `hostname`.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema
- `POST`:
```js
{
    "hostname": String // The hostname to use when reinstalling this bare metal server.
}
```
"""

URL_BARE_METAL_HALT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/halt")
"""
### Request Methods

- `POST`: Halt the Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METAL_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/bandwidth")
"""
### Request Methods

- `GET`: Get bandwidth information for the Bare Metal instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

The `bandwidth` object in a successful response contains objects representing a day in the month. The date is denoted by the nested object keys. Days begin and end in the UTC timezone. Bandwidth utilization data contained within the date object is refreshed periodically. We do not recommend using this endpoint to gather real-time metrics.
"""

URL_BARE_METALS_HALT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/halt")
"""
### Request Methods

- `POST`: Halt Bare Metals.

### Request Body Schema

- `POST`:

```js
{
    "baremetal_ids": Array<String> // Array of Bare Metal instance ids to halt.
}
```
"""

URL_BARE_METALS_REBOOT: Final[Url] = Url(Provider.VULTR).uri("bare-metals/reboot")
"""
### Request Methods

- `POST`: Reboot Bare Metals.

### Request Body Schema

- `POST`:

```js
{
    "baremetal_ids": Array<String> // Array of Bare Metal instance ids to reboot.
}
```
"""

URL_BARE_METALS_START: Final[Url] = Url(Provider.VULTR).uri("bare-metals/start")
"""
### Request Methods

- `POST`: Start Bare Metals.

### Request Body Schema

- `POST`:

```js
{
    "baremetal_ids": Array<String> // Array of Bare Metal instance ids to start.
}
```
"""

URL_BARE_METALS_USER_DATA: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/user-data")
"""
### Request Methods

- `GET`: Get the user-supplied, base64 encoded [user data] for a Bare Metal.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METALS_GET_AVAILABLE_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/upgrades")
"""
### Request Methods

- `GET`: Get available upgrades for a Bare Metal.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Query parameters
- `type` - Filter upgrade by type:
    - all (applications, plans)
    - applications
    - os
"""

URL_BARE_METALS_GET_VNC: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vnc")
"""
### Request Methods

- `GET`: Get the VNC URL for a Bare Metal.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpcs/attach")
"""
### Request Methods

- `POST`: Attach a VPC Network to a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema

- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpcs) to attach.
}
```
"""

URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpcs/detach")
"""
### Request Methods

- `POST`: Detach a VPC Network from an Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema

- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpcs) to detach.
}
```
"""

URL_BARE_METALS_LIST_VPCS: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpcs")
"""
### Request Methods

- `GET`: List the VPC networks for a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.
"""

URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpc2/attach")
"""
### Request Methods

- `POST`: Attach a VPC 2.0 Network to a Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema

- `POST`:

```js
{
    "vpc_id": String, // The [VPC ID](#operation/list-vpc2) to attach.
    "ip_address": String // The IP address to use for this instance on the attached VPC 2.0 network.
}
```
"""

URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpc2/detach")
"""
### Request Methods

- `POST`: Detach a VPC 2.0 Network from an Bare Metal Instance.

### Path parameters
- `baremetal-id` - The Bare Metal instance id.

### Request Body Schema

- `POST`:

```js
{
    "vpc_id": String // The [VPC ID](#operation/list-vpc2) to detach.
}
```
"""

URL_BARE_METALS_LIST_VPCS2: Final[Url] = Url(Provider.VULTR).uri("bare-metals/{baremetal-id}/vpc2")
"""
### Request Methods

- `GET`: List the VPC 2.0 networks for a Bare Metal Instance.

### Path parameters

- `baremetal-id` - The Bare Metal instance id.

"""

URL_BILLING_LIST_HISTORY: Final[Url] = Url(Provider.VULTR).uri("billing/history")
"""
### Request Methods
- `Get`: Retrieve billing history entries.

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100, maximum is 500.
- `cursor`: Cursor for pagination.
"""

URL_BILLING_LIST_INVOICES: Final[Url] = Url(Provider.VULTR).uri("billing/invoices")
"""
### Request Methods
- `Get`: Retrieve a list of all invoices on the account.

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100, maximum is 500.
- `cursor`: Cursor for pagination.
"""

URL_BILLING_GET_INVOICE: Final[Url] = Url(Provider.VULTR).uri("billing/invoices/{invoice-id}")
"""
### Request Methods
- `Get`: Retrieve a specific invoice by ID.

### Path Parameters
- `invoice-id`: The ID of the invoice to retrieve.
"""

URL_BILLING_GET_INVOICE_ITEMS: Final[Url] = Url(Provider.VULTR).uri("billing/invoices/{invoice-id}/items")
"""
### Request Methods
- `Get`: Retrieve line items for a specific invoice.

### Path Parameters
- `invoice-id`: The ID of the invoice.

### Query Parameters
- `per_page`: Number of items requested per page. Default is 100, maximum is 500.
- `cursor`: Cursor for pagination.
"""

URL_BILLING_LIST_PENDING_CHARGES: Final[Url] = Url(Provider.VULTR).uri("billing/pending-charges")
"""
### Request Methods
- `Get`: Retrieve all pending charges for the account.
"""

URL_BLOCK_STORAGE: Final[Url] = Url(Provider.VULTR).uri("blocks")
"""
### Request Methods

- `GET`: List all Block Storage in your account.
- `POST`: Create new Block Storage in a `region` with a size of `size_gb`.

### Query parameters
- `GET`:
    - `per_page` - Number of items requested per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.

### Request Body Schema
- `POST`:

```js
{
    "region": String, // The [Region id](#operation/list-regions) where the Block Storage will be created.
    "size_gb": Integer, // Size in GB may range between 10 and 40000, depending on the block_type.
    "label": Optional<String>, // The user-supplied label.
    "block_type": Optional<String> // An optional parameter, that determines the type of block storage volume.
    // high_perf from 10GB to 10,000GB
    // storage_opt from 40GB to 40,000GB
}
```
"""

URL_BLOCK_STORAGE_ID: Final[Url] = Url(Provider.VULTR).uri("blocks/{block-id}")
"""
### Request Methods

- `GET`: Get information for Block Storage.
- `PATCH`: Update information for Block Storage.
- `DELETE`: Delete Block Storage.

### Path parameters
- `block-id` - The Block Storage id.

### Request Body Schema
- `PATCH`:

```js
{
    "label": Optional<String>, // The user-supplied label.
    "size_gb": Optional<Integer> // The new size of the block storage volume in GB. Must be >= current size.
}
```
"""

URL_BLOCK_STORAGE_ATTACH: Final[Url] = Url(Provider.VULTR).uri("blocks/{block-id}/attach")
"""
### Request Methods

- `POST`: Attach Block Storage to Instance.

### Path parameters
- `block-id` - The Block Storage id.

### Request Body Schema
- `POST`:

```js
{
    "instance_id": String, // The [Instance id](#operation/list-instances) to attach.
    "live": Optional<Boolean> // Attach without restarting the Instance.
    // true: Attach live
    // false: Restart and attach (default)
}
```
"""

URL_BLOCK_STORAGE_DETACH: Final[Url] = Url(Provider.VULTR).uri("blocks/{block-id}/detach")
"""
### Request Methods

- `POST`: Detach Block Storage.

### Path parameters
- `block-id` - The Block Storage id.

### Request Body Schema
- `POST`:

```js
{
    "live": Optional<Boolean> // Detach without restarting the Instance.
}
```

|Value|Description|
|----|----|
|true|Detach live, do not restart the instance.|
|false|Restart the instance and detach the Block Storage.|

### Notes
- Block Storage must be in `active` state.
- Re-attaching a Block Storage volume is allowed after 3 minutes.
"""

URL_CDN_LIST_PULL_ZONES: Final[Url] = Url(Provider.VULTR).uri("cdns/pull-zones")
"""
### Request Methods

- `Get`: List CDN Pull Zones.
- `Post`: Create a new CDN Pull Zone.

### Request Body Schema
- `Post`:

```js
{
    "label": String, // The user-supplied label.
    "origin_scheme": String, // The URI scheme of the origin domain. Enum: ["http", "https"]
    "origin_domain": String, // The domain name from which the content stored in the CDN will be pulled.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain and origin_scheme=https)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain and origin_scheme=https)
    "cors": Optional<Boolean>, // Enable Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Enable Gzip compression
    "block_ai": Optional<Boolean>, // Block AI bots
    "block_bad_bots": Optional<Boolean> // Block potentially malicious bots
}
// Required: label, origin_scheme, origin_domain
```
"""

URL_CDN_GET_PULL_ZONE: Final[Url] = Url(Provider.VULTR).uri("cdns/pull-zones/{pullzone-id}")
"""
### Request Methods

- `Get`: Get information about a CDN Pull Zones.
- `Put`: Update information for a CDN Pullzone. All attributes are optional. If not set, the attributes will retain their original values.
- `Delete`: Delete a CDN Pull Zone.

### Request Body Schema
- `Put`:

```js
{
    "label": Optional<String>, // The user-supplied label.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain and origin_scheme=https)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain and origin_scheme=https)
    "cors": Optional<Boolean>, // Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Optional feature to compress files
    "block_ai": Optional<Boolean>, // Optional feature to block AI bots
    "block_bad_bots": Optional<Boolean>, // Optional feature to block malicious bots
    "regions": Optional<Array> // List of [Region ids](#operation/list-regions) for content delivery
}
```
"""

URL_CDN_PURGE_PULL_ZONE: Final[Url] = Url(Provider.VULTR).uri("cdns/pull-zones/{pullzone-id}/purge")
"""
### Request Methods

- `Get`: Clears cached content on server proxies so that visitors can get the latest page versions.

**Note:** This action may only be performed once every six hours.  
**Note:** This action may take a few extra seconds to complete.
"""

URL_CDN_LIST_PUSH_ZONES: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones")
"""
### Request Methods

- `Get`: List CDN Push Zones.
- `Post`: Create a new CDN Push Zone.

### Request Body Schema
- `Post`:

```js
{
    "label": String, // The user-supplied label.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain)
    "cors": Optional<Boolean>, // Enable Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Enable Gzip compression
    "block_ai": Optional<Boolean>, // Block AI bots
    "block_bad_bots": Optional<Boolean> // Block potentially malicious bots
}
```
"""

URL_CDN_GET_PUSH_ZONE: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones/{pushzone-id}")
"""
### Request Methods

- `Get`: Get information about a CDN Push Zone.
- `Put`: Update information for a CDN Pushzone. All attributes are optional. If not set, the attributes will retain their original values.
- `Delete`: Delete a CDN Push Zone.

### Request Body Schema
- `Put`:

```js
{
    "label": Optional<String>, // The user-supplied label.
    "vanity_domain": Optional<String>, // An optional domain name that can be used to access the cached files.
    "ssl_cert": Optional<String>, // Base 64 encoded SSL certificate (required if vanity_domain)
    "ssl_cert_key": Optional<String>, // Base 64 encoded SSL private key (required if vanity_domain)
    "cors": Optional<Boolean>, // Cross-origin resource sharing
    "gzip": Optional<Boolean>, // Optional feature to compress files
    "block_ai": Optional<Boolean>, // Optional feature to block AI bots
    "block_bad_bots": Optional<Boolean>, // Optional feature to block malicious bots
    "regions": Optional<Array> // List of [Region ids](#operation/list-regions) for content delivery
}
```
"""

URL_CDN_LIST_PUSH_ZONE_FILES: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones/{pushzone-id}/files")
"""
### Request Methods

- `Get`: Get a list of files that have been uploaded to a specific CDN Push Zones.
- `Post`: Create a presigned post endpoint that can be used to upload a file to your Push Zone.

### Request Body Schema
- `Post`:

```js
{
    "name": String, // The name of the file including extension.
    "size": Integer // The size of the file in bytes.
}
```
"""

URL_CDN_DELETE_PUSH_ZONE_FILE: Final[Url] = Url(Provider.VULTR).uri("cdns/push-zones/{pushzone-id}/files/{file-name}")
"""
### Request Methods

- `Get`: Get information about a CDN Push Zone file.
- `Delete`: Delete a CDN Push Zone file.

### Path Parameters
- `pushzone-id`: The [Push Zone ID](#operation/list-pushzones)
- `file-name`: The [File Name](#operation/list-pushzone-files)
"""

URL_CONTAINER_LIST: Final[Url] = Url(Provider.VULTR).uri("registries")
"""
### Request Methods

- `Get`: List All Container Registry Subscriptions for this account

### Query parameters
- `Get`:
    - `per_page` - Number of items requested per page. Default is 100 and max is 500.
    - `cursor` - Cursor for paging. See Meta and pagination.
"""

URL_CONTAINER: Final[Url] = Url(Provider.VULTR).uri("registry")
"""
### Request Methods
- `Post`: Create a new Container Registry Subscription

### Request Body Schema
- `Post`:

```js
{
    "name": "The globally unique name to reference this registry",
    "public": "If true, this is a publically accessible registry allowing anyone to pull from it. If false, this registry is completely private",
    "region": "The name of the region you'd like to deploy this Registry in. Can get list of regions from /registry/region/list endpoint i.e. sjc",
    "plan": "The key of the plan you'd like to select which dictates how much storage you're allocated and the monthly cost. Can get list of plans from /plan/list endpoint i.e. start_up"
}
```
"""

URL_CONTAINER_ID: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}")
"""
### Request Methods
- `Get`: Get a single Container Registry Subscription
- `Put`: Update a Container Registry Subscription
- `Delete`: Delete a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID

### Request Body Schema
- `Put`:

```js
{
    "public": "If true, this is a publically accessible registry allowing anyone to pull from it. If false, this registry is completely private",
    "plan": "The key of the plan you'd like to upgrade to which dictates how much storage you're allocated and the monthly cost. Can get list of plans from /plan/list endpoint i.e. business"
}
```
"""

URL_CONTAINER_REPOSITORY: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repositories")
"""
### Request Methods
- `Get`: List All Repositories in a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
"""

URL_CONTAINER_REPOSITORY_IMAGE: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repository/{repository-image}")
"""
### Request Methods
- `Get`: Get a single Repository in a Container Registry Subscription
- `Put`: Update a Repository in a Container Registry Subscription
- `Delete`: Delete a Repository from a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
- `repository-image`: Target repository name

### Request Body Schema
- `Put`:

```js
{
    "description": "This is my super cool hello-world project"
}
```
"""

URL_CONTAINER_DOCKER_CREDENTIALS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/docker-credentials")
"""
### Request Methods
- `Options`: Create a fresh set of Docker Credentials for this Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID

### Query parameters
- `expiry_seconds`: "The duration in seconds for which the credentials are valid (default: 0)"
- `read_write`: "If false, credentials will be read-only (default: false)"
"""

URL_CONTAINER_KUBERNETES_DOCKER_CREDENTIALS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/docker-credentials/kubernetes")
"""
### Request Methods
- `Options`: Create a fresh set of Docker Credentials for this Container Registry Subscription and return them in a Kubernetes friendly YAML format

### Path parameters
- `registry-id`: The Container Registry Subscription ID

### Query parameters
- `expiry_seconds`: "The duration in seconds for which the credentials are valid (default: 0)"
- `read_write`: "If false, credentials will be read-only (default: false)"
- `base64_encode`: "If true, encodes the output in base64 (default: false)"
"""

URL_CONTAINER_ROBOTS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/robots")
"""
### Request Methods
- `Get`: List All Robots in a Conainer Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
"""

URL_CONTAINER_ROBOT: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/robot/{robot-name}")
"""
### Request Methods
- `Get`: Get a single Robot in a Container Registry Subscription
- `Put`: Update the description, disable, duration, and add or remove access, in a Container Registry Subscription Robot
- `Delete`: Deletes a Robot from a Container Registry Subscription

### Path parameters
- `registry-id`: The Container Registry Subscription ID
- `robot-name`: The Robot name

### Request Body Schema
- `Put`:

```js
{
    "description": "Robot user auto generated by Vultr - enter only what you want to update in the request body",
    "disable": true,
    "duration": -1,
    "access": [
        {
            "action": "pull",
            "resource": "repository",
            "effect": "allow"
        },
        {
            "action": "delete",
            "resource": "artifact",
            "effect": "deny"
        }
    ]
}
```
"""

URL_CONTAINER_ARTIFACTS: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repository/{repository-image}/artifacts")
"""
### Request Methods
- `Get`: List All Artifacts in a Container Registry Repository

### Path parameters
- `registry-id`: The Container Registry Subscription ID
- `repository-image`: The Repository Name
"""

URL_CONTAINER_ARTIFACT: Final[Url] = Url(Provider.VULTR).uri("registry/{registry-id}/repository/{repository-image}/artifact/{artifact-digest}")
"""
### Request Methods
- `Get`: Get a single Artifact in a Container Registry Repository
- `Delete`: Deletes an Artifact from a Container Registry Repository

### Path Parameters
- `registry-id`: The Container Registry Subscription ID
- `repository-image`: The Repository Name
- `artifact-digest`: The Artifact Digest
"""

URL_CONTAINER_LIST_REGIONS: Final[Url] = Url(Provider.VULTR).uri("registry/region/list")
"""
### Request Methods
- `Get`: List All Regions where a Container Registry can be deployed
"""

URL_DATABASE_LIST_PLANS: Final[Url] = Url(Provider.VULTR).uri("databases/plans")
"""
### Request Methods

- `Get`: List Managed Database Plans.

### Query parameters
- `Get`:
    - `engine` - Filter by engine type\n\n* `mysql`\n* `pg`\n* `valkey`\n* `kafka`
    - `nodes` - Filter by number of nodes.
    - `region` - Filter by [Region id](#operation/list-regions).
"""

URL_DATABASE_LIST: Final[Url] = Url(Provider.VULTR).uri("databases")
"""
### Request Methods

- `Get`: List all Managed Databases in your account.
- `Post`: Create a new Managed Database in a `region` with the desired `plan`. Supply optional attributes as desired.

### Query parameters
- `Get`:
    - `label` - Filter by label.
    - `tag` - Filter by specific tag.
    - `region` - Filter by [Region id](#operation/list-regions).

### Request Body Schema
- `Post`:
{
    "database_engine": String, // The database engine type for the Managed Database. * `mysql` * `pg` * `valkey` * `kafka`
    "database_engine_version": String, // The version of the chosen database engine type for the Managed Database. * MySQL: `8` * PostgreSQL: `13` - `16` * Valkey: `7` * Kafka: `3.7`
    "region": String, // The [Region id](#operation/list-regions) where the Managed Database is located.
    "plan": String, // The [Plan id](#operation/list-database-plans) to use when deploying this Managed Database.
    "label": String, // A user-supplied label for this Managed Database.
    "tag": Optional<String>, // The user-supplied tag for this Managed Database.
    "vpc_id": Optional<String>, // The [VPC id](#operation/list-vpcs) to use when deploying this Managed Database.
    "maintenance_dow": Optional<String>, // The day of week for routine maintenance updates. * `monday` * `tuesday` * `wednesday` * `thursday` * `friday` * `saturday` * `sunday`
    "maintenance_time": Optional<String>, // The preferred time (UTC) for routine maintenance updates in 24-hour HH:00 format
    "trusted_ips": Optional<Array<String>>, // A list of IP addresses allowed to access the Managed Database in CIDR notation
    "mysql_sql_modes": Optional<Array<String>>, // A list of SQL modes to enable (MySQL engine types only)
    "mysql_require_primary_key": Optional<Boolean>, // Require a primary key for all tables (MySQL engine types only)
    "mysql_slow_query_log": Optional<Boolean>, // Enable slow query logging (MySQL engine types only)
    "mysql_long_query_time": Optional<Integer>, // Number of seconds to denote a slow query (MySQL engine types only)
    "eviction_policy": Optional<String> // Set the data eviction policy (Valkey engine types only)
}
"""

URL_DATABASE_GET: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}")
"""
### Request Methods

- `Get`: Get information about a Managed Database.
- `Put`: Update information for a Managed Database. All attributes are optional. If not set, the attributes will retain their original values.
- `Delete`: Delete a Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Put`:
{
    "region": Optional<String>, // The [Region id](#operation/list-regions) where the Managed Database is located.
    "plan": Optional<String>, // The [Plan id](#operation/list-database-plans) for this Managed Database.
    "label": Optional<String>, // A user-supplied label for this Managed Database.
    "tag": Optional<String>, // The user-supplied tag for this Managed Database.
    "vpc_id": Optional<String>, // The [VPC id](#operation/list-vpcs) for this Managed Database.
    "maintenance_dow": Optional<String>, // The day of week for routine maintenance updates
    "maintenance_time": Optional<String>, // The preferred time (UTC) for routine maintenance updates
    "cluster_time_zone": Optional<String>, // The configured time zone in TZ database format
    "trusted_ips": Optional<Array<String>>, // A list of IP addresses allowed to access the Managed Database
    "mysql_sql_modes": Optional<Array<String>>, // A list of SQL modes to enable (MySQL engine types only)
    "mysql_require_primary_key": Optional<Boolean>, // Require a primary key for all tables (MySQL engine types only)
    "mysql_slow_query_log": Optional<Boolean>, // Enable slow query logging (MySQL engine types only)
    "mysql_long_query_time": Optional<Integer>, // Number of seconds to denote a slow query (MySQL engine types only)
    "eviction_policy": Optional<String> // Set the data eviction policy (Valkey engine types only)
}
"""

URL_DATABASE_USAGE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/usage")
"""
### Request Methods

- `Get`: Get disk, memory, and vCPU usage information for a Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_USERS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/users")
"""
### Request Methods

- `Get`: List all database users within the Managed Database.
- `Post`: Create a new database user within the Managed Database. Supply optional attributes as desired.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
{
    "username": String, // The username of the database user
    "password": Optional<String>, // The password for the database user (omit to auto-generate)
    "encryption": Optional<String>, // The password encryption type (MySQL engine types only) * `caching_sha2_password` * `mysql_native_password`
    "permission": Optional<String> // The permission level (Kafka engine types only) * `admin` * `read` * `write` * `readwrite`
}
"""

URL_DATABASE_USER: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/users/{username}")
"""
### Request Methods

- `Get`: Get information about a Managed Database user.
- `Put`: Update database user information within a Managed Database.
- `Delete`: Delete a database user within a Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `username` - The [database user](#operation/list-database-users).

### Request Body Schema
- `Put`:
{
    "password": String // The password for the database user (can be empty to auto-generate)
}
"""

URL_DATABASE_USER_ACCESS_CONTROL: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/users/{username}/access-control")
"""
### Request Methods

- `Put`: Configure access control settings for a Managed Database user (Valkey and Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `username` - The [database user](#operation/list-database-users).

### Request Body Schema
- `Put`:
{
    "acl_categories": Optional<Array<String>>, // ACL categories array (Valkey)
    "acl_channels": Optional<Array<String>>, // ACL channels array (Valkey)
    "acl_commands": Optional<Array<String>>, // ACL commands array (Valkey)
    "acl_keys": Optional<Array<String>> // ACL keys array (Valkey)
}
OR
{
    "permission": Optional<String> // Kafka permissions * `admin` * `read` * `write` * `readwrite`
}
"""

URL_DATABASE_LOGICAL_DATABASES: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/dbs")
"""
### Request Methods

- `Get`: List all logical databases within the Managed Database (MySQL and PostgreSQL only).
- `Post`: Create a new logical database within the Managed Database (MySQL and PostgreSQL only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
{
    "name": String // The name of the logical database
}
"""

URL_DATABASE_LOGICAL_DATABASE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/dbs/{db-name}")
"""
### Request Methods

- `Get`: Get information about a logical database within a Managed Database (MySQL and PostgreSQL only).
- `Delete`: Delete a logical database within a Managed Database (MySQL and PostgreSQL only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `db-name` - The [logical database name](#operation/list-database-dbs).
"""

URL_DATABASE_TOPICS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/topics")
"""
### Request Methods

- `Get`: List all topics within the Managed Database (Kafka engine types only).
- `Post`: Create a new topic within the Managed Database (Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
{
    "name": String, // The name for the database topic
    "partitions": Integer, // The number of partitions
    "replication": Integer, // The replication factor
    "retention_hours": Integer, // The retention hours
    "retention_bytes": Integer // The retention bytes
}
"""

URL_DATABASE_TOPIC: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/topics/{topic-name}")
"""
### Request Methods

- `Get`: Get information about a Managed Database topic (Kafka engine types only).
- `Put`: Update topic information within a Managed Database (Kafka engine types only).
- `Delete`: Delete a topic within a Managed Database (Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `topic-name` - The [database topic](#operation/list-database-topics).

### Request Body Schema
- `Put`:
{
    "partitions": "The number of partitions for the database topic.",
    "replication": "The replication factor for the database topic.",
    "retention_hours": "The retention hours for the database topic.",
    "retention_bytes": "The retention bytes for the database topic."
}
"""

URL_DATABASE_QUOTAS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/quotas")
"""
### Request Methods

- `Get`: List all quotas within the Managed Database (Kafka engine types only).
- `Post`: Create a new quota within the Managed Database (Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
{
    "client_id": "The client ID for the database quota. Note: Creating a new quota with the same client ID and user will overwrite the previous record.",
    "consumer_byte_rate": "The consumer byte rate for the database quota.",
    "producer_byte_rate": "The producer byte rate for the database quota.",
    "request_percentage": "The CPU request percentage for the database quota.",
    "user": "The [user](#operation/list-database-users) for the database quota."
}
"""

URL_DATABASE_MAINTENANCE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/maintenance")
"""
### Request Methods

- `Get`: List all available version upgrades within the Managed Database.
- `Post`: Start maintenance updates for the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_MIGRATION: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/migration")
"""
### Request Methods

- `Get`: View the status of a migration attached to the Managed Database.
- `Post`: Start a migration to the Managed Database.
- `Delete`: Detach a migration from the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
{
    "host": "The host name of the source server.",
    "port": "The connection port of the source server.",
    "username": "The username of the source server. Uses `default` for Valkey if left empty or unset.",
    "password": "The password of the source server.",
    "database": "The database of the source server. Required for MySQL/PostgreSQL engine types, but excluded for Valkey.",
    "ignored_databases": "Comma-separated list of ignored databases on the source server. Excluded for Valkey engine types.",
    "ssl": "The true/false value for whether SSL is needed to connect to the source server."
}
"""

URL_DATABASE_READ_REPLICA: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/read-replica")
"""
### Request Methods

- `Post`: Create a read-only replica node for the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
{
    "region": "The [Region id](#operation/list-regions) where the Managed Database is located.",
    "label": "A user-supplied label for this Managed Database."
}
"""

URL_DATABASE_PROMOTE_READ_REPLICA: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/promote-read-replica")
"""
### Request Methods

- `Post`: Promote a read-only replica node to its own primary Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_BACKUPS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/backups")
"""
### Request Methods

- `Get`: Get backup information for the Managed Database.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_RESTORE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/restore")
"""
### Request Methods

- `Post`: Create a new Managed Database from a backup.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
```js
{
    "label": String, // A user-supplied label for this Managed Database.
    "type": String, // The type of backup restoration to use for this Managed Database.
    "date": String, // The [backup date](#operation/get-backup-information) to use when restoring the Managed Database in YYYY-MM-DD date format.
    "time": String // The [backup time](#operation/get-backup-information) to use when restoring the Managed Database in HH-MM-SS time format (24-hour UTC).
}
```
"""

URL_DATABASE_FORK: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/fork")
"""
### Request Methods

- `Post`: Fork a Managed Database to a new subscription from a backup.

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
```js
{
    "label": String, // A user-supplied label for this Managed Database.
    "region": String, // The [Region id](#operation/list-regions) where the Managed Database is located.
    "plan": String, // The [Plan id](#operation/list-database-plans) to use when deploying this Managed Database.
    "vpc_id": String, // The [VPC id](#operation/list-vpcs) to use when deploying this Managed Database.
    "type": String, // The type of backup restoration to use for this Managed Database.
    "date": String, // The [backup date](#operation/get-backup-information) to use when restoring the Managed Database in YYYY-MM-DD date format.
    "time": String // The [backup time](#operation/get-backup-information) to use when restoring the Managed Database in HH-MM-SS time format (24-hour UTC).
}
```
"""

URL_DATABASE_CONNECTION_POOLS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/connection-pools")
"""
### Request Methods

- `Get`: List all connection pools within the Managed Database (PostgreSQL engine types only).
- `Post`: Create a new connection pool within the Managed Database (PostgreSQL engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
```js
{
    "name": String, // The name of the connection pool.
    "database": String, // The logical database associated with the connection pool.
    "username": String, // The database user associated with the connection pool.
    "mode": String, // The mode for the connection pool.
    "size": Integer // The size of the connection pool.
}
```
"""

URL_DATABASE_CONNECTION_POOL: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/connection-pools/{pool-name}")
"""
### Request Methods

- `Get`: Get information about a Managed Database connection pool (PostgreSQL engine types only).
- `Put`: Update connection-pool information within a Managed Database (PostgreSQL engine types only).
- `Delete`: Delete a connection pool within a Managed Database (PostgreSQL engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
- `pool-name` - The [connection pool name](#operation/list-connection-pools).

### Request Body Schema
- `Put`:
```js
{
    "database": String, // The logical database associated with the connection pool.
    "username": String, // The database user associated with the connection pool.
    "mode": String, // The mode for the connection pool.
    "size": Integer // The size of the connection pool.
}
```
"""

URL_DATABASE_ADVANCED_OPTIONS: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/advanced-options")
"""
### Request Methods

- `Get`: List all configured and available advanced options for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).
- `Put`: Updates an advanced configuration option for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).
"""

URL_DATABASE_VERSION_UPGRADE: Final[Url] = Url(Provider.VULTR).uri("databases/{database-id}/version-upgrade")
"""
### Request Methods

- `Get`: List all available version upgrades within the Managed Database (PostgreSQL engine types only).
- `Post`: Start a version upgrade for the Managed Database (PostgreSQL engine types only).

### Path parameters
- `database-id` - The [Managed Database ID](#operation/list-databases).

### Request Body Schema
- `Post`:
```js
{
    "version": String // The version number to upgrade the Managed Database to.
}
```
"""

URL_DOMAIN_LIST: Final[Url] = Url(Provider.VULTR).uri("domains")
"""
### Request Methods

- `Get`: List all DNS Domains in your account.
- `Post`: Create a DNS Domain for `domain`. If no `ip` address is supplied a domain with no records will be created.
"""

URL_DOMAIN: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}")
"""
### Request Methods

- `Get`: Get information for the DNS Domain.
- `Put`: Update the DNS Domain.
- `Delete`: Delete the DNS Domain.
"""

URL_DOMAIN_SOA: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/soa")
"""
### Request Methods

- `Get`: Get SOA information for the DNS Domain.
- `Patch`: Update the SOA information for the DNS Domain. All attributes are optional. If not set, the attributes will retain their original values.
"""

URL_DOMAIN_DNSSEC: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/dnssec")
"""
### Request Methods

- `Get`: Get the DNSSEC information for the DNS Domain.
"""

URL_DOMAIN_RECORDS: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/records")
"""
### Request Methods

- `Get`: Get the DNS records for the Domain.
- `Post`: Create a DNS record.
"""

URL_DOMAIN_RECORD: Final[Url] = Url(Provider.VULTR).uri("domains/{dns-domain}/records/{record-id}")
"""
### Request Methods

- `Get`: Get information for a DNS Record.
- `Patch`: Update the information for a DNS record. All attributes are optional. If not set, the attributes will retain their original values.
- `Delete`: Delete the DNS record.
"""

URL_FIREWALL_GROUP_LIST: Final[Url] = Url(Provider.VULTR).uri("firewalls")
"""
### Request Methods

- `Get`: Get a list of all Firewall Groups.
- `Post`: Create a new Firewall Group.
"""

URL_FIREWALL_GROUP_GET: Final[Url] = Url(Provider.VULTR).uri("firewalls/{firewall-group-id}")
"""
### Request Methods

- `Get`: Get information for a Firewall Group.
- `Put`: Update information for a Firewall Group.
- `Delete`: Delete a Firewall Group.
"""

URL_FIREWALL_GROUP_RULES: Final[Url] = Url(Provider.VULTR).uri("firewalls/{firewall-group-id}/rules")
"""
### Request Methods

- `Get`: Get the Firewall Rules for a Firewall Group.
- `Post`: Create a Firewall Rule for a Firewall Group. The attributes `ip_type`, `protocol`, `subnet`, and `subnet_size` are required.
"""

URL_FIREWALL_GROUP_RULE: Final[Url] = Url(Provider.VULTR).uri("firewalls/{firewall-group-id}/rules/{firewall-rule-id}")
"""
### Request Methods

- `Get`: Get a Firewall Rule.
- `Delete`: Delete a Firewall Rule.
"""

URL_INFERENCE_LIST: Final[Url] = Url(Provider.VULTR).uri("inference")
"""
### Request Methods

- `Get`: List all Serverless Inference subscriptions in your account.
- `Post`: Create a new Serverless Inference subscription.
"""

URL_INFERENCE_GET: Final[Url] = Url(Provider.VULTR).uri("inference/{inference-id}")
"""
### Request Methods

- `Get`: Get information about a Serverless Inference subscription.
- `Patch`: Update information for a Serverless Inference subscription.
- `Delete`: Delete a Serverless Inference subscription.
"""

URL_INFERENCE_USAGE: Final[Url] = Url(Provider.VULTR).uri("inference/{inference-id}/usage")
"""
### Request Methods

- `Get`: Get usage information for a Serverless Inference subscription.
"""

URL_INSTANCE_LIST: Final[Url] = Url(Provider.VULTR).uri("instances")
"""
### Request Methods

- `Get`: List all VPS instances in your account.
"""

URL_INSTANCE_CREATE: Final[Url] = Url(Provider.VULTR).uri("instances")
"""
### Request Methods

- `Post`: Create a new VPS Instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:

* `os_id`
* `iso_id`
* `snapshot_id`
* `app_id`
* `image_id`

Supply other attributes as desired.
"""

URL_INSTANCE_GET: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}")
"""
### Request Methods

- `Get`: Get information about an Instance.
- `Patch`: Update information for an Instance. All attributes are optional. If not set, the attributes will retain their original values.
**Note:** Changing `os_id`, `app_id` or `image_id` may take a few extra seconds to complete.
- `Delete`: Delete an Instance.
"""

URL_INSTANCE_REINSTALL: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/reinstall")
"""
### Request Methods

- `Post`: Reinstall an Instance using an optional `hostname`.

**Note:** This action may take a few extra seconds to complete.
"""

URL_INSTANCE_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/bandwidth")
"""
### Request Methods

- `Get`: Get bandwidth information about an Instance.

The `bandwidth` object in a successful response contains objects representing a day in the month. The date is denoted by the nested object keys. Days begin and end in the UTC timezone. The bandwidth utilization data contained within the date object is refreshed periodically. We do not recommend using this endpoint to gather real-time metrics.
"""

URL_INSTANCE_NEIGHBORS: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/neighbors")
"""
### Request Methods

- `Get`: Get a list of other instances in the same location as this Instance.
"""

URL_INSTANCE_PRIVATE_NETWORKS: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/private-networks")
"""
### Request Methods

- `Get`: **Deprecated**: use [List Instance VPCs](#operation/list-instance-vpcs) instead.<br><br>List the private networks for an Instance.
"""


URL_INSTANCE_VPCS: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpcs")
"""
### Request Methods

- `Get`: List the VPCs for an Instance.
"""

URL_INSTANCE_VPC2S: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpc2")
"""
### Request Methods

- `Get`: List the VPC 2.0 networks for an Instance.
"""

URL_INSTANCE_ISO: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/iso")
"""
### Request Methods

- `Get`: Get the ISO status for an Instance.
"""

URL_INSTANCE_ISO_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/iso/attach")
"""
### Request Methods

- `Post`: Attach an ISO to an Instance.
"""

URL_INSTANCE_ISO_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/iso/detach")
"""
### Request Methods

- `Post`: Detach the ISO from an Instance.
"""

URL_INSTANCE_PRIVATE_NETWORKS_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/private-networks/attach")
"""
### Request Methods

- `Post`: Attach Private Network to an Instance.<br><br>**Deprecated**: use [Attach VPC to Instance](#operation/attach-instance-vpc) instead.
"""

URL_INSTANCE_PRIVATE_NETWORKS_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/private-networks/detach")
"""
### Request Methods

- `Post`: Detach Private Network from an Instance.<br><br>**Deprecated**: use [Detach VPC from Instance](#operation/detach-instance-vpc) instead.
"""

URL_INSTANCE_VPCS_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpcs/attach")
"""
### Request Methods

- `Post`: Attach a VPC to an Instance.
"""

URL_INSTANCE_VPCS_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpcs/detach")
"""
### Request Methods

- `Post`: Detach a VPC from an Instance.
"""

URL_INSTANCE_VPC2_ATTACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpc2/attach")
"""
### Request Methods

- `Post`: Attach a VPC 2.0 Network to an Instance.
"""

URL_INSTANCE_VPC2_DETACH: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/vpc2/detach")
"""
### Request Methods

- `Post`: Detach a VPC 2.0 Network from an Instance.
"""
URL_INSTANCE_IPV4: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv4")
"""
### Request Methods

- `Get`: List the IPv4 information for an Instance.
- `Post`: Create an IPv4 address for an Instance.
"""

URL_INSTANCE_IPV6: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv6")
"""
### Request Methods

- `Get`: Get the IPv6 information for an VPS Instance.
"""

URL_INSTANCE_IPV4_REVERSE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv4/reverse")
"""
### Request Methods

- `Post`: Create a reverse IPv4 entry for an Instance. The `ip` and `reverse` attributes are required.
"""

URL_INSTANCE_IPV6_REVERSE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv6/reverse")
"""
### Request Methods

- `Get`: List the reverse IPv6 information for an Instance.
- `Post`: Create a reverse IPv6 entry for an Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format.
"""

URL_INSTANCE_IPV4_REVERSE_DEFAULT: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv4/reverse/default")
"""
### Request Methods

- `Post`: Set a reverse DNS entry for an IPv4 address.
"""

URL_INSTANCE_IPV6_REVERSE_IPV6: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/ipv6/reverse/{ipv6}")
"""
### Request Methods

- `Delete`: Delete the reverse IPv6 for an Instance.
"""

URL_INSTANCE_START: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/start")
"""
### Request Methods

- `Post`: Start an Instance.
"""

URL_INSTANCE_REBOOT: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/reboot")
"""
### Request Methods

- `Post`: Reboot an Instance.
"""

URL_INSTANCE_HALT: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/halt")
"""
### Request Methods

- `Post`: Halt an Instance.
"""

URL_INSTANCE_USER_DATA: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/user-data")
"""
### Request Methods

- `Get`: Get the user-supplied, base64 encoded user data for an Instance.
"""

URL_INSTANCES_HALT: Final[Url] = Url(Provider.VULTR).uri("instances/halt")
"""
### Request Methods

- `Post`: Halt Instances.
"""

URL_INSTANCES_REBOOT: Final[Url] = Url(Provider.VULTR).uri("instances/reboot")
"""
### Request Methods

- `Post`: Reboot Instances.
"""

URL_INSTANCES_START: Final[Url] = Url(Provider.VULTR).uri("instances/start")
"""
### Request Methods

- `Post`: Start Instances.
"""

URL_INSTANCE_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/upgrades")
"""
### Request Methods

- `Get`: Get available upgrades for an Instance.
"""

URL_INSTANCE_BACKUP_SCHEDULE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/backup-schedule")
"""
### Request Methods

- `Get`: Get the backup schedule for an Instance.
- `Post`: Set the backup schedule for an Instance in UTC. The `type` is required.
"""

URL_INSTANCE_RESTORE: Final[Url] = Url(Provider.VULTR).uri("instances/{instance-id}/restore")
"""
### Request Methods

- `Post`: Restore an Instance from either `backup_id` or `snapshot_id`.
"""

URL_ISO: Final[Url] = Url(Provider.VULTR).uri("iso")
"""
### Request Methods

- `Get`: Get the ISOs in your account.
- `Post`: Create a new ISO in your account from `url`.
"""

URL_ISO_ID: Final[Url] = Url(Provider.VULTR).uri("iso/{iso-id}")
"""
### Request Methods

- `Get`: Get information for an ISO.
- `Delete`: Delete an ISO.
"""

URL_ISO_PUBLIC: Final[Url] = Url(Provider.VULTR).uri("iso-public")
"""
### Request Methods

- `Get`: List all Vultr Public ISOs.
"""


URL_KUBERNETES_LIST: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters")
"""
### Request Methods

- `Get`: List all Kubernetes clusters currently deployed.\n
- `Post`: Create Kubernetes Cluster.
"""

URL_KUBERNETES_GET: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}")
"""
### Request Methods

- `Get`: Get Kubernetes Cluster.
- `Put`: Update Kubernetes Cluster.
- `Delete`: Delete Kubernetes Cluster.
"""

URL_KUBERNETES_DELETE_WITH_LINKED_RESOURCES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/delete-with-linked-resources")
"""
### Request Methods

- `Delete`: Delete Kubernetes Cluster and all related resources.
"""

URL_KUBERNETES_RESOURCES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/resources")
"""
### Request Methods

- `Get`: Get the block storage volumes and load balancers deployed by the specified Kubernetes cluster.
"""

URL_KUBERNETES_AVAILABLE_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/available-upgrades")
"""
### Request Methods

- `Get`: Get the available upgrades for the specified Kubernetes cluster.
"""

URL_KUBERNETES_UPGRADES: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/upgrades")
"""
### Request Methods

- `Post`: Start a Kubernetes cluster upgrade.
"""

URL_KUBERNETES_NODEPOOLS: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools")
"""
### Request Methods

- `Get`: List all available NodePools on a Kubernetes Cluster.
- `Post`: Create NodePool for a Existing Kubernetes Cluster.
"""

URL_KUBERNETES_NODEPOOL: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}")
"""
### Request Methods

- `Get`: Get Nodepool from a Kubernetes Cluster.
- `Patch`: Update a Nodepool on a Kubernetes Cluster.
- `Delete`: Delete a NodePool from a Kubernetes Cluster.
"""

URL_KUBERNETES_NODEPOOL_INSTANCE: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}")
"""
### Request Methods

- `Delete`: Delete a single nodepool instance from a given Nodepool.
"""

URL_KUBERNETES_NODEPOOL_INSTANCE_RECYCLE: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/node-pools/{nodepool-id}/nodes/{node-id}/recycle")
"""
### Request Methods

- `Post`: Recycle a specific NodePool Instance.
"""

URL_KUBERNETES_CONFIG: Final[Url] = Url(Provider.VULTR).uri("kubernetes/clusters/{vke-id}/config")
"""
### Request Methods

- `Get`: Get Kubernetes Cluster Kubeconfig.
"""

URL_KUBERNETES_VERSIONS: Final[Url] = Url(Provider.VULTR).uri("kubernetes/versions")
"""
### Request Methods

- `Get`: Get a list of supported Kubernetes versions.
"""


URL_LOAD_BALANCER_LIST: Final[Url] = Url(Provider.VULTR).uri("load-balancers")
"""
### Request Methods

- `Get`: List the Load Balancers in your account.
"""

URL_LOAD_BALANCER_CREATE: Final[Url] = Url(Provider.VULTR).uri("load-balancers")
"""
### Request Methods

- `Post`: Create a new Load Balancer in a particular `region`.
"""

URL_LOAD_BALANCER_GET: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}")
"""
### Request Methods

- `Get`: Get information for a Load Balancer.
- `Patch`: Update information for a Load Balancer. All attributes are optional. If not set, the attributes will retain their original values.
- `Delete`: Delete a Load Balancer.
"""

URL_LOAD_BALANCER_SSL: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/ssl")
"""
### Request Methods

- `Delete`: Delete a Load Balancer SSL.
"""

URL_LOAD_BALANCER_AUTO_SSL: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/auto_ssl")
"""
### Request Methods

- `Delete`: Remove a Load Balancer Auto SSL. This will not remove an ssl certificate from the load balancer.
"""

URL_LOAD_BALANCER_FORWARDING_RULES: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/forwarding-rules")
"""
### Request Methods

- `Get`: List the fowarding rules for a Load Balancer.
- `Post`: Create a new forwarding rule for a Load Balancer.
"""

URL_LOAD_BALANCER_FORWARDING_RULE: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{load-balancer-id}/forwarding-rules/{forwarding-rule-id}")
"""
### Request Methods

- `Get`: Get information for a Forwarding Rule on a Load Balancer.
- `Delete`: Delete a Forwarding Rule on a Load Balancer.
"""

URL_LOAD_BALANCER_FIREWALL_RULES: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{loadbalancer-id}/firewall-rules")  # Note: Inconsistent hyphenation with other URLs. Consider changing to load-balancer-id for consistency.
"""
### Request Methods

- `Get`: List the firewall rules for a Load Balancer.
"""


URL_LOAD_BALANCER_FIREWALL_RULE: Final[Url] = Url(Provider.VULTR).uri("load-balancers/{loadbalancer-id}/firewall-rules/{firewall-rule-id}") # Note: Inconsistent hyphenation with other URLs. Consider changing to load-balancer-id for consistency.
"""
### Request Methods

- `Get`: Get a firewall rule for a Load Balancer.
"""
URL_MARKET_PLACE_APP_VARIABLE: Final[Url] = Url(Provider.VULTR).uri("marketplace/apps/{image-id}/variables")
"""
### Request Methods

- `Get`: List all user-supplied variables for a Marketplace App.
"""
URL_OS: Final[Url] = Url(Provider.VULTR).uri("os")
"""
### Request Methods

- `Get`: List the OS images available for installation at Vultr.
"""

URL_PLAN: Final[Url] = Url(Provider.VULTR).uri("plans")
"""
### Request Methods

- `Get`: Get a list of all VPS plans at Vultr.
"""

URL_PLAN_METAL: Final[Url] = Url(Provider.VULTR).uri("plans-metal")
"""
### Request Methods

- `Get`: Get a list of all Bare Metal plans at Vultr.
"""

URL_REGION: Final[Url] = Url(Provider.VULTR).uri("regions")
"""
### Request Methods

- `Get`: List all Regions at Vultr.
"""

URL_REGION_ID_AVAILABLE: Final[Url] = Url(Provider.VULTR).uri("regions/{region-id}/availability")
"""
### Request Methods

- `Get`: Get a list of the available plans in Region `region-id`. Not all plans are available in all regions.
"""

URL_RESERVED_IP: Final[Url] = Url(Provider.VULTR).uri("reserved-ips")
"""
### Request Methods

- `Get`: List all Reserved IPs in your account.
- `Post`: Create a new Reserved IP. The `region` and `ip_type` attributes are required.
"""

URL_RESERVED_IP_ID: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/{reserved-ip}")
"""
### Request Methods

- `Get`: Get information about a Reserved IP.
- `Patch`: Update information on a Reserved IP.
- `Delete`: Delete a Reserved IP.
"""

URL_RESERVED_IP_ATTACH: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/{reserved-ip}/attach")
"""
### Request Methods

- `Post`: Attach a Reserved IP to an compute instance or a baremetal instance - `instance_id`.
"""

URL_RESERVED_IP_DETACH: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/{reserved-ip}/detach")
"""
### Request Methods

- `Post`: Detach a Reserved IP.
"""

URL_RESERVED_IP_CONVERT: Final[Url] = Url(Provider.VULTR).uri("reserved-ips/convert")
"""
### Request Methods

- `Post`: Convert the `ip_address` of an existing instance into a Reserved IP.
"""

URL_SNAPSHOT: Final[Url] = Url(Provider.VULTR).uri("snapshots")
"""
### Request Methods

- `Get`: Get information about all Snapshots in your account.
- `Post`: Create a new Snapshot for `instance_id`.
"""

URL_SNAPSHOT_ID: Final[Url] = Url(Provider.VULTR).uri("snapshots/{snapshot-id}")
"""
### Request Methods

- `Get`: Get information about a Snapshot.
- `Put`: Update the description for a Snapshot.
- `Delete`: Delete a Snapshot.
"""

URL_SNAPSHOT_CREATE_FROM_URL: Final[Url] = Url(Provider.VULTR).uri("snapshots/create-from-url")
"""
### Request Methods

- `Post`: Create a new Snapshot from a RAW image located at `url`.
"""


URL_SSH_KEY_LIST: Final[Url] = Url(Provider.VULTR).uri("ssh-keys")
"""
### Request Methods

- `Get`: List all SSH Keys in your account.
- `Post`: Create a new SSH Key for use with future instances. This does not update any running instances.
"""

URL_SSH_KEY: Final[Url] = Url(Provider.VULTR).uri("ssh-keys/{ssh-key-id}")
"""
### Request Methods

- `Get`: Get information about an SSH Key.
- `Patch`: Update an SSH Key. The attributes `name` and `ssh_key` are optional. If not set, the attributes will retain their original values. New deployments will use the updated key, but this action does not update previously deployed instances.
- `Delete`: Delete an SSH Key.
"""

URL_STARTUP_SCRIPT_LIST: Final[Url] = Url(Provider.VULTR).uri("startup-scripts")
"""
### Request Methods

- `Get`: Get a list of all Startup Scripts.
- `Post`: Create a new Startup Script. The `name` and `script` attributes are required, and scripts are base-64 encoded.
"""

URL_STARTUP_SCRIPT: Final[Url] = Url(Provider.VULTR).uri("startup-scripts/{startup-id}")
"""
### Request Methods

- `Get`: Get information for a Startup Script.
- `Patch`: Update a Startup Script. The attributes `name` and `script` are optional. If not set, the attributes will retain their original values. The `script` attribute is base-64 encoded. New deployments will use the updated script, but this action does not update previously deployed instances.
- `Delete`: Delete a Startup Script.
"""

URL_SUB_ACCOUNT_LIST: Final[Url] = Url(Provider.VULTR).uri("subaccounts")
"""
### Request Methods

- `Get`: Get information about all sub-accounts for your account.
- `Post`: Create a new subaccount.
"""

URL_USER_LIST: Final[Url] = Url(Provider.VULTR).uri("users")
"""
### Request Methods

- `Get`: Get a list of all Users in your account.
- `Post`: Create a new User. The `email`, `name`, and `password` attributes are required.
"""

URL_USER: Final[Url] = Url(Provider.VULTR).uri("users/{user-id}")
"""
### Request Methods

- `Get`: Get information about a User.
- `Patch`: Update information for a User. All attributes are optional. If not set, the attributes will retain their original values.
- `Delete`: Delete a User.
"""

URL_VPC_LIST: Final[Url] = Url(Provider.VULTR).uri("vpcs")
"""
### Request Methods

- `Get`: Get a list of all VPCs in your account.
"""

URL_VPC_GET: Final[Url] = Url(Provider.VULTR).uri("vpcs/{vpc-id}")
"""
### Request Methods

- `Get`: Get information about a VPC.
- `Put`: Update information for a VPC.
- `Delete`: Delete a VPC.
"""

URL_VPC2_LIST: Final[Url] = Url(Provider.VULTR).uri("vpc2")
"""
### Request Methods

- `Get`: Get a list of all VPC 2.0 networks in your account.
- `Post`: Create a new VPC 2.0 network in a `region`. VPCs should use [RFC1918 private address space](https://tools.ietf.org/html/rfc1918):

    10.0.0.0    - 10.255.255.255  (10/8 prefix)
    172.16.0.0  - 172.31.255.255  (172.16/12 prefix)
    192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
"""

URL_VPC2_GET: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}")
"""
### Request Methods

- `Get`: Get information about a VPC 2.0 network.
- `Put`: Update information for a VPC 2.0 network.
- `Delete`: Delete a VPC 2.0 network.
"""

URL_VPC2_NODES: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}/nodes")
"""
### Request Methods

- `Get`: Get a list of nodes attached to a VPC 2.0 network.
"""

URL_VPC2_ATTACH_NODES: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}/nodes/attach")
"""
### Request Methods

- `Post`: Attach nodes to a VPC 2.0 network.
"""

URL_VPC2_DETACH_NODES: Final[Url] = Url(Provider.VULTR).uri("vpc2/{vpc-id}/nodes/detach")
"""
### Request Methods

- `Post`: Remove nodes from a VPC 2.0 network.
"""


URL_VFS_REGIONS: Final[Url] = Url(Provider.VULTR).uri("vfs/regions")
"""
### Request Methods

- `Get`: Retrieve a list of all regions where VFS can be deployed.
"""

URL_VFS_LIST: Final[Url] = Url(Provider.VULTR).uri("vfs")
"""
### Request Methods

- `Get`: Retrieve a list of all VFS subscriptions for the account.
- `Post`: Create a new VFS subscription with the specified configuration.
"""

URL_VFS_GET: Final[Url] = Url(Provider.VULTR).uri("vfs/{vfs_id}")
"""
### Request Methods

- `Get`: Retrieve a specific VFS subscription by ID.
- `Put`: Update a VFS subscription's label or storage size.
- `Delete`: Delete a specific VFS subscription by ID.
"""

URL_VFS_ATTACHMENTS: Final[Url] = Url(Provider.VULTR).uri("vfs/{vfs_id}/attachments")
"""
### Request Methods

- `Get`: Retrieve a list of all attachments for a specific VFS subscription.
"""

URL_VFS_ATTACHMENT: Final[Url] = Url(Provider.VULTR).uri("vfs/{vfs_id}/attachments/{vps_id}")
"""
### Request Methods

- `Put`: Attach a VPS instance to a VFS subscription.
- `Get`: Retrieve details about a specific VFS-VPS attachment.
- `Delete`: Detach a VPS instance from a VFS subscription.
"""

URL_OBJECT_STORAGE_LIST: Final[Url] = Url(Provider.VULTR).uri("object-storage")
"""
### Request Methods

- `Get`: Get a list of all Object Storage in your account.
- `Post`: Create new Object Storage. The `cluster_id` attribute is required.
"""

URL_OBJECT_STORAGE_ID: Final[Url] = Url(Provider.VULTR).uri("object-storage/{object-storage-id}")
"""
### Request Methods

- `Get`: Get information about an Object Storage.
- `Put`: Update the label for an Object Storage.
- `Delete`: Delete an Object Storage.
"""

URL_OBJECT_STORAGE_ID_REGENERATE: Final[Url] = Url(Provider.VULTR).uri("object-storage/{object-storage-id}/regenerate-keys")  # Note: Corrected to regenerate-keys based on provided JSON
"""
### Request Methods

- `Post`: Regenerate the keys for an Object Storage.
"""

URL_OBJECT_STORAGE_CLUSTERS: Final[Url] = Url(Provider.VULTR).uri("object-storage/clusters")
"""
### Request Methods

- `Get`: Get a list of all Object Storage Clusters.
"""
