from typing import Optional, List, Literal

from typing import Optional

class ListInstancesData:
    def __init__(self):
        """
        Data structure used for filtering the list of Vultr VPS Instances.
        """
        self._per_page: Optional[int] = None
        self._cursor: Optional[str] = None
        self._tag: Optional[str] = None
        self._label: Optional[str] = None
        self._main_ip: Optional[str] = None
        self._region: Optional[str] = None
        self._firewall_group_id: Optional[str] = None
        self._hostname: Optional[str] = None
        self._show_pending_charges: Optional[bool] = None

    def per_page(self, per_page: int) -> "ListInstancesData":
        """
        Set the number of items requested per page. Default is 100 and Max is 500.

        Args:
            per_page (int): The number of items per page.

        Returns:
            ListInstancesData: The current object with the per_page value set.
        """
        self._per_page = per_page
        return self

    def cursor(self, cursor: str) -> "ListInstancesData":
        """
        Set the cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Args:
            cursor (str): The cursor for paging.

        Returns:
            ListInstancesData: The current object with the cursor value set.
        """
        self._cursor = cursor
        return self

    def tag(self, tag: str) -> "ListInstancesData":
        """
        Filter by specific tag. (Deprecated)

        Args:
            tag (str): The tag to filter by.

        Returns:
            ListInstancesData: The current object with the tag filter set.
        """
        self._tag = tag
        return self

    def label(self, label: str) -> "ListInstancesData":
        """
        Filter by label.

        Args:
            label (str): The label to filter by.

        Returns:
            ListInstancesData: The current object with the label filter set.
        """
        self._label = label
        return self

    def main_ip(self, main_ip: str) -> "ListInstancesData":
        """
        Filter by main IP address.

        Args:
            main_ip (str): The main IP address to filter by.

        Returns:
            ListInstancesData: The current object with the main IP filter set.
        """
        self._main_ip = main_ip
        return self

    def region(self, region: str) -> "ListInstancesData":
        """
        Filter by [Region id](#operation/list-regions).

        Args:
            region (str): The region ID to filter by.

        Returns:
            ListInstancesData: The current object with the region filter set.
        """
        self._region = region
        return self

    def firewall_group_id(self, firewall_group_id: str) -> "ListInstancesData":
        """
        Filter by [Firewall group id](#operation/list-firewall-groups).

        Args:
            firewall_group_id (str): The firewall group ID to filter by.

        Returns:
            ListInstancesData: The current object with the firewall group ID filter set.
        """
        self._firewall_group_id = firewall_group_id
        return self

    def hostname(self, hostname: str) -> "ListInstancesData":
        """
        Filter by hostname.

        Args:
            hostname (str): The hostname to filter by.

        Returns:
            ListInstancesData: The current object with the hostname filter set.
        """
        self._hostname = hostname
        return self

    def show_pending_charges(self, show_pending_charges: bool) -> "ListInstancesData":
        """
        Set to `true` to show pending charges.

        Args:
            show_pending_charges (bool): Whether to show pending charges.

        Returns:
            ListInstancesData: The current object with the show_pending_charges setting set.
        """
        self._show_pending_charges = show_pending_charges
        return self
    
    def apply_params(self, request):
        """
        Applies the parameters from this data structure to a given request object.

        Args:
            request (composer.Request): The request object to apply the parameters to.
        
        Returns:
            composer.Request: The request object with the parameters applied.
        """
        if self._per_page is not None:
            request.add_param("per_page", self._per_page)
        if self._cursor is not None:
            request.add_param("cursor", self._cursor)
        if self._tag is not None:
            request.add_param("tag", self._tag)
        if self._label is not None:
            request.add_param("label", self._label)
        if self._main_ip is not None:
            request.add_param("main_ip", self._main_ip)
        if self._region is not None:
            request.add_param("region", self._region)
        if self._firewall_group_id is not None:
            request.add_param("firewall_group_id", self._firewall_group_id)
        if self._hostname is not None:
            request.add_param("hostname", self._hostname)
        if self._show_pending_charges is not None:
            request.add_param("show_pending_charges", self._show_pending_charges)
        return request
    
