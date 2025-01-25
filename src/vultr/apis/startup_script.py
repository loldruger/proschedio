from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import const, get_key


async def list_startup_scripts(per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of all Startup Scripts in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_STARTUP_SCRIPT_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_startup_script(name: str, script: str, type: Optional[Literal["boot", "pxe"]]):
    """
    Create a new Startup Script in your account.

    Args:
        name (str): The name of the Startup Script.
        script (str): The Startup Script contents.
        type (Optional[Literal["boot", "pxe"]]): The Startup Script type. Default: "boot"

    Returns:
        requests.Response: The response from the API.
    """
    body = {
        "name": name,
        "script": script,
        "type": type,
    }
    return await composer.Request(const.URL_STARTUP_SCRIPT_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({k: v for k, v in body.items() if v is not None}) \
        .request()

async def get_startup_script(startup_id: str):
    """
    Get information for a Startup Script.

    Args:
        startup_id (str): The [Startup Script id](#operation/list-startup-scripts).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_startup_script(startup_id: str, data: UpdateStartupScriptData):
    """
    Update a Startup Script.

    Args:
        startup_id (str): The [Startup Script id](#operation/list-startup-scripts).
        data (UpdateStartupScriptData): The data to update the Startup Script.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def delete_startup_script(startup_id: str):
    """
    Delete a Startup Script.

    Args:
        startup_id (str): The [Startup Script id](#operation/list-startup-scripts).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()