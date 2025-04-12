import json
from typing import Literal
from typing_extensions import deprecated

from src.proschedio.request import Request

class ListInstancesData:
    """
    Data structure used for filtering the list of Vultr VPS Instances.
    """
    def __init__(self):
        self._per_page: int | None = None
        self._cursor: str | None = None
        self._tag: str | None = None # Deprecated
        self._label: str | None = None
        self._main_ip: str | None = None
        self._region: str | None = None
        self._firewall_group_id: str | None = None
        self._hostname: str | None = None
        self._show_pending_charges: bool | None = None

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
    
class UpdateInstanceData:
    """
    Data structure used for updating a Vultr VPS Instance.
    All fields are optional.
    """
    def __init__(self):
        self._label: str | None = None
        self._user_scheme: Literal["root", "limited"] | None = None
        self._enable_ipv6: bool | None = None
        self._attach_vpc: list[str] | None = None
        self._detach_vpc: list[str] | None = None
        self._attach_vpc2: list[str] | None = None # Deprecated
        self._detach_vpc2: list[str] | None = None # Deprecated
        self._os_id: int | None = None
        self._app_id: int | None = None
        self._image_id: str | None = None
        self._firewall_group_id: str | None = None
        self._plan: str | None = None
        self._tags: list[str] | None = None
        self._backups: Literal["enabled", "disabled"] | None = None
        self._hostname: str | None = None

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
    def attach_vpc(self, attach_vpc: list[str] | None) -> "UpdateInstanceData":
        self._attach_vpc = attach_vpc
        return self
    def detach_vpc(self, detach_vpc: list[str] | None) -> "UpdateInstanceData":
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
    def tags(self, tags: list[str]) -> "UpdateInstanceData":
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
        self._hour: int | None = None
        self._dow: int | None = None
        self._dom: int | None = None

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