class CreateInstanceData:
    def __init__(self, region: str, plan: str):
        """
        Data structure used for creating a Vultr VPS Instance.

        Args:
            region (str): [Required] [Region id](#operation/list-regions) where the Instance is located.
            plan (str): [Required] [Plan id](#operation/list-plans) to use when deploying this instance.
        """
        self._region: str = region
        self._plan: str = plan
        self._os_id: Optional[int] = None
        self._ipxe_chain_url: Optional[str] = None
        self._iso_id: Optional[str] = None
        self._script_id: Optional[str] = None
        self._snapshot_id: Optional[str] = None
        self._enable_ipv6: Optional[bool] = None
        self._disable_public_ipv4: Optional[bool] = None
        self._attach_private_network: Optional[List[str]] = None
        self._attach_vpc: Optional[List[str]] = None
        self._attach_vpc2: Optional[List[str]] = None
        self._label: Optional[str] = None
        self._sshkey_id: Optional[List[str]] = None
        self._backups: Optional[Literal["enabled", "disabled"]] = None
        self._app_id: Optional[int] = None
        self._image_id: Optional[str] = None
        self._user_data: Optional[str] = None
        self._ddos_protection: Optional[bool] = None
        self._activation_email: Optional[bool] = None
        self._hostname: Optional[str] = None
        self._tag: Optional[str] = None
        self._firewall_group_id: Optional[str] = None
        self._reserved_ipv4: Optional[str] = None
        self._enable_private_network: Optional[bool] = None
        self._enable_vpc: Optional[bool] = None
        self._enable_vpc2: Optional[bool] = None
        self._tags: Optional[List[str]] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        self._app_variables: Optional[dict] = None

    def os_id(self, os_id: int) -> "CreateInstanceData":
        """
        Set the [Operating System id](#operation/list-os) to use when deploying this instance.

        Args:
            os_id (int): The OS ID.

        Returns:
            CreateInstanceData: The current object with the OS ID set.
        """
        self._os_id = os_id
        return self

    def ipxe_chain_url(self, ipxe_chain_url: str) -> "CreateInstanceData":
        """
        Set the URL location of the iPXE chainloader.

        Args:
            ipxe_chain_url (str): The iPXE chainloader URL.

        Returns:
            CreateInstanceData: The current object with the iPXE chainloader URL set.
        """
        self._ipxe_chain_url = ipxe_chain_url
        return self

    def iso_id(self, iso_id: str) -> "CreateInstanceData":
        """
        Set the [ISO id](#operation/list-isos) to use when deploying this instance.

        Args:
            iso_id (str): The ISO ID.

        Returns:
            CreateInstanceData: The current object with the ISO ID set.
        """
        self._iso_id = iso_id
        return self

    def script_id(self, script_id: str) -> "CreateInstanceData":
        """
        Set the [Startup Script id](#operation/list-startup-scripts) to use.

        Args:
            script_id (str): The Startup Script ID.

        Returns:
            CreateInstanceData: The current object with the Startup Script ID set.
        """
        self._script_id = script_id
        return self

    def snapshot_id(self, snapshot_id: str) -> "CreateInstanceData":
        """
        Set the [Snapshot id](#operation/list-snapshots) to use for deployment.

        Args:
            snapshot_id (str): The Snapshot ID.

        Returns:
            CreateInstanceData: The current object with the Snapshot ID set.
        """
        self._snapshot_id = snapshot_id
        return self

    def enable_ipv6(self, enable_ipv6: bool) -> "CreateInstanceData":
        """
        Enable IPv6. Default: false

        Args:
            enable_ipv6 (bool): Whether to enable IPv6.

        Returns:
            CreateInstanceData: The current object with the IPv6 setting set.
        """
        self._enable_ipv6 = enable_ipv6
        return self

    def disable_public_ipv4(self, disable_public_ipv4: bool) -> "CreateInstanceData":
        """
        Disable public IPv4 when IPv6 is enabled. Default: false

        Args:
            disable_public_ipv4 (bool): Whether to disable public IPv4.

        Returns:
            CreateInstanceData: The current object with the public IPv4 setting set.
        """
        self._disable_public_ipv4 = disable_public_ipv4
        return self

    def attach_private_network(self, attach_private_network: List[str]) -> "CreateInstanceData":
        """
        [Deprecated] Use `attach_vpc`. Set the [Private Network ids](#operation/list-networks) to attach.

        Args:
            attach_private_network (List[str]): The Private Network IDs.

        Returns:
            CreateInstanceData: The current object with the Private Network IDs set.
        """
        self._attach_private_network = attach_private_network
        return self

    def attach_vpc(self, attach_vpc: List[str]) -> "CreateInstanceData":
        """
        Set the [VPC IDs](#operation/list-vpcs) to attach.

        Args:
            attach_vpc (List[str]): The VPC IDs.

        Returns:
            CreateInstanceData: The current object with the VPC IDs set.
        """
        self._attach_vpc = attach_vpc
        return self

    def attach_vpc2(self, attach_vpc2: List[str]) -> "CreateInstanceData":
        """
        Set the [VPC 2.0 IDs](#operation/list-vpc2) to attach.

        Args:
            attach_vpc2 (List[str]): The VPC 2.0 IDs.

        Returns:
            CreateInstanceData: The current object with the VPC 2.0 IDs set.
        """
        self._attach_vpc2 = attach_vpc2
        return self

    def label(self, label: str) -> "CreateInstanceData":
        """
        Set the user-supplied label (max 255 characters).

        Args:
            label (str): The label.

        Returns:
            CreateInstanceData: The current object with the label set.
        """
        self._label = label
        return self

    def sshkey_id(self, sshkey_id: List[str]) -> "CreateInstanceData":
        """
        Set the [SSH Key ids](#operation/list-ssh-keys) to install.

        Args:
            sshkey_id (List[str]): The SSH Key IDs.

        Returns:
            CreateInstanceData: The current object with the SSH Key IDs set.
        """
        self._sshkey_id = sshkey_id
        return self

    def backups(self, backups: Literal["enabled", "disabled"]) -> "CreateInstanceData":
        """
        Enable automatic backups.

        Args:
            backups (Literal["enabled", "disabled"]): Whether to enable automatic backups.

        Returns:
            CreateInstanceData: The current object with the backups setting set.
        """
        self._backups = backups
        return self
    
    def app_id(self, app_id: int) -> "CreateInstanceData":
        """
        Set the [Application id](#operation/list-applications) for deployment.

        Args:
            app_id (int): The Application ID.

        Returns:
            CreateInstanceData: The current object with the Application ID set.
        """
        self._app_id = app_id
        return self
    
    def image_id(self, image_id: str) -> "CreateInstanceData":
        """
        Set the [Application image_id](#operation/list-applications) for deployment.

        Args:
            image_id (str): The Application image ID.

        Returns:
            CreateInstanceData: The current object with the Application image ID set.
        """
        self._image_id = image_id
        return self

    def user_data(self, user_data: str) -> "CreateInstanceData":
        """
        Set the Base64-encoded user data (cloud-init).

        Args:
            user_data (str): The user data.

        Returns:
            CreateInstanceData: The current object with the user data set.
        """
        self._user_data = user_data
        return self

    def ddos_protection(self, ddos_protection: bool) -> "CreateInstanceData":
        """
        Enable DDoS protection. Default: false

        Args:
            ddos_protection (bool): Whether to enable DDoS protection.

        Returns:
            CreateInstanceData: The current object with the DDoS protection setting set.
        """
        self._ddos_protection = ddos_protection
        return self

    def activation_email(self, activation_email: bool) -> "CreateInstanceData":
        """
        Send deployment email. Default: false

        Args:
            activation_email (bool): Whether to send deployment email.

        Returns:
            CreateInstanceData: The current object with the activation email setting set.
        """
        self._activation_email = activation_email
        return self

    def hostname(self, hostname: str) -> "CreateInstanceData":
        """
        Set the hostname (max 255 characters).

        Args:
            hostname (str): The hostname.

        Returns:
            CreateInstanceData: The current object with the hostname set.
        """
        self._hostname = hostname
        return self
    
    def tag(self, tag: str) -> "CreateInstanceData":
        """
        [Deprecated] Use `tags`. Set the user-supplied tag.

        Args:
            tag (str): The tag.

        Returns:
            CreateInstanceData: The current object with the tag set.
        """
        self._tag = tag
        return self

    def firewall_group_id(self, firewall_group_id: str) -> "CreateInstanceData":
        """
        Set the [Firewall Group id](#operation/list-firewall-groups) to attach.

        Args:
            firewall_group_id (str): The Firewall Group ID.

        Returns:
            CreateInstanceData: The current object with the Firewall Group ID set.
        """
        self._firewall_group_id = firewall_group_id
        return self
    
    def reserved_ipv4(self, reserved_ipv4: str) -> "CreateInstanceData":
        """
        Set the [Reserved IP id](#operation/list-reserved-ips) to use as main IP.

        Args:
            reserved_ipv4 (str): The Reserved IP ID.

        Returns:
            CreateInstanceData: The current object with the Reserved IP ID set.
        """
        self._reserved_ipv4 = reserved_ipv4
        return self

    def enable_private_network(self, enable_private_network: bool) -> "CreateInstanceData":
        """
        [Deprecated] Use `enable_vpc`. Enable private networking.

        Args:
            enable_private_network (bool): Whether to enable private networking.

        Returns:
            CreateInstanceData: The current object with the private networking setting set.
        """
        self._enable_private_network = enable_private_network
        return self
    
    def enable_vpc(self, enable_vpc: bool) -> "CreateInstanceData":
        """
        Enable VPC support. Default: false

        Args:
            enable_vpc (bool): Whether to enable VPC support.

        Returns:
            CreateInstanceData: The current object with the VPC support setting set.
        """
        self._enable_vpc = enable_vpc
        return self

    def enable_vpc2(self, enable_vpc2: bool) -> "CreateInstanceData":
        """
        Enable VPC 2.0 support. Default: false

        Args:
            enable_vpc2 (bool): Whether to enable VPC 2.0 support.

        Returns:
            CreateInstanceData: The current object with the VPC 2.0 support setting set.
        """
        self._enable_vpc2 = enable_vpc2
        return self

    def tags(self, tags: List[str]) -> "CreateInstanceData":
        """
        Set the tags to apply (max 5 tags, 255 chars each).

        Args:
            tags (List[str]): The tags.

        Returns:
            CreateInstanceData: The current object with the tags set.
        """
        self._tags = tags
        return self

    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "CreateInstanceData":
        """
        Set the Linux user scheme.

        Args:
            user_scheme (Literal["root", "limited"]): The user scheme.

        Returns:
            CreateInstanceData: The current object with the user scheme set.
        """
        self._user_scheme = user_scheme
        return self
    
    def app_variables(self, app_variables: dict) -> "CreateInstanceData":
        """
        Set the [App variables](#operation/list-marketplace-app-variables) (key/value pairs).

        Args:
            app_variables (dict): The app variables.

        Returns:
            CreateInstanceData: The current object with the app variables set.
        """
        self._app_variables = app_variables
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "region": self._region,
            "plan": self._plan,
            "os_id": self._os_id,
            "ipxe_chain_url": self._ipxe_chain_url,
            "iso_id": self._iso_id,
            "script_id": self._script_id,
            "snapshot_id": self._snapshot_id,
            "enable_ipv6": self._enable_ipv6,
            "disable_public_ipv4": self._disable_public_ipv4,
            "attach_private_network": self._attach_private_network,
            "attach_vpc": self._attach_vpc,
            "attach_vpc2": self._attach_vpc2,
            "label": self._label,
            "sshkey_id": self._sshkey_id,
            "backups": self._backups,
            "app_id": self._app_id,
            "image_id": self._image_id,
            "user_data": self._user_data,
            "ddos_protection": self._ddos_protection,
            "activation_email": self._activation_email,
            "hostname": self._hostname,
            "tag": self._tag,
            "firewall_group_id": self._firewall_group_id,
            "reserved_ipv4": self._reserved_ipv4,
            "enable_private_network": self._enable_private_network,
            "enable_vpc": self._enable_vpc,
            "enable_vpc2": self._enable_vpc2,
            "tags": self._tags,
            "user_scheme": self._user_scheme,
            "app_variables": self._app_variables,
        }
        return {k: v for k, v in data.items() if v is not None}
    
