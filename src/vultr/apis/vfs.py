from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import const, get_key


async def list_vfs_regions():
    """
    Retrieve a list of all regions where VFS can be deployed.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_REGIONS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_vfs_subscriptions(per_page: Optional[int] = None, cursor: Optional[str] = None):
    """
    Retrieve a list of all VFS subscriptions for the account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_VFS_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_vfs_subscription(data: CreateVfsData):
    """
    Create a new VFS subscription with the specified configuration.

    Args:
        data (CreateVfsData): The data to create the VFS subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_vfs_subscription(vfs_id: str):
    """
    Retrieve a specific VFS subscription by ID.

    Args:
        vfs_id (str): ID of the VFS subscription to retrieve.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ID.assign("vfs-id", vfs_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_vfs_subscription(vfs_id: str, data: UpdateVfsData):
    """
    Update a VFS subscription's label or storage size.

    Args:
        vfs_id (str): ID of the VFS subscription to update.
        data (UpdateVfsData): The data to update the VFS subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ID.assign("vfs-id", vfs_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def delete_vfs_subscription(vfs_id: str):
    """
    Delete a specific VFS subscription by ID.

    Args:
        vfs_id (str): ID of the VFS subscription to delete.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ID.assign("vfs-id", vfs_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_vfs_attachments(vfs_id: str):
    """
    Retrieve a list of all attachments for a specific VFS subscription.

    Args:
        vfs_id (str): ID of the VFS subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ATTACHMENTS.assign("vfs-id", vfs_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def attach_vps_to_vfs(vfs_id: str, vps_id: str):
    """
    Attach a VPS instance to a VFS subscription.

    Args:
        vfs_id (str): ID of the VFS subscription.
        vps_id (str): ID of the VPS subscription to attach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ATTACHMENT.assign("vfs-id", vfs_id).assign("vps-id", vps_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_vfs_vps_attachment(vfs_id: str, vps_id: str):
    """
    Retrieve details about a specific VFS-VPS attachment.

    Args:
        vfs_id (str): ID of the VFS subscription.
        vps_id (str): ID of the VPS subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ATTACHMENT.assign("vfs-id", vfs_id).assign("vps-id", vps_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def detach_vps_from_vfs(vfs_id: str, vps_id: str):
    """
    Detach a VPS instance from a VFS subscription.

    Args:
        vfs_id (str): ID of the VFS subscription.
        vps_id (str): ID of the VPS subscription to detach.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_VFS_ATTACHMENT.assign("vfs-id", vfs_id).assign("vps-id", vps_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()