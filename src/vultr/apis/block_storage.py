from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const


async def list_block_storage(per_page: Optional[int], cursor: Optional[str]):
    """
    List all Block Storage in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and max is 500.
        cursor (Optional[str]): Cursor for paging. See Meta and pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_BLOCK_STORAGE) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_block_storage(region: str, size_gb: int, label: Optional[str], block_type: Optional[str]):
    """
    Create new Block Storage in a `region` with a size of `size_gb`.

    Args:
        region (str): The [Region id](#operation/list-regions) where the Block Storage will be created.
        size_gb (int): Size in GB may range between 10 and 40000, depending on the block_type.
        label (Optional[str]): The user-supplied label.
        block_type (Optional[str]): An optional parameter, that determines the type of block storage volume.

    Returns:
        requests.Response: The response from the API.
    """
    body = {
        "region": region,
        "size_gb": size_gb,
    }
    if label is not None:
        body["label"] = label
    if block_type is not None:
        body["block_type"] = block_type

    return await composer.Request(_const.URL_BLOCK_STORAGE) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()


async def get_block_storage_by_id(block_id: str):
    """
    Get information for Block Storage.

    Args:
        block_id (str): The Block Storage id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_BLOCK_STORAGE_ID.assign("block-id", block_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_block_storage_by_id(block_id: str, label: Optional[str], size_gb: Optional[int]):
    """
    Update information for Block Storage.

    Args:
        block_id (str): The Block Storage id.
        label (Optional[str]): The user-supplied label.
        size_gb (Optional[int]): The new size of the block storage volume in GB. Must be >= current size.

    Returns:
        requests.Response: The response from the API.
    """
    body = {}
    if label is not None:
        body["label"] = label
    if size_gb is not None:
        body["size_gb"] = size_gb

    return await composer.Request(_const.URL_BLOCK_STORAGE_ID.assign("block-id", block_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()


async def delete_block_storage_by_id(block_id: str):
    """
    Delete Block Storage.

    Args:
        block_id (str): The Block Storage id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_BLOCK_STORAGE_ID.assign("block-id", block_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def attach_block_storage(block_id: str, instance_id: str, live: Optional[bool]):
    """
    Attach Block Storage to Instance.

    Args:
        block_id (str): The Block Storage id.
        instance_id (str): The [Instance id](#operation/list-instances) to attach.
        live (Optional[bool]): Attach without restarting the Instance.

    Returns:
        requests.Response: The response from the API.
    """
    body = {
        "instance_id": instance_id,
    }
    if live is not None:
        body["live"] = live

    return await composer.Request(_const.URL_BLOCK_STORAGE_ATTACH.assign("block-id", block_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()


async def detach_block_storage(block_id: str, live: Optional[bool]):
    """
    Detach Block Storage.

    Args:
        block_id (str): The Block Storage id.
        live (Optional[bool]): Detach without restarting the Instance.

    Returns:
        requests.Response: The response from the API.
    """
    body = {}
    if live is not None:
        body["live"] = live

    return await composer.Request(_const.URL_BLOCK_STORAGE_DETACH.assign("block-id", block_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()