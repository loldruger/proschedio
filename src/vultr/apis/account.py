from http import HTTPMethod

from proschedio import composer
from vultr import get_key
from vultr.apis import _const


async def get_account_info():
    """
    Get your Vultr account, permission, and billing information.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_ACCOUNT) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_account_bandwidth():
    """
    Get your Vultr account bandwidth information.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_ACCOUNT_BANDWIDTH) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()