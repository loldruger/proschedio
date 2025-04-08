from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts


async def list_regions(per_page: Optional[int], cursor: Optional[str]):
    """
    List all Regions at Vultr.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_REGION) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def get_available_plans_in_region(
    region_id: str,
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
            "vbm",
            "vcg"
        ]
    ],
):
    """
    Get a list of the available plans in Region `region-id`. Not all plans are available in all regions.

    Args:
        region_id (str): The [Region id](#operation/list-regions).
        type (Optional[Literal["all", "vc2", "vdc", "vhf", "vhp", "voc", "voc-g", "voc-c", "voc-m", "voc-s", "vbm", "vcg"]]): Filter the results by type.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_REGION_ID_AVAILABLE.assign("region-id", region_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if type is not None:
        request.add_param("type", type)

    return await request.request()