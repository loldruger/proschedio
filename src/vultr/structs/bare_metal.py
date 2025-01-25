import json
from typing import Final, Optional, Literal
from enum import Enum, StrEnum

class AvailableUpgradeType(StrEnum):
    ALL: Final[str] = "all"
    Application: Final[str]  = "application"
    Os: Final[str]  = "os"

class CreateData:
    def __init__(self, region: str, plan: str):
        """
        :param region: The Region id to create the instance.
        :param plan: The [Bare Metal plan id](#operation/list-metal-plans) to use for this instance.
        """
        self._region: str = region
        self._plan: str = plan
        self._script_id: Optional[str] = None
        self._enable_ipv6: Optional[bool] = None
        self._sshkey_id: Optional[list[str]] = None
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
        self._attach_vpc2: Optional[list[str]] = None
        self._detach_vpc2: Optional[list[str]] = None
        self._enable_vpc2: Optional[bool] = None
        self._tags: Optional[list[str]] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        self._mdisk_mode: Optional[Literal["raid1", "jbod", "none"]] = None
        self._app_variables: Optional[dict] = None

    def __str__(self) -> str:
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
        filtered_data = {k: v for k, v in data.items() if v is not None}
        return json.dumps(filtered_data)

    def script_id(self, script_id: str) -> "CreateData":
        """
        The [Startup Script id](#operation/list-startup-scripts) to use for this instance.
        """
        self._script_id = script_id
        return self
    
    def enable_ipv6(self, enable_ipv6: bool) -> "CreateData":
        """
        Enable IPv6.
        - true
        """
        self._enable_ipv6 = enable_ipv6
        return self
    
    def sshkey_id(self, sshkey_id: list[str]) -> "CreateData":
        """
        The [SSH Key id](#operation/list-ssh-keys) to install on this instance.
        """
        self._sshkey_id = sshkey_id
        return self
    
    def user_data(self, user_data: str) -> "CreateData":
        """
        The user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for this Instance.
        """
        self._user_data = user_data
        return self
    
    def label(self, label: str) -> "CreateData":
        """
        The user-supplied label.
        """
        self._label = label
        return self
    
    def activation_email(self, activation_email: bool) -> "CreateData":
        """
        Notify by email after deployment.
        - true
        - false (default)
        """
        self._activation_email = activation_email
        return self
    
    def hostname(self, hostname: str) -> "CreateData":
        """
        The user-supplied hostname to use when deploying this instance.
        """
        self._hostname = hostname
        return self
    
    def reserved_ipv4(self, reserved_ipv4: str) -> "CreateData":
        """
        The [Reserved IP id](#operation/list-reserved-ips) for this instance.
        """
        self._reserved_ipv4 = reserved_ipv4
        return self
    
    def os_id(self, os_id: int) -> "CreateData":
        """
        If supplied, deploy the instance using this [Operating System id](#operation/list-os).
        """
        self._os_id = os_id
        return self
    
    def snapshot_id(self, snapshot_id: str) -> "CreateData":
        """
        If supplied, deploy the instance using this [Snapshot ID](#operation/list-snapshots).
        """
        self._snapshot_id = snapshot_id
        return self
    
    def app_id(self, app_id: int) -> "CreateData":
        """
        If supplied, deploy the instance using this [Application id](#operation/list-applications).
        """
        self._app_id = app_id
        return self
    
    def image_id(self, image_id: str) -> "CreateData":
        """
        If supplied, deploy the instance using this [Application image_id](#operation/list-applications).
        """
        self._image_id = image_id
        return self
    
    def persistent_pxe(self, persistent_pxe: bool) -> "CreateData":
        """
        Enable persistent PXE.
        - true
        - false (default)
        """
        self._persistent_pxe = persistent_pxe
        return self
    
    def attach_vpc2(self, attach_vpc2: list[str]) -> "CreateData":
        """
        An array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.  Please choose one parameter.
        """
        self._attach_vpc2 = attach_vpc2
        return self
    
    def detach_vpc2(self, detach_vpc2: list[str]) -> "CreateData":
        """
        An array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.
        """
        self._detach_vpc2 = detach_vpc2
        return self
    
    def enable_vpc2(self, enable_vpc2: bool) -> "CreateData":
        """
        If `true`, VPC 2.0 support will be added to the new server.
        This parameter attaches a single VPC 2.0 netowrk. When no VPC 2.0 network exists in the region, it will be automatically created.
        If there are multiple VPC 2.0 networks in the instance's region, use `attach_vpc2` instead to specify a VPC 2.0 network.

        """
        self._enable_vpc2 = enable_vpc2
        return self
    
    def tags(self, tags: list[str]) -> "CreateData":
        """
        Tags to apply to the instance.
        """
        self._tags = tags
        return self
    
    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "CreateData":
        """
        Linux-only: The user scheme used for logging into this instance. By default, the "root" user is configured. Alternatively, a limited user with sudo permissions can be selected.
        - root
        - limited
        """
        self._user_scheme = user_scheme
        return self
    
    def mdisk_mode(self, mdisk_mode: Literal["raid1", "jbod", "none"]) -> "CreateData":
        """
        The RAID configuration used for the disks on this instance. The instance must be reinstalled for this change to take effect.
        - raid1
        - jbod
        - none (default)
        """
        self._mdisk_mode = mdisk_mode
        return self
    
    def app_variables(self, app_variables: dict) -> "CreateData":
        """
        The app variable inputs for configuring the marketplace app (name/value pairs).
        """
        self._app_variables = app_variables
        return self
    
    def to_json(self) -> dict:
        return json.loads(str(self))