class UpdateInstanceData:
    def __init__(self):
        """
        Data structure used for updating a Vultr VPS Instance.
        """
        self._app_id: Optional[int] = None
        self._image_id: Optional[str] = None
        self._backups: Optional[Literal["enabled", "disabled"]] = None
        self._firewall_group_id: Optional[str] = None
        self._enable_ipv6: Optional[bool] = None
        self._os_id: Optional[int] = None
        self._user_data: Optional[str] = None
        self._tag: Optional[str] = None
        self._plan: Optional[str] = None
        self._ddos_protection: Optional[bool] = None
        self._attach_private_network: Optional[List[str]] = None
        self._attach_vpc: Optional[List[str]] = None
        self._attach_vpc2: Optional[List[str]] = None
        self._detach_private_network: Optional[List[str]] = None
        self._detach_vpc: Optional[List[str]] = None
        self._detach_vpc2: Optional[List[str]] = None
        self._enable_private_network: Optional[bool] = None
        self._enable_vpc: Optional[bool] = None
        self._enable_vpc2: Optional[bool] = None
        self._label: Optional[str] = None
        self._tags: Optional[List[str]] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None

    def app_id(self, app_id: int) -> "UpdateInstanceData":
        """
        Set the [Application id](#operation/list-applications) to reinstall the instance.

        Args:
            app_id (int): The Application ID.

        Returns:
            UpdateInstanceData: The current object with the Application ID set.
        """
        self._app_id = app_id
        return self

    def image_id(self, image_id: str) -> "UpdateInstanceData":
        """
        Set the [Application image_id](#operation/list-applications) to reinstall the instance.

        Args:
            image_id (str): The Application image ID.

        Returns:
            UpdateInstanceData: The current object with the Application image ID set.
        """
        self._image_id = image_id
        return self

    def backups(self, backups: Literal["enabled", "disabled"]) -> "UpdateInstanceData":
        """
        Enable automatic backups.

        Args:
            backups (Literal["enabled", "disabled"]): Whether to enable automatic backups.

        Returns:
            UpdateInstanceData: The current object with the backups setting set.
        """
        self._backups = backups
        return self

    def firewall_group_id(self, firewall_group_id: str) -> "UpdateInstanceData":
        """
        Set the [Firewall Group id](#operation/list-firewall-groups) to attach.

        Args:
            firewall_group_id (str): The Firewall Group ID.

        Returns:
            UpdateInstanceData: The current object with the Firewall Group ID set.
        """
        self._firewall_group_id = firewall_group_id
        return self

    def enable_ipv6(self, enable_ipv6: bool) -> "UpdateInstanceData":
        """
        Enable IPv6. Default: false

        Args:
            enable_ipv6 (bool): Whether to enable IPv6.

        Returns:
            UpdateInstanceData: The current object with the IPv6 setting set.
        """
        self._enable_ipv6 = enable_ipv6
        return self

    def os_id(self, os_id: int) -> "UpdateInstanceData":
        """
        Set the [ISO id](#operation/list-isos) to reinstall (field name may be misleading).

        Args:
            os_id (int): The ISO ID.

        Returns:
            UpdateInstanceData: The current object with the ISO ID set.
        """
        self._os_id = os_id
        return self

    def user_data(self, user_data: str) -> "UpdateInstanceData":
        """
        Set the Base64-encoded user data (cloud-init).

        Args:
            user_data (str): The user data.

        Returns:
            UpdateInstanceData: The current object with the user data set.
        """
        self._user_data = user_data
        return self

    def tag(self, tag: str) -> "UpdateInstanceData":
        """
        [Deprecated] Use `tags`. Set the user-supplied tag.

        Args:
            tag (str): The tag.

        Returns:
            UpdateInstanceData: The current object with the tag set.
        """
        self._tag = tag
        return self

    def plan(self, plan: str) -> "UpdateInstanceData":
        """
        Set the [Plan id](#operation/list-plans) for upgrade.

        Args:
            plan (str): The Plan ID.

        Returns:
            UpdateInstanceData: The current object with the Plan ID set.
        """
        self._plan = plan
        return self

    def ddos_protection(self, ddos_protection: bool) -> "UpdateInstanceData":
        """
        Enable DDoS protection.

        Args:
            ddos_protection (bool): Whether to enable DDoS protection.

        Returns:
            UpdateInstanceData: The current object with the DDoS protection setting set.
        """
        self._ddos_protection = ddos_protection
        return self

    def attach_private_network(self, attach_private_network: List[str]) -> "UpdateInstanceData":
        """
        [Deprecated] Use `attach_vpc`. Set the [Private Network ids](#operation/list-networks) to attach.

        Args:
            attach_private_network (List[str]): The Private Network IDs.

        Returns:
            UpdateInstanceData: The current object with the Private Network IDs set.
        """
        self._attach_private_network = attach_private_network
        return self

    def attach_vpc(self, attach_vpc: List[str]) -> "UpdateInstanceData":
        """
        Set the [VPC IDs](#operation/list-vpcs) to attach.

        Args:
            attach_vpc (List[str]): The VPC IDs.

        Returns:
            UpdateInstanceData: The current object with the VPC IDs set.
        """
        self._attach_vpc = attach_vpc
        return self

    def attach_vpc2(self, attach_vpc2: List[str]) -> "UpdateInstanceData":
        """
        Set the [VPC 2.0 IDs](#operation/list-vpc2) to attach.

        Args:
            attach_vpc2 (List[str]): The VPC 2.0 IDs.

        Returns:
            UpdateInstanceData: The current object with the VPC 2.0 IDs set.
        """
        self._attach_vpc2 = attach_vpc2
        return self

    def detach_private_network(self, detach_private_network: List[str]) -> "UpdateInstanceData":
        """
        [Deprecated] Use `detach_vpc`. Set the [Private Network ids](#operation/list-networks) to detach.

        Args:
            detach_private_network (List[str]): The Private Network IDs.

        Returns:
            UpdateInstanceData: The current object with the Private Network IDs set.
        """
        self._detach_private_network = detach_private_network
        return self

    def detach_vpc(self, detach_vpc: List[str]) -> "UpdateInstanceData":
        """
        Set the [VPC IDs](#operation/list-vpcs) to detach.

        Args:
            detach_vpc (List[str]): The VPC IDs.

        Returns:
            UpdateInstanceData: The current object with the VPC IDs set.
        """
        self._detach_vpc = detach_vpc
        return self

    def detach_vpc2(self, detach_vpc2: List[str]) -> "UpdateInstanceData":
        """
        Set the [VPC 2.0 IDs](#operation/list-vpc2) to detach.

        Args:
            detach_vpc2 (List[str]): The VPC 2.0 IDs.

        Returns:
            UpdateInstanceData: The current object with the VPC 2.0 IDs set.
        """
        self._detach_vpc2 = detach_vpc2
        return self

    def enable_private_network(self, enable_private_network: bool) -> "UpdateInstanceData":
        """
        [Deprecated] Use `enable_vpc`. Enable private networking.

        Args:
            enable_private_network (bool): Whether to enable private networking.

        Returns:
            UpdateInstanceData: The current object with the private networking setting set.
        """
        self._enable_private_network = enable_private_network
        return self

    def enable_vpc(self, enable_vpc: bool) -> "UpdateInstanceData":
        """
        Enable VPC support. Default: false

        Args:
            enable_vpc (bool): Whether to enable VPC support.

        Returns:
            UpdateInstanceData: The current object with the VPC support setting set.
        """
        self._enable_vpc = enable_vpc
        return self

    def enable_vpc2(self, enable_vpc2: bool) -> "UpdateInstanceData":
        """
        Enable VPC 2.0 support. Default: false

        Args:
            enable_vpc2 (bool): Whether to enable VPC 2.0 support.

        Returns:
            UpdateInstanceData: The current object with the VPC 2.0 support setting set.
        """
        self._enable_vpc2 = enable_vpc2
        return self

    def label(self, label: str) -> "UpdateInstanceData":
        """
        Set the user-supplied label (max 255 characters).

        Args:
            label (str): The label.

        Returns:
            UpdateInstanceData: The current object with the label set.
        """
        self._label = label
        return self

    def tags(self, tags: List[str]) -> "UpdateInstanceData":
        """
        Set the tags to apply (max 5 tags, 255 chars each).

        Args:
            tags (List[str]): The tags.

        Returns:
            UpdateInstanceData: The current object with the tags set.
        """
        self._tags = tags
        return self

    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "UpdateInstanceData":
        """
        Set the Linux user scheme.

        Args:
            user_scheme (Literal["root", "limited"]): The user scheme.

        Returns:
            UpdateInstanceData: The current object with the user scheme set.
        """
        self._user_scheme = user_scheme
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "app_id": self._app_id,
            "image_id": self._image_id,
            "backups": self._backups,
            "firewall_group_id": self._firewall_group_id,
            "enable_ipv6": self._enable_ipv6,
            "os_id": self._os_id,
            "user_data": self._user_data,
            "tag": self._tag,
            "plan": self._plan,
            "ddos_protection": self._ddos_protection,
            "attach_private_network": self._attach_private_network,
            "attach_vpc": self._attach_vpc,
            "attach_vpc2": self._attach_vpc2,
            "detach_private_network": self._detach_private_network,
            "detach_vpc": self._detach_vpc,
            "detach_vpc2": self._detach_vpc2,
            "enable_private_network": self._enable_private_network,
            "enable_vpc": self._enable_vpc,
            "enable_vpc2": self._enable_vpc2,
            "label": self._label,
            "tags": self._tags,
            "user_scheme": self._user_scheme,
        }
        return {k: v for k, v in data.items() if v is not None}
    
