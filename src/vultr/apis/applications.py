from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts


async def list_applications(
    type: Optional[Literal["all", "marketplace", "one-click"]],
    per_page: Optional[int],
    cursor: Optional[str],
):
    """
    Get a list of all available Applications.

    Args:
        type (Optional[Literal["all", "marketplace", "one-click"]]): Filter the results by type.
        per_page (Optional[int]): Number of applications per page. Default is 100 and max is 500.
        cursor (Optional[str]): Cursor for paging. See Meta and pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_APPLICATIONS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if type is not None:
        request.add_param("type", type)
    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()