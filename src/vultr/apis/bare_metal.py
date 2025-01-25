from http import HTTPMethod
from typing import Optional, List, Literal, Dict

from proschedio import composer
from vultr import const, get_key
from vultr.structs import bare_metal

async def list_bare_metals(per_page: Optional[int], cursor: Optional[str]):
    """
    List all Bare Metal instances in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See Meta and pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BARE_METAL) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_bare_metal(data: bare_metal.CreateBareMetalData):
    """
    Create a new Bare Metal instance in a `region` with the desired `plan`.

    Args:
        data (CreateBareMetalData): The data to create the Bare Metal instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_bare_metal(baremetal_id: str):
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

async def update_bare_metal(baremetal_id: str, data: bare_metal.UpdateBareMetalData):
    """
    Update a Bare Metal instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        data (UpdateBareMetalData): The data to update the Bare Metal instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_bare_metal(baremetal_id: str):
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

async def get_bare_metal_ipv4(baremetal_id: str):
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

async def get_bare_metal_ipv6(baremetal_id: str):
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

async def create_bare_metal_reverse_ipv4(baremetal_id: str, data: bare_metal.CreateBareMetalReverseIPv4Data):
    """
    Create a reverse IPv4 entry for a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        data (CreateBareMetalReverseIPv4Data): The data to create the reverse IPv4 entry.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV4_REVERSE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def create_bare_metal_reverse_ipv6(baremetal_id: str, data: bare_metal.CreateBareMetalReverseIPv6Data):
    """
    Create a reverse IPv6 entry for a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        data (CreateBareMetalReverseIPv6Data): The data to create the reverse IPv6 entry.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV6_REVERSE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def set_bare_metal_reverse_ipv4(baremetal_id: str, ip: str):
    """
    Set a reverse DNS entry for an IPv4 address.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        ip (str): The IPv4 address.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METAL_IPV4_REVERSE_DEFAULT.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"ip": ip}) \
        .request()

async def delete_bare_metal_reverse_ipv6(baremetal_id: str, ipv6: str):
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

async def start_bare_metal(baremetal_id: str):
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

async def reboot_bare_metal(baremetal_id: str):
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

async def reinstall_bare_metal(baremetal_id: str, hostname: Optional[str]):
    """
    Reinstall the Bare Metal instance using an optional `hostname`.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        hostname (Optional[str]): The hostname to use when reinstalling this bare metal server.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BARE_METAL_REINSTALL.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json")
    
    if hostname is not None:
        request.set_body({"hostname": hostname})

    return await request.request()

async def halt_bare_metal(baremetal_id: str):
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

async def get_bare_metal_bandwidth(baremetal_id: str):
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

async def halt_bare_metals(baremetal_ids: List[str]):
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
        .set_body({"baremetal_ids": baremetal_ids}) \
        .request()

async def reboot_bare_metals(baremetal_ids: List[str]):
    """
    Reboot Bare Metals.

    Args:
        baremetal_ids (List[str]): Array of Bare Metal instance ids to reboot.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE.set_method(HTTPMethod.POST)) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"baremetal_ids": baremetal_ids}) \
        .request()

async def start_bare_metals(baremetal_ids: List[str]):
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
        .set_body({"baremetal_ids": baremetal_ids}) \
        .request()

async def get_bare_metal_user_data(baremetal_id: str):
    """
    Get the user-supplied, base64 encoded [user data] for a Bare Metal.

    Args:
        baremetal_id (str): The Bare Metal instance id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_USER_DATA.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_bare_metal_available_upgrades(baremetal_id: str, type: Optional[Literal["all", "applications", "os", "plans"]]):
    """
    Get available upgrades for a Bare Metal.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        type (Optional[Literal["all", "applications", "os", "plans"]]): Filter upgrade by type.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BARE_METALS_ID_AVAILABLE_UPGRADES.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")
    
    if type is not None:
        request.add_param("type", type)
    
    return await request.request()

async def get_bare_metal_vnc_url(baremetal_id: str):
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

async def attach_vpc_to_bare_metal(baremetal_id: str, vpc_id: str):
    """
    Attach a VPC Network to a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The [VPC ID](#operation/list-vpcs) to attach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id}) \
        .request()

async def detach_vpc_from_bare_metal(baremetal_id: str, vpc_id: str):
    """
    Detach a VPC Network from a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The [VPC ID](#operation/list-vpcs) to detach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id}) \
        .request()

async def list_bare_metal_vpcs(baremetal_id: str):
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

async def attach_vpc2_to_bare_metal(baremetal_id: str, vpc_id: Optional[str], ip_address: Optional[str]):
    """
    Attach a VPC 2.0 Network to a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (Optional[str]): The [VPC ID](#operation/list-vpc2) to attach.
        ip_address (Optional[str]): The IP address to use for this instance on the attached VPC 2.0 network.

    Returns:
        requests.Response: The response from the API.
    """
    body = {}
    
    if vpc_id is not None:
        body["vpc_id"] = vpc_id

    if ip_address is not None:
        body["ip_address"] = ip_address
    
    return await composer.Request(const.URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()

async def detach_vpc2_from_bare_metal(baremetal_id: str, vpc_id: str):
    """
    Detach a VPC 2.0 Network from a Bare Metal Instance.

    Args:
        baremetal_id (str): The Bare Metal instance id.
        vpc_id (str): The [VPC ID](#operation/list-vpc2) to detach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE.assign("baremetal-id", baremetal_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id}) \
        .request()

async def list_bare_metal_vpc2s(baremetal_id: str):
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