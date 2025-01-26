from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import object_storage


async def list_object_storages(per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of all Object Storage in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_OBJECT_STORAGE_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_object_storage(data: object_storage.CreateObjectStorageData):
    """
    Create new Object Storage. The `cluster_id` attribute is required.

    Args:
        data (CreateObjectStorageData): The data to create the Object Storage.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_OBJECT_STORAGE_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_object_storage(object_storage_id: str):
    """
    Get information about an Object Storage.

    Args:
        object_storage_id (str): The [Object Storage id](#operation/list-object-storages).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_OBJECT_STORAGE_ID.assign("object-storage-id", object_storage_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_object_storage(object_storage_id: str, label: Optional[str]):
    """
    Update the label for an Object Storage.

    Args:
        object_storage_id (str): The [Object Storage id](#operation/list-object-storages).
        label (Optional[str]): The user-supplied label for the Object Storage.

    Returns:
        requests.Response: The response from the API.
    """
    body = {}
    if label is not None:
        body["label"] = label
    
    return await composer.Request(_const.URL_OBJECT_STORAGE_ID.assign("object-storage-id", object_storage_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()


async def delete_object_storage(object_storage_id: str):
    """
    Delete an Object Storage.

    Args:
        object_storage_id (str): The [Object Storage id](#operation/list-object-storages).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_OBJECT_STORAGE_ID.assign("object-storage-id", object_storage_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def regenerate_object_storage_keys(object_storage_id: str):
    """
    Regenerate the keys for an Object Storage.

    Args:
        object_storage_id (str): The [Object Storage id](#operation/list-object-storages).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_OBJECT_STORAGE_ID_REGENERATE_KEY.assign("object-storage-id", object_storage_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_object_storage_clusters(per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of all Object Storage Clusters.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_OBJECT_STORAGE_CLUSTERS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()