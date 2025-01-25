from http import HTTPMethod

from proschedio import composer
from vultr import const, get_key


async def get_account_info():
    """
    Get your Vultr account, permission, and billing information.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_ACCOUNT) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_account_bandwidth():
    """
    Get your Vultr account bandwidth information.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_ACCOUNT_BANDWIDTH) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()