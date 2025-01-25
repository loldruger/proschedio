from typing import Optional, Literal


class CreateFirewallGroupData:
    def __init__(self, description: str):
        """
        Data structure used for creating a Vultr Firewall Group.

        Args:
            description (str): User-supplied description of this Firewall Group.
        """
        self._description: str = description

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"description": self._description}


class UpdateFirewallGroupData:
    def __init__(self, description: str):
        """
        Data structure used for updating a Vultr Firewall Group.

        Args:
            description (str): User-supplied description of this Firewall Group.
        """
        self._description: str = description

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"description": self._description}


class CreateFirewallRuleData:
    def __init__(
        self,
        ip_type: Literal["v4", "v6"],
        protocol: Literal["ICMP", "TCP", "UDP", "GRE", "ESP", "AH"],
        subnet: str,
        subnet_size: int,
    ):
        """
        Data structure used for creating a Vultr Firewall Rule.

        Args:
            ip_type (Literal["v4", "v6"]): The type of IP rule.
            protocol (Literal["ICMP", "TCP", "UDP", "GRE", "ESP", "AH"]): The protocol for this rule.
            subnet (str): IP address representing a subnet. The IP address format must match with the "ip_type" parameter value.
            subnet_size (int): The number of bits for the netmask in CIDR notation. Example: 32
        """
        self._ip_type: Literal["v4", "v6"] = ip_type
        self._protocol: Literal["ICMP", "TCP", "UDP", "GRE", "ESP", "AH"] = protocol
        self._subnet: str = subnet
        self._subnet_size: int = subnet_size
        self._port: Optional[str] = None
        self._source: Optional[str] = None
        self._notes: Optional[str] = None

    def port(self, port: str) -> "CreateFirewallRuleData":
        """
        Set the port (TCP/UDP only). This field can be a specific port or a colon separated port range.

        Args:
            port (str): The port or port range.

        Returns:
            CreateFirewallRuleData: The current object with the port set.
        """
        self._port = port
        return self

    def source(self, source: str) -> "CreateFirewallRuleData":
        """
        Set the source. If the source string is given a value of "cloudflare" subnet and subnet_size will both be ignored.

        Args:
            source (str): The source.

        Returns:
            CreateFirewallRuleData: The current object with the source set.
        """
        self._source = source
        return self

    def notes(self, notes: str) -> "CreateFirewallRuleData":
        """
        Set user-supplied notes for this rule.

        Args:
            notes (str): The notes.

        Returns:
            CreateFirewallRuleData: The current object with the notes set.
        """
        self._notes = notes
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "ip_type": self._ip_type,
            "protocol": self._protocol,
            "subnet": self._subnet,
            "subnet_size": self._subnet_size,
            "port": self._port,
            "source": self._source,
            "notes": self._notes,
        }
        return {k: v for k, v in data.items() if v is not None}