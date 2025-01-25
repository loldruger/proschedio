from typing import Optional, Literal


class CreateSnapshotData:
    def __init__(self, instance_id: str):
        """
        Data structure used for creating a Vultr Snapshot.

        Args:
            instance_id (str): Create a Snapshot for this [Instance id](#operation/list-instances).
        """
        self._instance_id: str = instance_id
        self._description: Optional[str] = None

    def description(self, description: str) -> "CreateSnapshotData":
        """
        Set the user-supplied description of the Snapshot.

        Args:
            description (str): The user-supplied description.

        Returns:
            CreateSnapshotData: The current object with the description set.
        """
        self._description = description
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "instance_id": self._instance_id,
            "description": self._description,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdateSnapshotData:
    def __init__(self, description: str):
        """
        Data structure used for updating a Vultr Snapshot.

        Args:
            description (str): The user-supplied description for the Snapshot.
        """
        self._description: str = description

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"description": self._description}

class CreateSnapshotFromUrlData:
    def __init__(self, url: str):
        """
        Data structure used for creating a Vultr Snapshot from a URL.

        Args:
            url (str): The public URL containing a RAW image.
        """
        self._url: str = url
        self._description: Optional[str] = None
        self._uefi: Optional[Literal["true", "false"]] = None

    def description(self, description: str) -> "CreateSnapshotFromUrlData":
        """
        Set the user-supplied description of the Snapshot.

        Args:
            description (str): The user-supplied description.

        Returns:
            CreateSnapshotFromUrlData: The current object with the description set.
        """
        self._description = description
        return self

    def uefi(self, uefi: Literal["true", "false"]) -> "CreateSnapshotFromUrlData":
        """
        Set whether or not the snapshot uses UEFI.

        Args:
            uefi (Literal["true", "false"]): Whether or not the snapshot uses UEFI.

        Returns:
            CreateSnapshotFromUrlData: The current object with the UEFI setting set.
        """
        self._uefi = uefi
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "url": self._url,
            "description": self._description,
            "uefi": self._uefi,
        }
        return {k: v for k, v in data.items() if v is not None}