from typing import Optional


class CreateVpcData:
    def __init__(self, region: str):
        """
        Data structure used for creating a Vultr VPC.

        Args:
            region (str): Create the VPC in this [Region id](#operation/list-regions).
        """
        self._region: str = region
        self._description: Optional[str] = None
        self._v4_subnet: Optional[str] = None
        self._v4_subnet_mask: Optional[int] = None

    def description(self, description: str) -> "CreateVpcData":
        """
        Set a description of the VPC.

        Args:
            description (str): A description of the VPC.

        Returns:
            CreateVpcData: The current object with the description set.
        """
        self._description = description
        return self

    def v4_subnet(self, v4_subnet: str) -> "CreateVpcData":
        """
        Set the IPv4 VPC address. For example: 10.99.0.0
        *If v4_subnet_mask is specified then v4_subnet is a required field.

        Args:
            v4_subnet (str): The IPv4 VPC address.

        Returns:
            CreateVpcData: The current object with the IPv4 subnet set.
        """
        self._v4_subnet = v4_subnet
        return self

    def v4_subnet_mask(self, v4_subnet_mask: int) -> "CreateVpcData":
        """
        Set the number of bits for the netmask in CIDR notation. Example: 24
        *If v4_subnet is specified then v4_subnet_mask is a required field.

        Args:
            v4_subnet_mask (int): The number of bits for the netmask.

        Returns:
            CreateVpcData: The current object with the IPv4 subnet mask set.
        """
        self._v4_subnet_mask = v4_subnet_mask
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
            "v4_subnet": self._v4_subnet,
            "v4_subnet_mask": self._v4_subnet_mask,
        }
        return {k: v for k, v in data.items() if v is not None}