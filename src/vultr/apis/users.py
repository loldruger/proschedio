from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import users

async def list_users(per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of all Users in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_USER_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_user(data: users.CreateUserData):
    """
    Create a new User. The `email`, `name`, and `password` attributes are required.

    Args:
        data (CreateUserData): The data to create the User.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_USER_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_user(user_id: str):
    """
    Get information about a User.

    Args:
        user_id (str): The [User id](#operation/list-users).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_USER_ID.assign("user-id", user_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_user(user_id: str, data: users.UpdateUserData):
    """
    Update information for a User.

    Args:
        user_id (str): The [User id](#operation/list-users).
        data (UpdateUserData): The data to update the User.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_USER_ID.assign("user-id", user_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_user(user_id: str):
    """
    Delete a User.

    Args:
        user_id (str): The [User id](#operation/list-users).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_USER_ID.assign("user-id", user_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()