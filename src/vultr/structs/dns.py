from typing import Optional, Literal


class CreateDomainData:
    def __init__(self, domain: str):
        """
        Data structure used for creating a Vultr DNS Domain.

        Args:
            domain (str): Your registered DNS Domain name.
        """
        self._domain: str = domain
        self._ip: Optional[str] = None
        self._dns_sec: Optional[Literal["enabled", "disabled"]] = None

    def ip(self, ip: str) -> "CreateDomainData":
        """
        Set the default IP address for your DNS Domain. If omitted an empty domain zone will be created.

        Args:
            ip (str): The default IP address.

        Returns:
            CreateDomainData: The current object with the IP address set.
        """
        self._ip = ip
        return self

    def dns_sec(self, dns_sec: Literal["enabled", "disabled"]) -> "CreateDomainData":
        """
        Enable or disable DNSSEC.

        Args:
            dns_sec (Literal["enabled", "disabled"]): Whether to enable or disable DNSSEC.

        Returns:
            CreateDomainData: The current object with the DNSSEC setting set.
        """
        self._dns_sec = dns_sec
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "domain": self._domain,
            "ip": self._ip,
            "dns_sec": self._dns_sec,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdateDomainData:
    def __init__(self, dns_sec: Literal["enabled", "disabled"]):
        """
        Data structure used for updating a Vultr DNS Domain.

        Args:
            dns_sec (Literal["enabled", "disabled"]): Enable or disable DNSSEC.
        """
        self._dns_sec: Literal["enabled", "disabled"] = dns_sec

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"dns_sec": self._dns_sec}


class UpdateDomainSOAData:
    def __init__(self):
        """
        Data structure used for updating the SOA information for a Vultr DNS Domain.
        """
        self._nsprimary: Optional[str] = None
        self._email: Optional[str] = None

    def nsprimary(self, nsprimary: str) -> "UpdateDomainSOAData":
        """
        Set the primary nameserver.

        Args:
            nsprimary (str): The primary nameserver.

        Returns:
            UpdateDomainSOAData: The current object with the primary nameserver set.
        """
        self._nsprimary = nsprimary
        return self

    def email(self, email: str) -> "UpdateDomainSOAData":
        """
        Set the contact email address.

        Args:
            email (str): The contact email address.

        Returns:
            UpdateDomainSOAData: The current object with the contact email address set.
        """
        self._email = email
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "nsprimary": self._nsprimary,
            "email": self._email,
        }
        return {k: v for k, v in data.items() if v is not None}


class CreateDomainRecordData:
    def __init__(self, type: Literal["A", "AAAA", "CNAME", "NS", "MX", "SRV", "TXT", "CAA", "SSHFP"], name: str, data: str, ttl: int):
        """
        Data structure used for creating a DNS record.

        Args:
            type (Literal["A", "AAAA", "CNAME", "NS", "MX", "SRV", "TXT", "CAA", "SSHFP"]): The DNS record type.
            name (str): The hostname for this DNS record.
            data (str): The DNS data for this record type.
            ttl (int): Time to Live in seconds.
        """
        self._name: str = name
        self._type: Literal["A", "AAAA", "CNAME", "NS", "MX", "SRV", "TXT", "CAA", "SSHFP"] = type
        self._data: str = data
        self._ttl: int = ttl
        self._priority: Optional[int] = None

    def priority(self, priority: int) -> "CreateDomainRecordData":
        """
        Set the DNS priority. Does not apply to all record types. (Only required for MX and SRV)

        Args:
            priority (int): The DNS priority.

        Returns:
            CreateDomainRecordData: The current object with the priority set.
        """
        self._priority = priority
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "name": self._name,
            "type": self._type,
            "data": self._data,
            "ttl": self._ttl,
            "priority": self._priority,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdateDomainRecordData:
    def __init__(self):
        """
        Data structure used for updating a DNS record.
        """
        self._name: Optional[str] = None
        self._data: Optional[str] = None
        self._ttl: Optional[int] = None
        self._priority: Optional[int] = None

    def name(self, name: str) -> "UpdateDomainRecordData":
        """
        Set the hostname for this DNS record.

        Args:
            name (str): The hostname.

        Returns:
            UpdateDomainRecordData: The current object with the hostname set.
        """
        self._name = name
        return self

    def data(self, data: str) -> "UpdateDomainRecordData":
        """
        Set the DNS data for this record type.

        Args:
            data (str): The DNS data.

        Returns:
            UpdateDomainRecordData: The current object with the DNS data set.
        """
        self._data = data
        return self

    def ttl(self, ttl: int) -> "UpdateDomainRecordData":
        """
        Set the Time to Live in seconds.

        Args:
            ttl (int): The TTL.

        Returns:
            UpdateDomainRecordData: The current object with the TTL set.
        """
        self._ttl = ttl
        return self

    def priority(self, priority: int) -> "UpdateDomainRecordData":
        """
        Set the DNS priority. Does not apply to all record types.

        Args:
            priority (int): The DNS priority.

        Returns:
            UpdateDomainRecordData: The current object with the priority set.
        """
        self._priority = priority
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "name": self._name,
            "data": self._data,
            "ttl": self._ttl,
            "priority": self._priority,
        }
        return {k: v for k, v in data.items() if v is not None}