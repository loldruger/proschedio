import json
from typing import Optional

class BareMetalCreateData:
    def __init__(self, region: str, plan: str):
        self.region: str = region
        """
        string
        [Required] The Region id to create the instance.
        """
        self.plan: str = plan
        """
        string
        [Required] The Bare Metal plan id to use for this instance.
        """
        self.script_id: Optional[str] = None
        """
        string
        The Startup Script id to use for this instance.
        """
        self.enable_ipv6: Optional[bool] = None
        """
        boolean
        Enable IPv6.
        - true
        """
        self.sshkey_id: Optional[list[str]] = None
        """
        Array of strings
        The SSH Key id to install on this instance.
        """
        self.user_data: Optional[str] = None
        """
        string
        The user-supplied, base64 encoded user data for this instance.
        """
        self.label: Optional[str] = None
        """
        string
        The user-supplied label.
        """
        self.activation_email: Optional[bool] = None
        """
        boolean
        Notify by email after deployment.
        - true
        - false (default)
        """
        self.hostname: Optional[str] = None
        """
        string
        The user-supplied hostname to use when deploying this instance.
        """
        self.reserved_ipv4: Optional[str] = None
        """
        string
        The Reserved IP id for this instance.
        """
        self.os_id: Optional[int] = None
        """
        integer
        If supplied, deploy the instance using this Operating System id.
        """
        self.snapshot_id: Optional[str] = None
        """
        string
        If supplied, deploy the instance using this Snapshot ID.
        """
        self.app_id: Optional[int] = None
        """
        integer
        If supplied, deploy the instance using this Application id.
        """
        self.image_id: Optional[str] = None
        """
        string
        If supplied, deploy the instance using this Application image_id.
        """
        self.persistent_pxe: Optional[bool] = None
        """
        boolean
        Enable persistent PXE.
        - true
        - false (default)
        """
        self.attach_vpc2: Optional[list[str]] = None
        """
        Array of strings
        An array of VPC IDs to attach to this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`. Please choose one parameter.
        """
        self.detach_vpc2: Optional[list[str]] = None
        """
        Array of strings
        An array of VPC IDs to detach from this Bare Metal Instance. This parameter takes precedence over `enable_vpc2`.
        """
        self.enable_vpc2: Optional[bool] = None
        """
        boolean

        If true, VPC 2.0 support will be added to the new server.
        This parameter attaches a single VPC 2.0 netowrk. When no VPC 2.0 network exists in the region, it will be automatically created.
        If there are multiple VPC 2.0 networks in the instance's region, use attach_vpc2 instead to specify a VPC 2.0 network.

        """
        self.tags: Optional[list[str]] = None
        """
        Array of strings
        Tags to apply to the instance.
        """
        self.user_scheme: Optional[str] = None
        """
        string
        Linux-only: The user scheme used for logging into this instance. By default, the "root" user is configured. Alternatively, a limited user with sudo permissions can be selected.
        - root
        - limited
        """
        self.mdisk_mode: Optional[str] = None
        """
        string
        The RAID configuration used for the disks on this instance. The instance must be reinstalled for this change to take effect.
        - raid1
        - jbod
        - none (default)
        """
        self.app_variables: Optional[dict] = None
        """
        object
        The app variable inputs for configuring the marketplace app (name/value pairs).
        """

    def __str__(self) -> str:
        data = {
            "region": self.region,
            "plan": self.plan,
            "script_id": self.script_id,
            "enable_ipv6": self.enable_ipv6,
            "sshkey_id": self.sshkey_id,
            "user_data": self.user_data,
            "label": self.label,
            "activation_email": self.activation_email,
            "hostname": self.hostname,
            "reserved_ipv4": self.reserved_ipv4,
            "os_id": self.os_id,
            "snapshot_id": self.snapshot_id,
            "app_id": self.app_id,
            "image_id": self.image_id,
            "persistent_pxe": self.persistent_pxe,
            "attach_vpc2": self.attach_vpc2,
            "detach_vpc2": self.detach_vpc2,
            "enable_vpc2": self.enable_vpc2,
            "tags": self.tags,
            "user_scheme": self.user_scheme,
            "mdisk_mode": self.mdisk_mode,
            "app_variables": self.app_variables,
        }
        filtered_data = {k: v for k, v in data.items() if v is not None}
        return json.dumps(filtered_data)

    def to_json(self) -> dict:
        return json.loads(str(self))

class BareMetalUpdateData:
    def __init__(self):
        self.user_data: Optional[str] = None
        self.label: Optional[str] = None
        self.os_id: Optional[int] = None
        self.app_id: Optional[int] = None
        self.image_id: Optional[int] = None
        self.enable_ipv6: Optional[bool] = None
        self.attach_vpc2: Optional[list[str]] = None
        self.detach_vpc2: Optional[list[str]] = None
        self.enable_vpc2: Optional[bool] = None
        self.tags: Optional[list[str]] = None
        self.user_scheme: Optional[str] = None
        self.mdisk_mode: Optional[str] = None
    
    def __str__(self) -> str:
        data = {
            "user_data": self.user_data,
            "label": self.label,
            "os_id": self.os_id,
            "app_id": self.app_id,
            "image_id": self.image_id,
            "enable_ipv6": self.enable_ipv6,
            "attach_vpc2": self.attach_vpc2,
            "detach_vpc2": self.detach_vpc2,
            "enable_vpc2": self.enable_vpc2,
            "tags": self.tags,
            "user_scheme": self.user_scheme,
            "mdisk_mode": self.mdisk_mode,
        }
        filtered_data = {k: v for k, v in data.items() if v is not None}
        return json.dumps(filtered_data)
    
    def to_json(self) -> dict:
        return json.loads(str(self))