from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import const, get_key


async def list_snapshots(
    description: Optional[str],
    per_page: Optional[int],
    cursor: Optional[str],
):
    """
    Get information about all Snapshots in your account.

    Args:
        description (Optional[str]): Filter the list of Snapshots by `description`.
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_SNAPSHOT_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if description is not None:
        request.add_param("description", description)
    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_snapshot(data: CreateSnapshotData):
    """
    Create a new Snapshot for `instance_id`.

    Args:
        data (CreateSnapshotData): The data to create the Snapshot.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_SNAPSHOT_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_snapshot(snapshot_id: str):
    """
    Get information about a Snapshot.

    Args:
        snapshot_id (str): The [Snapshot id](#operation/list-snapshots).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_SNAPSHOT_ID.assign("snapshot-id", snapshot_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_snapshot(snapshot_id: str, description: str):
    """
    Update the description for a Snapshot.

    Args:
        snapshot_id (str): The [Snapshot id](#operation/list-snapshots).
        description (str): The user-supplied description for the Snapshot.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_SNAPSHOT_ID.assign("snapshot-id", snapshot_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"description": description}) \
        .request()


async def delete_snapshot(snapshot_id: str):
    """
    Delete a Snapshot.

    Args:
        snapshot_id (str): The [Snapshot id](#operation/list-snapshots).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_SNAPSHOT_ID.assign("snapshot-id", snapshot_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_snapshot_from_url(data: CreateSnapshotFromUrlData):
    """
    Create a new Snapshot from a RAW image located at `url`.

    Args:
        data (CreateSnapshotFromUrlData): The data to create the Snapshot from URL.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_SNAPSHOT_CREATE_FROM_URL) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()