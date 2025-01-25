from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import const, get_key


async def get_billing_history(per_page: Optional[int], cursor: Optional[str]):
    """
    Retrieve billing history entries.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100, maximum is 500.
        cursor (Optional[str]): Cursor for pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BILLING_LIST_HISTORY) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page:
        request.add_param("per_page", per_page)
    if cursor:
        request.add_param("cursor", cursor)

    return await request.request()


async def get_billing_invoices(per_page: Optional[int], cursor: Optional[str]):
    """
    Retrieve a list of all invoices on the account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100, maximum is 500.
        cursor (Optional[str]): Cursor for pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BILLING_INVOICES) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page:
        request.add_param("per_page", per_page)
    if cursor:
        request.add_param("cursor", cursor)

    return await request.request()


async def get_billing_invoice_by_id(invoice_id: str):
    """
    Retrieve a specific invoice by ID.

    Args:
        invoice_id (str): The ID of the invoice to retrieve.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BILLING_INVOICE_ID.assign("invoice-id", invoice_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_billing_invoice_items(invoice_id: str, per_page: Optional[int], cursor: Optional[str]):
    """
    Retrieve line items for a specific invoice.

    Args:
        invoice_id (str): The ID of the invoice.
        per_page (Optional[int]): Number of items requested per page. Default is 100, maximum is 500.
        cursor (Optional[str]): Cursor for pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_BILLING_INVOICE_ID_ITEMS.assign("invoice-id", invoice_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page:
        request.add_param("per_page", per_page)
    if cursor:
        request.add_param("cursor", cursor)

    return await request.request()


async def get_pending_charges():
    """
    Retrieve all pending charges for the account.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_BILLING_LIST_PENDING_CHARGES) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()