from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import vpc2


async def list_vpc2s(per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of all VPC 2.0 networks in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_VPC2_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_vpc2(data: vpc2.CreateVpc2Data):
    """
    Create a new VPC 2.0 network in a `region`.

    Args:
        data (CreateVpc2Data): The data to create the VPC 2.0 network.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_VPC2_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_vpc2(vpc_id: str):
    """
    Get information about a VPC 2.0 network.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_VPC2_ID.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_vpc2(vpc_id: str, description: str):
    """
    Update information for a VPC 2.0 network.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).
        description (str): The VPC description.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_VPC2_ID.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"description": description}) \
        .request()


async def delete_vpc2(vpc_id: str):
    """
    Delete a VPC 2.0 network.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_VPC2_ID.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_vpc2_nodes(vpc_id: str, per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of nodes attached to a VPC 2.0 network.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_VPC2_NODES.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")
    
    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def attach_vpc2_nodes(vpc_id: str, data: vpc2.AttachDetachVpc2NodesData):
    """
    Attach nodes to a VPC 2.0 network.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).
        data (AttachDetachVpc2NodesData): The data to attach nodes to the VPC 2.0 network.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_VPC2_ATTACH_NODES.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def detach_vpc2_nodes(vpc_id: str, data: vpc2.AttachDetachVpc2NodesData):
    """
    Remove nodes from a VPC 2.0 network.

    Args:
        vpc_id (str): The [VPC ID](#operation/list-vpcs).
        data (AttachDetachVpc2NodesData): The data to detach nodes from the VPC 2.0 network.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_VPC2_DETACH_NODES.assign("vpc-id", vpc_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()