class ReinstallInstanceData:
    def __init__(self):
        """
        Data structure used for reinstalling a Vultr VPS Instance.
        """
        self._hostname: Optional[str] = None

    def hostname(self, hostname: str) -> "ReinstallInstanceData":
        """
        Set the hostname to use when reinstalling this instance.

        Args:
            hostname (str): The hostname.

        Returns:
            ReinstallInstanceData: The current object with the hostname set.
        """
        self._hostname = hostname
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {"hostname": self._hostname}
        return {k: v for k, v in data.items() if v is not None}
    
class AttachISOInstanceData:
    def __init__(self, iso_id: str):
        """
        Data structure used for attaching an ISO to a Vultr VPS Instance.

        Args:
            iso_id (str): The [ISO id](#operation/list-isos) to attach to this Instance.
        """
        self._iso_id: str = iso_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"iso_id": self._iso_id}
    
class AttachPrivateNetworkInstanceData:
    def __init__(self, network_id: str):
        """
        Data structure used for attaching a Private Network to a Vultr VPS Instance. (Deprecated)

        Args:
            network_id (str): The [Private Network id](#operation/list-networks) to attach to this Instance.
        """
        self._network_id: str = network_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"network_id": self._network_id}

class DetachPrivateNetworkInstanceData:
    def __init__(self, network_id: str):
        """
        Data structure used for detaching a Private Network from a Vultr VPS Instance. (Deprecated)

        Args:
            network_id (str): The [Private Network id](#operation/list-networks) to detach from this Instance.
        """
        self._network_id: str = network_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"network_id": self._network_id}
    
