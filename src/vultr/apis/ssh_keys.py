from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts


async def list_ssh_keys(per_page: Optional[int], cursor: Optional[str]):
    """
    List all SSH Keys in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_SSH_KEY_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_ssh_key(name: str, ssh_key: str):
    """
    Create a new SSH Key for use with future instances.

    Args:
        name (str): The user-supplied name for this SSH Key.
        ssh_key (str): The SSH Key.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_SSH_KEY_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"name": name, "ssh_key": ssh_key}) \
        .request()

async def get_ssh_key(ssh_key_id: str):
    """
    Get information about an SSH Key.

    Args:
        ssh_key_id (str): The [SSH Key id](#operation/list-ssh-keys).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_SSH_KEY_ID.assign("ssh-key-id", ssh_key_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_ssh_key(ssh_key_id: str, name: Optional[str], ssh_key: Optional[str]):
    """
    Update an SSH Key.

    Args:
        ssh_key_id (str): The [SSH Key id](#operation/list-ssh-keys).
        name (Optional[str]): The user-supplied name for this SSH Key.
        ssh_key (Optional[str]): The SSH Key.

    Returns:
        requests.Response: The response from the API.
    """
    body = {}
    if name is not None:
        body["name"] = name
    if ssh_key is not None:
        body["ssh_key"] = ssh_key

    return await composer.Request(Consts.URL_SSH_KEY_ID.assign("ssh-key-id", ssh_key_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(body) \
        .request()


async def delete_ssh_key(ssh_key_id: str):
    """
    Delete an SSH Key.

    Args:
        ssh_key_id (str): The [SSH Key id](#operation/list-ssh-keys).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_SSH_KEY_ID.assign("ssh-key-id", ssh_key_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()