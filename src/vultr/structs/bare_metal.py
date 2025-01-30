from typing import Optional, List, Literal, Dict

class CreateBareMetalData:
    def __init__(self, region: str, plan: str):
        """
        Data structure used for creating a Vultr Bare Metal instance.

        Args:
            region (str): The [Region id](#operation/list-regions) to create the instance.
            plan (str): The [Bare Metal plan id](#operation/list-metal-plans) to use for this instance.
        """
        self._region: str = region
        self._plan: str = plan
        self._script_id: Optional[str] = None
        self._enable_ipv6: Optional[bool] = None
        self._sshkey_id: Optional[List[str]] = None
        self._user_data: Optional[str] = None
        self._label: Optional[str] = None
        self._activation_email: Optional[bool] = None
        self._hostname: Optional[str] = None
        self._reserved_ipv4: Optional[str] = None
        self._os_id: Optional[int] = None
        self._snapshot_id: Optional[str] = None
        self._app_id: Optional[int] = None
        self._image_id: Optional[str] = None
        self._persistent_pxe: Optional[bool] = None
        self._attach_vpc2: Optional[List[str]] = None
        self._detach_vpc2: Optional[List[str]] = None
        self._enable_vpc2: Optional[bool] = None
        self._tags: Optional[List[str]] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        self._mdisk_mode: Optional[Literal["raid1", "jbod", "none"]] = None
        self._app_variables: Optional[Dict[str, str]] = None

    def script_id(self, script_id: str) -> "CreateBareMetalData":
        """
        Set the [Startup Script id](#operation/list-startup-scripts) to use for this instance.

        Args:
            script_id (str): The Startup Script ID.

        Returns:
            CreateBareMetalData: The current object with the script ID set.
        """
        self._script_id = script_id
        return self

    def enable_ipv6(self, enable_ipv6: bool) -> "CreateBareMetalData":
        """
        Enable IPv6.

        Args:
            enable_ipv6 (bool): Whether to enable IPv6.

        Returns:
            CreateBareMetalData: The current object with IPv6 enabled/disabled.
        """
        self._enable_ipv6 = enable_ipv6
        return self

    def sshkey_id(self, sshkey_id: List[str]) -> "CreateBareMetalData":
        """
        Set the [SSH Key id](#operation/list-ssh-keys) to install on this instance.

        Args:
            sshkey_id (List[str]): The SSH Key IDs.

        Returns:
            CreateBareMetalData: The current object with the SSH Key IDs set.
        """
        self._sshkey_id = sshkey_id
        return self

    def user_data(self, user_data: str) -> "CreateBareMetalData":
        """
        Set the user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for this Instance.

        Args:
            user_data (str): The user data.

        Returns:
            CreateBareMetalData: The current object with the user data set.
        """
        self._user_data = user_data
        return self

    def label(self, label: str) -> "CreateBareMetalData":
        """
        Set the user-supplied label.

        Args:
            label (str): The label.

        Returns:
            CreateBareMetalData: The current object with the label set.
        """
        self._label = label
        return self

    def activation_email(self, activation_email: bool) -> "CreateBareMetalData":
        """
        Set whether to notify by email after deployment.

        Args:
            activation_email (bool): Whether to notify by email.

        Returns:
            CreateBareMetalData: The current object with the activation email setting set.
        """
        self._activation_email = activation_email
        return self

    def hostname(self, hostname: str) -> "CreateBareMetalData":
        """
        Set the user-supplied hostname to use when deploying this instance.

        Args:
            hostname (str): The hostname.

        Returns:
            CreateBareMetalData: The current object with the hostname set.
        """
        self._hostname = hostname
        return self

    def reserved_ipv4(self, reserved_ipv4: str) -> "CreateBareMetalData":
        """
        Set the [Reserved IP id](#operation/list-reserved-ips) for this instance.

        Args:
            reserved_ipv4 (str): The Reserved IP ID.

        Returns:
            CreateBareMetalData: The current object with the Reserved IP ID set.
        """
        self._reserved_ipv4 = reserved_ipv4
        return self
    
    def os_id(self, os_id: int) -> "CreateBareMetalData":
        """
        If supplied, deploy the instance using this [Operating System id](#operation/list-os).

        Args:
            os_id (int): The Operating System ID.
        
        Returns:
            CreateBareMetalData: The current object with the OS ID set.
        """
        self._os_id = os_id
        return self

    def snapshot_id(self, snapshot_id: str) -> "CreateBareMetalData":
        """
        If supplied, deploy the instance using this [Snapshot ID](#operation/list-snapshots).

        Args:
            snapshot_id (str): The Snapshot ID.
        
        Returns:
            CreateBareMetalData: The current object with the Snapshot ID set.
        """
        self._snapshot_id = snapshot_id
        return self

    def app_id(self, app_id: int) -> "CreateBareMetalData":
        """
        If supplied, deploy the instance using this [Application id](#operation/list-applications).

        Args:
            app_id (int): The Application ID.
        
        Returns:
            CreateBareMetalData: The current object with the Application ID set.
        """
        self._app_id = app_id
        return self

    def image_id(self, image_id: str) -> "CreateBareMetalData":
        """
        If supplied, deploy the instance using this [Application image_id](#operation/list-applications).

        Args:
            image_id (str): The Application image ID.
        
        Returns:
            CreateBareMetalData: The current object with the Application image ID set.
        """
        self._image_id = image_id
        return self

    def persistent_pxe(self, persistent_pxe: bool) -> "CreateBareMetalData":
        """
        Enable persistent PXE.

        Args:
            persistent_pxe (bool): Whether to enable persistent PXE.

        Returns:
            CreateBareMetalData: The current object with persistent PXE enabled/disabled.
        """
        self._persistent_pxe = persistent_pxe
        return self

    def attach_vpc2(self, attach_vpc2: List[str]) -> "CreateBareMetalData":
        """
        Set an array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.

        Args:
            attach_vpc2 (List[str]): The VPC IDs to attach.

        Returns:
            CreateBareMetalData: The current object with the VPC IDs to attach set.
        """
        self._attach_vpc2 = attach_vpc2
        return self

    def detach_vpc2(self, detach_vpc2: List[str]) -> "CreateBareMetalData":
        """
        Set an array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.

        Args:
            detach_vpc2 (List[str]): The VPC IDs to detach.

        Returns:
            CreateBareMetalData: The current object with the VPC IDs to detach set.
        """
        self._detach_vpc2 = detach_vpc2
        return self

    def enable_vpc2(self, enable_vpc2: bool) -> "CreateBareMetalData":
        """
        If `true`, VPC 2.0 support will be added to the new server.

        Args:
            enable_vpc2 (bool): Whether to enable VPC 2.0 support.

        Returns:
            CreateBareMetalData: The current object with VPC 2.0 support enabled/disabled.
        """
        self._enable_vpc2 = enable_vpc2
        return self

    def tags(self, tags: List[str]) -> "CreateBareMetalData":
        """
        Set the tags to apply to the instance.

        Args:
            tags (List[str]): The tags to apply.

        Returns:
            CreateBareMetalData: The current object with the tags set.
        """
        self._tags = tags
        return self

    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "CreateBareMetalData":
        """
        Set the Linux-only user scheme used for logging into this instance.

        Args:
            user_scheme (Literal["root", "limited"]): The user scheme.

        Returns:
            CreateBareMetalData: The current object with the user scheme set.
        """
        self._user_scheme = user_scheme
        return self

    def mdisk_mode(self, mdisk_mode: Literal["raid1", "jbod", "none"]) -> "CreateBareMetalData":
        """
        Set the RAID configuration used for the disks on this instance.

        Args:
            mdisk_mode (Literal["raid1", "jbod", "none"]): The RAID configuration.

        Returns:
            CreateBareMetalData: The current object with the RAID configuration set.
        """
        self._mdisk_mode = mdisk_mode
        return self
    
    def app_variables(self, app_variables: Dict[str, str]) -> "CreateBareMetalData":
        """
        Set the [app variable inputs](#operation/list-marketplace-app-variables) for configuring the marketplace app (name/value pairs).

        Args:
            app_variables (Dict[str, str]): The app variables.

        Returns:
            CreateBareMetalData: The current object with the app variables set.
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
            "script_id": self._script_id,
            "enable_ipv6": self._enable_ipv6,
            "sshkey_id": self._sshkey_id,
            "user_data": self._user_data,
            "label": self._label,
            "activation_email": self._activation_email,
            "hostname": self._hostname,
            "reserved_ipv4": self._reserved_ipv4,
            "os_id": self._os_id,
            "snapshot_id": self._snapshot_id,
            "app_id": self._app_id,
            "image_id": self._image_id,
            "persistent_pxe": self._persistent_pxe,
            "attach_vpc2": self._attach_vpc2,
            "detach_vpc2": self._detach_vpc2,
            "enable_vpc2": self._enable_vpc2,
            "tags": self._tags,
            "user_scheme": self._user_scheme,
            "mdisk_mode": self._mdisk_mode,
            "app_variables": self._app_variables,
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateBareMetalData:
    def __init__(self):
        """
        Data structure used for updating a Vultr Bare Metal instance.
        """
        self._user_data: Optional[str] = None
        self._label: Optional[str] = None
        self._os_id: Optional[int] = None
        self._app_id: Optional[int] = None
        self._image_id: Optional[str] = None
        self._enable_ipv6: Optional[bool] = None
        self._attach_vpc2: Optional[List[str]] = None
        self._detach_vpc2: Optional[List[str]] = None
        self._enable_vpc2: Optional[bool] = None
        self._tags: Optional[List[str]] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        self._mdisk_mode: Optional[Literal["raid1", "jbod", "none"]] = None

    def user_data(self, user_data: str) -> "UpdateBareMetalData":
        """
        Set the user-supplied, base64 encoded user data to attach to this instance.

        Args:
            user_data (str): The user data.

        Returns:
            UpdateBareMetalData: The current object with the user data set.
        """
        self._user_data = user_data
        return self

    def label(self, label: str) -> "UpdateBareMetalData":
        """
        Set the user-supplied label.

        Args:
            label (str): The label.

        Returns:
            UpdateBareMetalData: The current object with the label set.
        """
        self._label = label
        return self

    def os_id(self, os_id: int) -> "UpdateBareMetalData":
        """
        If supplied, reinstall the instance using this [Operating System id](#operation/list-os).

        Args:
            os_id (int): The Operating System ID.

        Returns:
            UpdateBareMetalData: The current object with the OS ID set.
        """
        self._os_id = os_id
        return self

    def app_id(self, app_id: int) -> "UpdateBareMetalData":
        """
        If supplied, reinstall the instance using this [Application id](#operation/list-applications).

        Args:
            app_id (int): The Application ID.

        Returns:
            UpdateBareMetalData: The current object with the Application ID set.
        """
        self._app_id = app_id
        return self

    def image_id(self, image_id: str) -> "UpdateBareMetalData":
        """
        If supplied, reinstall the instance using this [Application image_id](#operation/list-applications).

        Args:
            image_id (str): The Application image ID.

        Returns:
            UpdateBareMetalData: The current object with the Application image ID set.
        """
        self._image_id = image_id
        return self

    def enable_ipv6(self, enable_ipv6: bool) -> "UpdateBareMetalData":
        """
        Enable IPv6.

        Args:
            enable_ipv6 (bool): Whether to enable IPv6.

        Returns:
            UpdateBareMetalData: The current object with IPv6 enabled/disabled.
        """
        self._enable_ipv6 = enable_ipv6
        return self

    def attach_vpc2(self, attach_vpc2: List[str]) -> "UpdateBareMetalData":
        """
        Set an array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance. This parameter takes precedence over enable_vpc2.

        Args:
            attach_vpc2 (List[str]): The VPC IDs to attach.

        Returns:
            UpdateBareMetalData: The current object with the VPC IDs to attach set.
        """
        self._attach_vpc2 = attach_vpc2
        return self

    def detach_vpc2(self, detach_vpc2: List[str]) -> "UpdateBareMetalData":
        """
        Set an array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance. This parameter takes precedence over enable_vpc2.

        Args:
            detach_vpc2 (List[str]): The VPC IDs to detach.

        Returns:
            UpdateBareMetalData: The current object with the VPC IDs to detach set.
        """
        self._detach_vpc2 = detach_vpc2
        return self

    def enable_vpc2(self, enable_vpc2: bool) -> "UpdateBareMetalData":
        """
        If true, VPC 2.0 support will be added to the new server.

        Args:
            enable_vpc2 (bool): Whether to enable VPC 2.0 support.

        Returns:
            UpdateBareMetalData: The current object with VPC 2.0 support enabled/disabled.
        """
        self._enable_vpc2 = enable_vpc2
        return self

    def tags(self, tags: List[str]) -> "UpdateBareMetalData":
        """
        Set the tags to apply to the instance.

        Args:
            tags (List[str]): The tags to apply.

        Returns:
            UpdateBareMetalData: The current object with the tags set.
        """
        self._tags = tags
        return self

    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "UpdateBareMetalData":
        """
        Set the Linux-only user scheme used for logging into this instance. The instance must be reinstalled for this change to take effect.

        Args:
            user_scheme (Literal["root", "limited"]): The user scheme.

        Returns:
            UpdateBareMetalData: The current object with the user scheme set.
        """
        self._user_scheme = user_scheme
        return self

    def mdisk_mode(self, mdisk_mode: Literal["raid1", "jbod", "none"]) -> "UpdateBareMetalData":
        """
        Set the RAID configuration used for the disks on this instance. The instance must be reinstalled for this change to take effect.

        Args:
            mdisk_mode (Literal["raid1", "jbod", "none"]): The RAID configuration.

        Returns:
            UpdateBareMetalData: The current object with the RAID configuration set.
        """
        self._mdisk_mode = mdisk_mode
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "user_data": self._user_data,
            "label": self._label,
            "os_id": self._os_id,
            "app_id": self._app_id,
            "image_id": self._image_id,
            "enable_ipv6": self._enable_ipv6,
            "attach_vpc2": self._attach_vpc2,
            "detach_vpc2": self._detach_vpc2,
            "enable_vpc2": self._enable_vpc2,
            "tags": self._tags,
            "user_scheme": self._user_scheme,
            "mdisk_mode": self._mdisk_mode,
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateBareMetalReverseIPv4Data:
    def __init__(self, ip: str, reverse: str):
        """
        Data structure used for creating a reverse IPv4 entry for a Bare Metal Instance.

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

class CreateBareMetalReverseIPv6Data:
    def __init__(self, ip: str, reverse: str):
        """
        Data structure used for creating a reverse IPv6 entry for a Bare Metal Instance.

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
            "reverse": self._reverse,
        }