class AttachVPCInstanceData:
    def __init__(self, vpc_id: str):
        """
        Data structure used for attaching a VPC to a Vultr VPS Instance.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs) to attach to this Instance.
        """
        self._vpc_id: str = vpc_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"vpc_id": self._vpc_id}

class DetachVPCInstanceData:
    def __init__(self, vpc_id: str):
        """
        Data structure used for detaching a VPC from a Vultr VPS Instance.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs) to detach from this Instance.
        """
        self._vpc_id: str = vpc_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"vpc_id": self._vpc_id}
    
class AttachVPC2InstanceData:
    def __init__(self, vpc_id: str):
        """
        Data structure used for attaching a VPC 2.0 Network to a Vultr VPS Instance.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpc2) to attach to this Instance.
        """
        self._vpc_id: str = vpc_id
        self._ip_address: Optional[str] = None

    def ip_address(self, ip_address: str) -> "AttachVPC2InstanceData":
        """
        Set the IP address to use for this instance on the attached VPC 2.0 network.

        Args:
            ip_address (str): The IP address.

        Returns:
            AttachVPC2InstanceData: The current object with the IP address set.
        """
        self._ip_address = ip_address
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "vpc_id": self._vpc_id,
            "ip_address": self._ip_address,
        }
        return {k: v for k, v in data.items() if v is not None}

