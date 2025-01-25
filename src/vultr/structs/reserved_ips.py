from typing import Optional, Literal


class CreateReservedIpData:
    def __init__(self, region: str, ip_type: Literal["v4", "v6"]):
        """
        Data structure used for creating a Vultr Reserved IP.

        Args:
            region (str): The [Region id](#operation/list-regions) where the Reserved IP will be created.
            ip_type (Literal["v4", "v6"]): The type of IP address.
        """
        self._region: str = region
        self._ip_type: Literal["v4", "v6"] = ip_type
        self._label: Optional[str] = None

    def label(self, label: str) -> "CreateReservedIpData":
        """
        Set the user-supplied label.

        Args:
            label (str): The user-supplied label.

        Returns:
            CreateReservedIpData: The current object with the label set.
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
            "region": self._region,
            "ip_type": self._ip_type,
            "label": self._label,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdateReservedIpData:
    def __init__(self, label: str):
        """
        Data structure used for updating a Vultr Reserved IP.

        Args:
            label (str): The user-supplied label.
        """
        self._label: str = label

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"label": self._label}

class ConvertIpToReservedIpData:
    def __init__(self, ip_address: str):
        """
        Data structure used for converting an existing instance IP address to a Reserved IP.

        Args:
            ip_address (str): The IP address to convert.
        """
        self._ip_address: str = ip_address
        self._label: Optional[str] = None
    
    def label(self, label: str) -> "ConvertIpToReservedIpData":
        """
        Set the user-supplied label.

        Args:
            label (str): The user-supplied label.

        Returns:
            ConvertIpToReservedIpData: The current object with the label set.
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
            "ip_address": self._ip_address,
            "label": self._label
        }
        return {k: v for k, v in data.items() if v is not None}