class UpdateData:
    def __init__(self):
        self._user_data: Optional[str] = None
        self._label: Optional[str] = None
        self._os_id: Optional[int] = None
        self._app_id: Optional[int] = None
        self._image_id: Optional[int] = None
        self._enable_ipv6: Optional[bool] = None
        self._attach_vpc2: Optional[list[str]] = None
        self._detach_vpc2: Optional[list[str]] = None
        self._enable_vpc2: Optional[bool] = None
        self._tags: Optional[list[str]] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        self._mdisk_mode: Optional[str] = None

    def user_data(self, user_data: str) -> "UpdateData":
        """
        The user-supplied, base64 encoded user data to attach to this instance.
        """
        self._user_data = user_data
        return self
    
    def label(self, label: str) -> "UpdateData":
        """
        The user-supplied label.
        """
        self._label = label
        return self
    
    def os_id(self, os_id: int) -> "UpdateData":
        """
        If supplied, reinstall the instance using this [Operating System id](#operation/list-os).
        """
        self._os_id = os_id
        return self
    
    def app_id(self, app_id: int) -> "UpdateData":
        """
        If supplied, reinstall the instance using this [Application id](#operation/list-applications).
        """
        self._app_id = app_id
        return self
    
    def image_id(self, image_id: int) -> "UpdateData":
        """
        If supplied, reinstall the instance using this [Application image_id](#operation/list-applications).
        """
        self._image_id = image_id
        return self
    
    def enable_ipv6(self, enable_ipv6: bool) -> "UpdateData":
        """
        Enable IPv6.
        * true
        """
        self._enable_ipv6 = enable_ipv6
        return self
    
    def attach_vpc2(self, attach_vpc2: list[str]) -> "UpdateData":
        """
        An array of [VPC IDs](#operation/list-vpc2) to attach to this Bare Metal Instance. This parameter takes precedence over enable_vpc2. Please choose one parameter.
        """
        self._attach_vpc2 = attach_vpc2
        return self
    
    def detach_vpc2(self, detach_vpc2: list[str]) -> "UpdateData":
        """
        An array of [VPC IDs](#operation/list-vpc2) to detach from this Bare Metal Instance. This parameter takes precedence over enable_vpc2.
        """
        self._detach_vpc2 = detach_vpc2
        return self
    
    def enable_vpc2(self, enable_vpc2: bool) -> "UpdateData":
        """
        If true, VPC 2.0 support will be added to the new server. This parameter attaches a single VPC 2.0 netowrk. When no VPC 2.0 network exists in the region, it will be automatically created. If there are multiple VPC 2.0 networks in the instance's region, use attach_vpc2 instead to specify a VPC 2.0 network.
        """
        self._enable_vpc2 = enable_vpc2
        return self

    def tags(self, tags: list[str]) -> "UpdateData":
        """
        Tags to apply to the instance.
        """
        self._tags = tags
        return self
    
    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "UpdateData":
        """
        Linux-only: The user scheme used for logging into this instance. The instance must be reinstalled for this change to take effect. 
        * root 
        * limited
        """
        self._user_scheme = user_scheme
        return self
    
    def mdisk_mode(self, mdisk_mode: Literal["raid1", "jbod", "none"]) -> "UpdateData":
        """
        The RAID configuration used for the disks on this instance. The instance must be reinstalled for this change to take effect. 
        * raid1 
        * jbod 
        * none(default)
        """
        self._mdisk_mode = mdisk_mode
        return self

    def __str__(self) -> str:
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
        filtered_data = {k: v for k, v in data.items() if v is not None}
        return json.dumps(filtered_data)
    
    def to_json(self) -> dict:
        return json.loads(str(self))