class DetachVPC2InstanceData:
    def __init__(self, vpc_id: str):
        """
        Data structure used for detaching a VPC 2.0 Network from a Vultr VPS Instance.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpc2) to detach from this Instance.
        """
        self._vpc_id: str = vpc_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"vpc_id": self._vpc_id}


class SetInstanceBackupScheduleData:
    def __init__(self, type: Literal["daily", "weekly", "monthly", "daily_alt_even", "daily_alt_odd"]):
        """
        Data structure used for setting the backup schedule for a Vultr VPS Instance.

        Args:
            type (Literal["daily", "weekly", "monthly", "daily_alt_even", "daily_alt_odd"]): Type of backup schedule.
        """
        self._type: Literal["daily", "weekly", "monthly", "daily_alt_even", "daily_alt_odd"] = type
        self._hour: Optional[int] = None
        self._dow: Optional[int] = None
        self._dom: Optional[int] = None

    def hour(self, hour: int) -> "SetInstanceBackupScheduleData":
        """
        Set the hour of day to run in UTC.

        Args:
            hour (int): The hour of the day.

        Returns:
            SetInstanceBackupScheduleData: The current object with the hour set.
        """
        self._hour = hour
        return self

    def dow(self, dow: int) -> "SetInstanceBackupScheduleData":
        """
        Set the day of week to run (1-7).

        Args:
            dow (int): The day of the week.

        Returns:
            SetInstanceBackupScheduleData: The current object with the day of week set.
        """
        self._dow = dow
        return self

    def dom(self, dom: int) -> "SetInstanceBackupScheduleData":
        """
        Set the day of month to run (1-28).

        Args:
            dom (int): The day of the month.

        Returns:
            SetInstanceBackupScheduleData: The current object with the day of month set.
        """
        self._dom = dom
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "type": self._type,
            "hour": self._hour,
            "dow": self._dow,
            "dom": self._dom,
        }
        return {k: v for k, v in data.items() if v is not None}


