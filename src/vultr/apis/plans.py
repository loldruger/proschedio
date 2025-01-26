from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import get_key
from vultr.apis import _const


async def list_plans(
    type: Optional[
        Literal[
            "all",
            "vc2",
            "vdc",
            "vhf",
            "vhp",
            "voc",
            "voc-g",
            "voc-c",
            "voc-m",
            "voc-s",
            "vcg",
        ]
    ],
    per_page: Optional[int],
    cursor: Optional[str],
    os: Optional[Literal["windows"]],
):
    """
    Get a list of all VPS plans at Vultr.

    Args:
        type (Optional[Literal["all", "vc2", "vdc", "vhf", "vhp", "voc", "voc-g", "voc-c", "voc-m", "voc-s", "vcg"]]): Filter the results by type.
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
        os (Optional[Literal["windows"]]): Filter the results by operating system.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_PLAN) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if type is not None:
        request.add_param("type", type)
    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)
    if os is not None:
        request.add_param("os", os)

    return await request.request()