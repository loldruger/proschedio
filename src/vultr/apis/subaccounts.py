from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import subaccount


async def list_subaccounts(per_page: Optional[int], cursor: Optional[str]):
    """
    Get information about all sub-accounts for your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_SUBACCOUNT_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_subaccount(data: subaccount.CreateSubaccountData):
    """
    Create a new subaccount.

    Args:
        data (CreateSubaccountData): The data to create the subaccount.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_SUBACCOUNT_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()