class RestoreInstanceData:
    def __init__(self):
        """
        Data structure used for restoring a Vultr VPS Instance.
        """
        self._backup_id: Optional[str] = None
        self._snapshot_id: Optional[str] = None

    def backup_id(self, backup_id: str) -> "RestoreInstanceData":
        """
        Set the [Backup id](#operation/list-backups) used to restore this instance.

        Args:
            backup_id (str): The Backup ID.

        Returns:
            RestoreInstanceData: The current object with the Backup ID set.
        """
        self._backup_id = backup_id
        return self

    def snapshot_id(self, snapshot_id: str) -> "RestoreInstanceData":
        """
        Set the [Snapshot id](#operation/list-snapshots) used to restore this instance.

        Args:
            snapshot_id (str): The Snapshot ID.

        Returns:
            RestoreInstanceData: The current object with the Snapshot ID set.
        """
        self._snapshot_id = snapshot_id
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "backup_id": self._backup_id,
            "snapshot_id": self._snapshot_id,
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateInstanceIPv4Data:
    def __init__(self):
        """
        Data structure used for creating an IPv4 address for a Vultr VPS Instance.
        """
        self._reboot: Optional[bool] = None
    
    def reboot(self, reboot: bool) -> "CreateInstanceIPv4Data":
        """
        Set if the server is rebooted immediately after the IPv4 address is created.

        Args:
            reboot (bool): Whether to reboot the server.

        Returns:
            CreateInstanceIPv4Data: The current object with the reboot setting set.
        """
        self._reboot = reboot
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "reboot": self._reboot
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateInstanceReverseIPv4Data:
    def __init__(self, ip: str, reverse: str):
        """
        Data structure used for creating a reverse IPv4 entry for a Vultr VPS Instance.

        Args:
            ip (str): The IPv4 address.
            reverse (str): The IPv4 reverse entry.
        """
        self._ip: str = ip
        self._reverse: str = reverse

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "ip": self._ip,
            "reverse": self._reverse,
        }

class CreateInstanceReverseIPv6Data:
    def __init__(self, ip: str, reverse: str):
        """
        Data structure used for creating a reverse IPv6 entry for a Vultr VPS Instance.

        Args:
            ip (str): The IPv6 address in full, expanded format.
            reverse (str): The IPv6 reverse entry.
        """
        self._ip: str = ip
        self._reverse: str = reverse
    
    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "ip": self._ip,
            "reverse": self._reverse
        }

class SetInstanceReverseIPv4Data:
    def __init__(self, ip: str):
        """
        Data structure used for setting a reverse DNS entry for an IPv4 address of a Vultr VPS Instance.

        Args:
            ip (str): The IPv4 address.
        """
        self._ip: str = ip
    
    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "ip": self._ip
        }