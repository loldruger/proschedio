from typing import Optional, List


class CreateVpc2Data:
    def __init__(self, region: str):
        """
        Data structure used for creating a Vultr VPC 2.0 network.

        Args:
            region (str): The [Region id](#operation/list-regions) to create the instance.
        """
        self._region: str = region
        self._description: Optional[str] = None
        self._ip_block: Optional[str] = None
        self._prefix_length: Optional[int] = None

    def description(self, description: str) -> "CreateVpc2Data":
        """
        Set a description of the VPC.

        Args:
            description (str): A description of the VPC.

        Returns:
            CreateVpc2Data: The current object with the description set.
        """
        self._description = description
        return self

    def ip_block(self, ip_block: str) -> "CreateVpc2Data":
        """
        Set the VPC subnet IP address. For example: 10.99.0.0

        Args:
            ip_block (str): The VPC subnet IP address.

        Returns:
            CreateVpc2Data: The current object with the IP block set.
        """
        self._ip_block = ip_block
        return self

    def prefix_length(self, prefix_length: int) -> "CreateVpc2Data":
        """
        Set the number of bits for the netmask in CIDR notation. Example: 24

        Args:
            prefix_length (int): The number of bits for the netmask.

        Returns:
            CreateVpc2Data: The current object with the prefix length set.
        """
        self._prefix_length = prefix_length
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "region": self._region,
            "description": self._description,
            "ip_block": self._ip_block,
            "prefix_length": self._prefix_length,
        }
        return {k: v for k, v in data.items() if v is not None}

class AttachDetachVpc2NodesData:
    def __init__(self, nodes: List[List[str]]):
        """
        Data structure used for attaching or detaching nodes to/from a Vultr VPC 2.0 network.

        Args:
            nodes (List[List[str]]): An array of ID strings for [instances](#operation/list-instances) and [Bare Metal servers](#operation/list-baremetals) to attach as nodes to the VPC 2.0 network. A limit of 1000 nodes can be processed in a request
        """
        self._nodes: List[List[str]] = nodes

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "nodes": self._nodes
        }