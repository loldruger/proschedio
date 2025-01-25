from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import const, get_key


async def list_vpcs(per_page: Optional[int] = None, cursor: Optional[str] = None):
    """
    Get a list of all VPCs in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_VPC_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_vpc(data: CreateVpcData):
    """
    Create a new VPC in a `region`. VPCs should use [RFC1918 private address space](https://tools.ietf.org/html/rfc1918).

    Args:
        data (CreateVpcData): The data to create the VPC.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VPC_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_vpc(vpc_id: str):
    """
    Get information about a VPC.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VPC_ID.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_vpc(vpc_id: str, description: str):
    """
    Update information for a VPC.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).
        description (str): The VPC description.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VPC_ID.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"description": description}) \
        .request()


async def delete_vpc(vpc_id: str):
    """
    Delete a VPC.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VPC_ID.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()