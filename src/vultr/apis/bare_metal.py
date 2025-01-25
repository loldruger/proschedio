from http import HTTPMethod
from typing import List, Optional

from proschedio import composer
from vultr import const, get_key
import vultr.structs.bare_metal as bare_metal


async def get_list(per_page: int, cursor: str):
    """
    List all Bare Metal instances in your account.

    Args:
        per_page (int): Number of items requested per page. Default is 100 and Max is 500.
        cursor (str): Cursor for paging. See Meta and pagination.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_param("per_page", per_page) \
        .add_param("cursor", cursor) \
        .request()


async def create(data: bare_metal.CreateData):
    """
    Create a new Bare Metal instance.

    Args:
        data (bare_metal.CreateData): The data to create the instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_by_id(baremetal_id: str):
    """
    Get information for a Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_by_id(baremetal_id: str, data: bare_metal.UpdateData):
    """
    Update a Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        data (bare_metal.UpdateData): The data to update the instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def delete_by_id(baremetal_id: str):
    """
    Delete a Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_ipv4_addresses_by_id(baremetal_id: str):
    """
    Get the IPv4 information for the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV4.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_ipv6_addresses_by_id(baremetal_id: str):
    """
    Get the IPv6 information for the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV6.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_ipv4_reverse_by_id(baremetal_id: str, ip: str, reverse: str):
    """
    Create a reverse IPv4 entry for a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        ip (str): The IPv4 address.
        reverse (str): The IPv4 reverse entry.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV4_REVERSE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "ip": ip,
            "reverse": reverse
        }) \
        .request()


async def create_ipv6_reverse_by_id(baremetal_id: str, ip: str, reverse: str):
    """
    Create a reverse IPv6 entry for a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        ip (str): The IPv6 address in full, expanded format.
        reverse (str): The IPv6 reverse entry.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV6_REVERSE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "ip": ip,
            "reverse": reverse
        }) \
        .request()

async def set_default_reverse_dns_by_id(baremetal_id: str, ipv4: str):
    """
    Set a reverse DNS entry for an IPv4 address.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        ipv4 (str): The IPv4 address.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV4_REVERSE_DEFAULT.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "ip": ipv4
        }) \
        .request()


async def delete_ipv6_reverse_by_id(baremetal_id: str, ipv6: str):
    """
    Delete the reverse IPv6 for a Bare metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        ipv6 (str): The IPv6 address.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV6_REVERSE_IPV6.assign("baremetal-id", baremetal_id).assign("ipv6", ipv6)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def start_by_id(baremetal_id: str):
    """
    Start the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_START.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def reboot_by_id(baremetal_id: str):
    """
    Reboot the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_REBOOT.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def reinstall_by_id(baremetal_id: str, hostname: Optional[str]):
    """
    Reinstall the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        hostname (Optional[str]): The hostname to use when reinstalling this bare metal server.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BARE_METAL_REINSTALL.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if hostname:
        request.add_header("Content-Type", "application/json") \
            .set_body({
                "hostname": hostname
            })

    return await request.request()


async def halt_by_id(baremetal_id: str):
    """
    Halt the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_HALT.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_bandwidth_by_id(baremetal_id: str):
    """
    Get bandwidth information for the Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_BANDWIDTH.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def start_by_ids(baremetal_ids: List[str]):
    """
    Start Bare Metals.

    Args:
        baremetal_ids (List[str]): Array of Bare Metal instance ids to start.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_START) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "baremetal_ids": baremetal_ids
        }) \
        .request()


async def reboot_by_ids(baremetal_ids: List[str]):
    """
    Reboot Bare Metals.

    Args:
        baremetal_ids (List[str]): Array of Bare Metal instance ids to reboot.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_REBOOT) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "baremetal_ids": baremetal_ids
        }) \
        .request()


async def halt_by_ids(baremetal_ids: List[str]):
    """
    Halt Bare Metals.

    Args:
        baremetal_ids (List[str]): Array of Bare Metal instance ids to halt.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_HALT) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "baremetal_ids": baremetal_ids
        }) \
        .request()

async def get_user_data_by_id(baremetal_id: str):
    """
    Get the user-supplied, base64 encoded user data for a Bare Metal.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_USER_DATA.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_available_upgrades_by_id(baremetal_id: str, type: Optional[bare_metal.AvailableUpgradeType]):
    """
    Get available upgrades for a Bare Metal.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        type (Optional[bare_metal.AvailableUpgradeType]): Filter upgrade by type.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BARE_METALS_ID_AVAILABLE_UPGRADES.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if type:
        request.add_param("type", type.value)

    return await request.request()


async def get_vnc_url_by_id(baremetal_id: str):
    """
    Get the VNC URL for a Bare Metal.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_ID_VNC.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def attach_vpc_by_id(baremetal_id: str, vpc_id: str):
    """
    Attach a VPC Network to a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The VPC ID to attach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "vpc_id": vpc_id
        }) \
        .request()


async def detach_vpc_by_id(baremetal_id: str, vpc_id: str):
    """
    Detach a VPC Network from an Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The VPC ID to detach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "vpc_id": vpc_id
        }) \
        .request()


async def get_vpc_attached_list(baremetal_id: str):
    """
    List the VPC networks for a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_VPCS.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def attach_vpc2(baremetal_id: str, vpc_id: str, ip_address: Optional[str]):
    """
    Attach a VPC 2.0 Network to a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The VPC ID to attach.
        ip_address (Optional[str]): The IP address to use for this instance on the attached VPC 2.0 network.

    Returns:
        requests.Response: The response from the API.
    """
    body = {
        "vpc_id": vpc_id
    }
    if ip_address:
        body["ip_address"] = ip_address

    return await composer.Request(const.URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()


async def detach_vpc2(baremetal_id: str, vpc_id: str):
    """
    Detach a VPC 2.0 Network from an Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The VPC ID to detach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            "vpc_id": vpc_id
        }) \
        .request()


async def get_vpc2_attached_list(baremetal_id: str):
    """
    List the VPC 2.0 networks for a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_VPCS2.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()