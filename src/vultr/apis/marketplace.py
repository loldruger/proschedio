from http import HTTPMethod

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts


async def get_marketplace_app_variables(image_id: str):
    """
    List all user-supplied variables for a Marketplace App.

    Args:
        image_id (str): The application's [Image ID](#operation/list-applications).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_MARKETPLACE_APP_VARIABLES.assign("image-id", image_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()