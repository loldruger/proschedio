import json
from typing import Optional, List, Literal
from typing_extensions import deprecated

from src.proschedio.request import Request

class ListInstancesData:
    """
    Data structure used for filtering the list of Vultr VPS Instances.
    """
    def __init__(self):
        self._per_page: Optional[int] = None
        self._cursor: Optional[str] = None
        self._tag: Optional[str] = None # Deprecated
        self._label: Optional[str] = None
        self._main_ip: Optional[str] = None
        self._region: Optional[str] = None
        self._firewall_group_id: Optional[str] = None
        self._hostname: Optional[str] = None
        self._show_pending_charges: Optional[bool] = None

    # --- Builder methods --- 
    def per_page(self, per_page: int) -> "ListInstancesData":
        self._per_page = per_page
        return self

    def cursor(self, cursor: str) -> "ListInstancesData":
        self._cursor = cursor
        return self

    @deprecated("The 'tag' parameter is deprecated, use 'label' instead.")
    def tag(self, tag: str) -> "ListInstancesData": # Deprecated
        self._tag = tag
        return self

    def label(self, label: str) -> "ListInstancesData":
        self._label = label
        return self

    def main_ip(self, main_ip: str) -> "ListInstancesData":
        self._main_ip = main_ip
        return self

    def region(self, region: str) -> "ListInstancesData":
        self._region = region
        return self

    def firewall_group_id(self, firewall_group_id: str) -> "ListInstancesData":
        self._firewall_group_id = firewall_group_id
        return self

    def hostname(self, hostname: str) -> "ListInstancesData":
        self._hostname = hostname
        return self

    def show_pending_charges(self, show_pending_charges: bool) -> "ListInstancesData":
        self._show_pending_charges = show_pending_charges
        return self
    
    # --- Parameter application --- 
    def apply_params(self, request: Request):
        """
        Applies the parameters from this data structure to a given request object.
        (Assumes request object has an add_param method)
        """
        if self._per_page is not None: request.add_param("per_page", str(self._per_page))
        if self._cursor is not None: request.add_param("cursor", self._cursor)
        if self._tag is not None: request.add_param("tag", self._tag)
        if self._label is not None: request.add_param("label", self._label)
        if self._main_ip is not None: request.add_param("main_ip", self._main_ip)
        if self._region is not None: request.add_param("region", self._region)
        if self._firewall_group_id is not None: request.add_param("firewall_group_id", self._firewall_group_id)
        if self._hostname is not None: request.add_param("hostname", self._hostname)
        if self._show_pending_charges is not None: request.add_param("show_pending_charges", str(self._show_pending_charges))
        return request
    
