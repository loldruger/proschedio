from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import cdns

async def list_cdn_pull_zones():
    """
    List CDN Pull Zones.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_LIST_PULL_ZONES) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_cdn_pull_zone(data: cdns.CreatePullZoneData):
    """
    Create a new CDN Pull Zone.

    Args:
        data (CreatePullZoneData): The data to create the pull zone.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_LIST_PULL_ZONES) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_cdn_pull_zone(pullzone_id: str):
    """
    Get information about a CDN Pull Zone.

    Args:
        pullzone_id (str): The Pull Zone ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PULL_ZONE_ID.assign("pullzone-id", pullzone_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_cdn_pull_zone(pullzone_id: str, data: cdns.UpdatePullZoneData):
    """
    Update information for a CDN Pull Zone.

    Args:
        pullzone_id (str): The Pull Zone ID.
        data (UpdatePullZoneData): The data to update the pull zone.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PULL_ZONE_ID.assign("pullzone-id", pullzone_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def delete_cdn_pull_zone(pullzone_id: str):
    """
    Delete a CDN Pull Zone.

    Args:
        pullzone_id (str): The Pull Zone ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PULL_ZONE_ID.assign("pullzone-id", pullzone_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def purge_cdn_pull_zone_cache(pullzone_id: str):
    """
    Clears cached content on server proxies so that visitors can get the latest page versions.

    Args:
        pullzone_id (str): The Pull Zone ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PULL_ZONE_PURGE.assign("pullzone-id", pullzone_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_cdn_push_zones():
    """
    List CDN Push Zones.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONES) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_cdn_push_zone(data: cdns.CreatePushZoneData):
    """
    Create a new CDN Push Zone.

    Args:
        data (CreatePushZoneData): The data to create the push zone.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONES) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_cdn_push_zone(pushzone_id: str):
    """
    Get information about a CDN Push Zone.

    Args:
        pushzone_id (str): The Push Zone ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_ID.assign("pushzone-id", pushzone_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_cdn_push_zone(pushzone_id: str, data: cdns.UpdatePushZoneData):
    """
    Update information for a CDN Push Zone.

    Args:
        pushzone_id (str): The Push Zone ID.
        data (UpdatePushZoneData): The data to update the push zone.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_ID.assign("pushzone-id", pushzone_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def delete_cdn_push_zone(pushzone_id: str):
    """
    Delete a CDN Push Zone.

    Args:
        pushzone_id (str): The Push Zone ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_ID.assign("pushzone-id", pushzone_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_cdn_push_zone_files(pushzone_id: str):
    """
    Get a list of files that have been uploaded to a specific CDN Push Zone.

    Args:
        pushzone_id (str): The Push Zone ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_FILES.assign("pushzone-id", pushzone_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_cdn_push_zone_file(pushzone_id: str, data: cdns.CreatePushZoneFileData):
    """
    Create a presigned post endpoint that can be used to upload a file to your Push Zone.

    Args:
        pushzone_id (str): The Push Zone ID.
        data (CreatePushZoneFileData): The data to create the file.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_FILES.assign("pushzone-id", pushzone_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_cdn_push_zone_file(pushzone_id: str, file_name: str):
    """
    Get information about a CDN Push Zone file.

    Args:
        pushzone_id (str): The Push Zone ID.
        file_name (str): The File Name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_FILE.assign("pushzone-id", pushzone_id).assign("file-name", file_name)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def delete_cdn_push_zone_file(pushzone_id: str, file_name: str):
    """
    Delete a CDN Push Zone file.

    Args:
        pushzone_id (str): The Push Zone ID.
        file_name (str): The File Name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_CDN_PUSH_ZONE_FILE.assign("pushzone-id", pushzone_id).assign("file-name", file_name)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()