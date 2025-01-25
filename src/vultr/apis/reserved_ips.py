from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import const, get_key


async def list_reserved_ips(per_page: Optional[int] = None, cursor: Optional[str] = None):
    """
    List all Reserved IPs in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_RESERVED_IP) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_reserved_ip(data: CreateReservedIpData):
    """
    Create a new Reserved IP. The `region` and `ip_type` attributes are required.

    Args:
        data (CreateReservedIpData): The data to create the Reserved IP.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_reserved_ip(reserved_ip: str):
    """
    Get information about a Reserved IP.

    Args:
        reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP_ID.assign("reserved-ip", reserved_ip)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_reserved_ip(reserved_ip: str, label: str):
    """
    Update information on a Reserved IP.

    Args:
        reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).
        label (str): The user-supplied label.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP_ID.assign("reserved-ip", reserved_ip)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"label": label}) \
        .request()


async def delete_reserved_ip(reserved_ip: str):
    """
    Delete a Reserved IP.

    Args:
        reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP_ID.assign("reserved-ip", reserved_ip)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def attach_reserved_ip(reserved_ip: str, instance_id: str):
    """
    Attach a Reserved IP to an compute instance or a baremetal instance - `instance_id`.

    Args:
        reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).
        instance_id (str): Attach the Reserved IP to a [Compute Instance id](#operation/list-instances) or a [Bare Metal Instance id](#operation/list-baremetals).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP_ATTACH.assign("reserved-ip", reserved_ip)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"instance_id": instance_id}) \
        .request()


async def detach_reserved_ip(reserved_ip: str):
    """
    Detach a Reserved IP.

    Args:
        reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP_DETACH.assign("reserved-ip", reserved_ip)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def convert_to_reserved_ip(data: ConvertIpToReservedIpData):
    """
    Convert the `ip_address` of an existing [instance](#operation/list-instances) into a Reserved IP.

    Args:
        data (ConvertIpToReservedIpData): The data to convert the IP address.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_RESERVED_IP_CONVERT) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()