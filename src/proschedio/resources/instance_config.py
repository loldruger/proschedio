from typing import Literal, Optional, TypedDict, List

class VultrInstanceConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr VPS Instance.
    """
    os_id: Optional[int]
    ipxe_chain_url: Optional[str]
    iso_id: Optional[str]
    script_id: Optional[str]
    snapshot_id: Optional[str]
    enable_ipv6: Optional[bool]
    disable_public_ipv4: Optional[bool]
    attach_vpc: Optional[List[str]]
    label: Optional[str]
    sshkey_id: Optional[List[str]]
    backups: Optional[Literal["enabled", "disabled"]]
    app_id: Optional[int]
    image_id: Optional[str]
    user_data: Optional[str]
    ddos_protection: Optional[bool]
    activation_email: Optional[bool]
    hostname: Optional[str]
    firewall_group_id: Optional[str]
    reserved_ipv4: Optional[str]
    enable_vpc: Optional[bool]
    tags: Optional[List[str]]
    # Deprecated fields omitted: attach_private_network, attach_vpc2, tag, enable_private_network, enable_vpc2
    # Fields potentially added by user request: user_scheme, app_variables
    user_scheme: Optional[Literal["root", "limited"]]
    # self._app_variables: Optional[dict] = None
    wait_for_ready: Optional[bool]
    wait_timeout: Optional[int]
    wait_interval: Optional[int]