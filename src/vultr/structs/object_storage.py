from typing import Optional


class CreateObjectStorageData:
    def __init__(self, cluster_id: int):
        """
        Data structure used for creating a Vultr Object Storage.

        Args:
            cluster_id (int): The [Cluster id](#operation/list-object-storage-clusters) where the Object Storage will be created.
        """
        self._cluster_id: int = cluster_id
        self._label: Optional[str] = None

    def label(self, label: str) -> "CreateObjectStorageData":
        """
        Set the user-supplied label for this Object Storage.

        Args:
            label (str): The user-supplied label.

        Returns:
            CreateObjectStorageData: The current object with the label set.
        """
        self._label = label
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "cluster_id": self._cluster_id,
            "label": self._label,
        }
        return {k: v for k, v in data.items() if v is not None}