class CreateInstanceData:
    """
    Data structure used for creating a Vultr VPS Instance.
    """
    def __init__(self, region: str, plan: str):
        self._region: str = region
        self._plan: str = plan
        self._os_id: Optional[int] = None
        self._ipxe_chain_url: Optional[str] = None
        self._iso_id: Optional[str] = None
        self._script_id: Optional[str] = None
        self._snapshot_id: Optional[str] = None
        self._enable_ipv6: Optional[bool] = None
        self._disable_public_ipv4: Optional[bool] = None
        self._attach_vpc: Optional[List[str]] = None
        self._label: Optional[str] = None
        self._sshkey_id: Optional[List[str]] = None
        self._backups: Optional[Literal["enabled", "disabled"]] = None
        self._app_id: Optional[int] = None
        self._image_id: Optional[str] = None
        self._user_data: Optional[str] = None
        self._ddos_protection: Optional[bool] = None
        self._activation_email: Optional[bool] = None
        self._hostname: Optional[str] = None
        self._firewall_group_id: Optional[str] = None
        self._reserved_ipv4: Optional[str] = None
        self._enable_vpc: Optional[bool] = None
        self._tags: Optional[List[str]] = None
        # Deprecated fields omitted: attach_private_network, attach_vpc2, tag, enable_private_network, enable_vpc2
        # Fields potentially added by user request: user_scheme, app_variables
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        # self._app_variables: Optional[dict] = None

    # --- Builder methods --- 
    def os_id(self, os_id: int) -> "CreateInstanceData":
        self._os_id = os_id
        return self
    def ipxe_chain_url(self, ipxe_chain_url: str) -> "CreateInstanceData":
        self._ipxe_chain_url = ipxe_chain_url
        return self
    def iso_id(self, iso_id: str) -> "CreateInstanceData":
        self._iso_id = iso_id
        return self
    def script_id(self, script_id: str) -> "CreateInstanceData":
        self._script_id = script_id
        return self
    def snapshot_id(self, snapshot_id: str) -> "CreateInstanceData":
        self._snapshot_id = snapshot_id
        return self
    def enable_ipv6(self, enable_ipv6: bool) -> "CreateInstanceData":
        self._enable_ipv6 = enable_ipv6
        return self
    def disable_public_ipv4(self, disable_public_ipv4: bool) -> "CreateInstanceData":
        self._disable_public_ipv4 = disable_public_ipv4
        return self
    def attach_vpc(self, attach_vpc: List[str]) -> "CreateInstanceData":
        self._attach_vpc = attach_vpc
        return self
    def label(self, label: str) -> "CreateInstanceData":
        self._label = label
        return self
    def sshkey_id(self, sshkey_id: List[str]) -> "CreateInstanceData":
        self._sshkey_id = sshkey_id
        return self
    def backups(self, backups: Literal["enabled", "disabled"]) -> "CreateInstanceData":
        self._backups = backups
        return self
    def app_id(self, app_id: int) -> "CreateInstanceData":
        self._app_id = app_id
        return self
    def image_id(self, image_id: str) -> "CreateInstanceData":
        self._image_id = image_id
        return self
    def user_data(self, user_data: str) -> "CreateInstanceData":
        self._user_data = user_data
        return self
    def ddos_protection(self, ddos_protection: bool) -> "CreateInstanceData":
        self._ddos_protection = ddos_protection
        return self
    def activation_email(self, activation_email: bool) -> "CreateInstanceData":
        self._activation_email = activation_email
        return self
    def hostname(self, hostname: str) -> "CreateInstanceData":
        self._hostname = hostname
        return self
    def firewall_group_id(self, firewall_group_id: str) -> "CreateInstanceData":
        self._firewall_group_id = firewall_group_id
        return self
    def reserved_ipv4(self, reserved_ipv4: str) -> "CreateInstanceData":
        self._reserved_ipv4 = reserved_ipv4
        return self
    def enable_vpc(self, enable_vpc: bool) -> "CreateInstanceData":
        self._enable_vpc = enable_vpc
        return self
    def tags(self, tags: List[str]) -> "CreateInstanceData":
        self._tags = tags
        return self
    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "CreateInstanceData":
        self._user_scheme = user_scheme
        return self
    # def app_variables(self, app_variables: dict) -> "CreateInstanceData":
    #     self._app_variables = app_variables
    #     return self

    # --- JSON conversion --- 
    def to_json(self) -> 'str':
        """
        Convert the data structure to a JSON format for Vultr API requests.
        """
        return json.dumps({
            "region": self._region,
            "plan": self._plan,
            "os_id": self._os_id,
            "ipxe_chain_url": self._ipxe_chain_url,
            "iso_id": self._iso_id,
            "script_id": self._script_id,
            "snapshot_id": self._snapshot_id,
            "enable_ipv6": self._enable_ipv6,
            "disable_public_ipv4": self._disable_public_ipv4,
            "attach_vpc": self._attach_vpc,
            "label": self._label,
            "sshkey_id": self._sshkey_id,
            "backups": self._backups,
            "app_id": self._app_id,
            "image_id": self._image_id,
            "user_data": self._user_data,
            "ddos_protection": self._ddos_protection,
            "activation_email": self._activation_email,
            "hostname": self._hostname,
            "firewall_group_id": self._firewall_group_id,
            "reserved_ipv4": self._reserved_ipv4,
            "enable_vpc": self._enable_vpc,
            "tags": self._tags,
            "user_scheme": self._user_scheme,
            # "app_variables": self._app_variables,
        })

