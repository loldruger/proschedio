from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const


async def list_backups(
    instance_id: Optional[str],
    per_page: Optional[int],
    cursor: Optional[str],
):
    """
    Get information about Backups in your account.

    Args:
        instance_id (Optional[str]): Filter the backups list by Instance id.
        per_page (Optional[int]): Number of items requested per page. Default is 100 and max is 500.
        cursor (Optional[str]): Cursor for paging. See Meta and pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_BACKUPS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if instance_id is not None:
        request.add_param("instance_id", instance_id)
    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def get_backup(backup_id: str):
    """
    Get the information for the Backup.

    Args:
        backup_id (str): The Backup id.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_BACKUPS_ID.assign("backup-id", backup_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()