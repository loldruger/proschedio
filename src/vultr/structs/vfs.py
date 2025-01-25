from typing import Optional, List, Dict


class StorageSize:
    def __init__(self, gb: int):
        """
        Data structure representing the storage size for a Vultr VFS subscription.

        Args:
            gb (int): Size in gigabytes for the VFS.
        """
        self.gb: int = gb

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"gb": self.gb}


class CreateVfsData:
    def __init__(self, region: str, label: str, storage_size: StorageSize):
        """
        Data structure used for creating a Vultr VFS subscription.

        Args:
            region (str): Region identifier where to create the VFS.
            label (str): User-defined label for the VFS subscription.
            storage_size (StorageSize): Size in gigabytes for the VFS.
        """
        self._region: str = region
        self._label: str = label
        self._storage_size: StorageSize = storage_size
        self._disk_type: Optional[str] = None
        self._tags: Optional[List[str]] = None

    def disk_type(self, disk_type: str) -> "CreateVfsData":
        """
        Set the type of storage disk (defaults to nvme if not specified).

        Args:
            disk_type (str): Type of storage disk.

        Returns:
            CreateVfsData: The current object with the disk type set.
        """
        self._disk_type = disk_type
        return self

    def tags(self, tags: List[str]) -> "CreateVfsData":
        """
        Set optional tags to apply to the VFS subscription.

        Args:
            tags (List[str]): Optional tags.

        Returns:
            CreateVfsData: The current object with the tags set.
        """
        self._tags = tags
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "region": self._region,
            "label": self._label,
            "storage_size": self._storage_size.to_json(),
            "disk_type": self._disk_type,
            "tags": self._tags,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdateVfsData:
    def __init__(self, label: str, storage_size: StorageSize):
        """
        Data structure used for updating a Vultr VFS subscription.

        Args:
            label (str): New label for the VFS subscription.
            storage_size (StorageSize): Size in gigabytes for the VFS.
        """
        self._label: str = label
        self._storage_size: StorageSize = storage_size

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "label": self._label,
            "storage_size": self._storage_size.to_json(),
        }