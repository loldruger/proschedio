from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import const, get_key


async def list_isos(per_page: Optional[int], cursor: Optional[str]):
    """
    Get the ISOs in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_ISO_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_iso(url: str):
    """
    Create a new ISO in your account from `url`.

    Args:
        url (str): Public URL location of the ISO image to download. Example: https://example.com/my-iso.iso

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_ISO_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"url": url}) \
        .request()


async def get_iso(iso_id: str):
    """
    Get information for an ISO.

    Args:
        iso_id (str): The [ISO id](#operation/list-isos).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_ISO_ID.assign("iso-id", iso_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def delete_iso(iso_id: str):
    """
    Delete an ISO.

    Args:
        iso_id (str): The [ISO id](#operation/list-isos).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_ISO_ID.assign("iso-id", iso_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_public_isos():
    """
    List all Vultr Public ISOs.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_ISO_PUBLIC_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()