class UpdateInstanceData:
    """
    Data structure used for updating a Vultr VPS Instance.
    All fields are optional.
    """
    def __init__(self):
        self._label: Optional[str] = None
        self._user_scheme: Optional[Literal["root", "limited"]] = None
        self._enable_ipv6: Optional[bool] = None
        self._attach_vpc: Optional[List[str]] = None
        self._detach_vpc: Optional[List[str]] = None
        self._attach_vpc2: Optional[List[str]] = None # Deprecated
        self._detach_vpc2: Optional[List[str]] = None # Deprecated
        self._os_id: Optional[int] = None
        self._app_id: Optional[int] = None
        self._image_id: Optional[str] = None
        self._firewall_group_id: Optional[str] = None
        self._plan: Optional[str] = None
        self._tags: Optional[List[str]] = None
        self._backups: Optional[Literal["enabled", "disabled"]] = None
        self._hostname: Optional[str] = None

    # --- Builder methods --- 
    def label(self, label: str) -> "UpdateInstanceData":
        self._label = label
        return self
    def user_scheme(self, user_scheme: Literal["root", "limited"]) -> "UpdateInstanceData":
        self._user_scheme = user_scheme
        return self
    def enable_ipv6(self, enable_ipv6: bool) -> "UpdateInstanceData":
        self._enable_ipv6 = enable_ipv6
        return self
    def attach_vpc(self, attach_vpc: List[str]) -> "UpdateInstanceData":
        self._attach_vpc = attach_vpc
        return self
    def detach_vpc(self, detach_vpc: List[str]) -> "UpdateInstanceData":
        self._detach_vpc = detach_vpc
        return self
    def os_id(self, os_id: int) -> "UpdateInstanceData":
        self._os_id = os_id
        return self
    def app_id(self, app_id: int) -> "UpdateInstanceData":
        self._app_id = app_id
        return self
    def image_id(self, image_id: str) -> "UpdateInstanceData":
        self._image_id = image_id
        return self
    def firewall_group_id(self, firewall_group_id: str) -> "UpdateInstanceData":
        self._firewall_group_id = firewall_group_id
        return self
    def plan(self, plan: str) -> "UpdateInstanceData":
        self._plan = plan
        return self
    def tags(self, tags: List[str]) -> "UpdateInstanceData":
        self._tags = tags
        return self
    def backups(self, backups: Literal["enabled", "disabled"]) -> "UpdateInstanceData":
        self._backups = backups
        return self
    def hostname(self, hostname: str) -> "UpdateInstanceData":
        self._hostname = hostname
        return self

    # --- JSON conversion --- 
    def to_json(self) -> str:
        """
        Convert the data structure to a JSON format for Vultr API requests.
        """
        return json.dumps({
            "label": self._label,
            "user_scheme": self._user_scheme,
            "enable_ipv6": self._enable_ipv6,
            "attach_vpc": self._attach_vpc,
            "detach_vpc": self._detach_vpc,
            "os_id": self._os_id,
            "app_id": self._app_id,
            "image_id": self._image_id,
            "firewall_group_id": self._firewall_group_id,
            "plan": self._plan,
            "tags": self._tags,
            "backups": self._backups,
            "hostname": self._hostname,
        })

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

    def to_json(self) -> str:
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests,
        including only non-None optional fields.

        Returns:
            Dict[str, Union[str, int]]: The data in JSON format.
        """

        return json.dumps({
            "type": self._type,
            "hour": self._hour,
            "dow": self._dow,
            "dom": self._dom
        })

# Add other data structures if needed, e.g., for reverse DNS
class SetInstanceReverseIPv4Data:
    """
    Data structure for setting default reverse DNS for an IPv4 address.
    """
    def __init__(self, ip: str):
        self._ip = ip

    def to_json(self) -> str:
        return json.dumps({"ip": self._ip})
