from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const


async def list_os_images(per_page: Optional[int], cursor: Optional[str]):
    """
    List the OS images available for installation at Vultr.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_OS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()