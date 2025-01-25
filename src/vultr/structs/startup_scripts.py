from typing import Optional, Literal
from http import HTTPMethod

from proschedio import composer
from vultr import const, get_key

class UpdateStartupScriptData:
    def __init__(self):
        """
        Data structure used for updating a Vultr Startup Script.
        """
        self._name: Optional[str] = None
        self._script: Optional[str] = None
        self._type: Optional[Literal["boot", "pxe"]] = None

    def name(self, name: str) -> "UpdateStartupScriptData":
        """
        Set the name of the Startup Script.

        Args:
            name (str): The name of the Startup Script.

        Returns:
            UpdateStartupScriptData: The current object with the name set.
        """
        self._name = name
        return self

    def script(self, script: str) -> "UpdateStartupScriptData":
        """
        Set the base64 encoded Startup Script.

        Args:
            script (str): The base64 encoded Startup Script.

        Returns:
            UpdateStartupScriptData: The current object with the script set.
        """
        self._script = script
        return self

    def type(self, type: Literal["boot", "pxe"]) -> "UpdateStartupScriptData":
        """
        Set the Startup Script type.

        Args:
            type (Literal["boot", "pxe"]): The Startup Script type.

        Returns:
            UpdateStartupScriptData: The current object with the type set.
        """
        self._type = type
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "name": self._name,
            "script": self._script,
            "type": self._type,
        }
        return {k: v for k, v in data.items() if v is not None}

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