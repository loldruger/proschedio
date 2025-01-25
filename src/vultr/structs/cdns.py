from typing import Optional, List


class CreatePullZoneData:
    def __init__(self, label: str, origin_scheme: str, origin_domain: str):
        """
        Data structure used for creating a Vultr CDN Pull Zone

        Args:
            label (str): The user-supplied label.
            origin_scheme (str): The URI scheme of the origin domain. Enum: ["http", "https"]
            origin_domain (str): The domain name from which the content stored in the CDN will be pulled.
        """
        self._label: str = label
        self._origin_scheme: str = origin_scheme
        self._origin_domain: str = origin_domain
        self._vanity_domain: Optional[str] = None
        self._ssl_cert: Optional[str] = None
        self._ssl_cert_key: Optional[str] = None
        self._cors: Optional[bool] = None
        self._gzip: Optional[bool] = None
        self._block_ai: Optional[bool] = None
        self._block_bad_bots: Optional[bool] = None

    def vanity_domain(self, vanity_domain: str) -> "CreatePullZoneData":
        """
        An optional domain name that can be used to access the cached files.

        Args:
            vanity_domain (str): The vanity domain to use.

        Returns:
            CreatePullZoneData: The current object with the vanity domain set.
        """
        self._vanity_domain = vanity_domain
        return self

    def ssl_cert(self, ssl_cert: str) -> "CreatePullZoneData":
        """
        Base 64 encoded SSL certificate (required if vanity_domain and origin_scheme=https)

        Args:
            ssl_cert (str): Base64 encoded SSL certificate.

        Returns:
            CreatePullZoneData: The current object with the SSL certificate set.
        """
        self._ssl_cert = ssl_cert
        return self

    def ssl_cert_key(self, ssl_cert_key: str) -> "CreatePullZoneData":
        """
        Base 64 encoded SSL private key (required if vanity_domain and origin_scheme=https)

        Args:
            ssl_cert_key (str): Base64 encoded SSL private key.

        Returns:
            CreatePullZoneData: The current object with the SSL private key set.
        """
        self._ssl_cert_key = ssl_cert_key
        return self

    def cors(self, cors: bool) -> "CreatePullZoneData":
        """
        Enable Cross-origin resource sharing

        Args:
            cors (bool): Whether to enable CORS.

        Returns:
            CreatePullZoneData: The current object with CORS setting set.
        """
        self._cors = cors
        return self

    def gzip(self, gzip: bool) -> "CreatePullZoneData":
        """
        Enable Gzip compression

        Args:
            gzip (bool): Whether to enable Gzip compression.

        Returns:
            CreatePullZoneData: The current object with Gzip compression setting set.
        """
        self._gzip = gzip
        return self

    def block_ai(self, block_ai: bool) -> "CreatePullZoneData":
        """
        Block AI bots

        Args:
            block_ai (bool): Whether to block AI bots.

        Returns:
            CreatePullZoneData: The current object with AI bot blocking setting set.
        """
        self._block_ai = block_ai
        return self

    def block_bad_bots(self, block_bad_bots: bool) -> "CreatePullZoneData":
        """
        Block potentially malicious bots

        Args:
            block_bad_bots (bool): Whether to block potentially malicious bots.

        Returns:
            CreatePullZoneData: The current object with potentially malicious bot blocking setting set.
        """
        self._block_bad_bots = block_bad_bots
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "label": self._label,
            "origin_scheme": self._origin_scheme,
            "origin_domain": self._origin_domain,
            "vanity_domain": self._vanity_domain,
            "ssl_cert": self._ssl_cert,
            "ssl_cert_key": self._ssl_cert_key,
            "cors": self._cors,
            "gzip": self._gzip,
            "block_ai": self._block_ai,
            "block_bad_bots": self._block_bad_bots,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdatePullZoneData:
    def __init__(self):
        """
        Data structure used for updating a Vultr CDN Pull Zone
        """
        self._label: Optional[str] = None
        self._vanity_domain: Optional[str] = None
        self._ssl_cert: Optional[str] = None
        self._ssl_cert_key: Optional[str] = None
        self._cors: Optional[bool] = None
        self._gzip: Optional[bool] = None
        self._block_ai: Optional[bool] = None
        self._block_bad_bots: Optional[bool] = None
        self._regions: Optional[List[str]] = None

    def label(self, label: str) -> "UpdatePullZoneData":
        """
        The user-supplied label.

        Args:
            label (str): The user-supplied label.

        Returns:
            UpdatePullZoneData: The current object with the label set.
        """
        self._label = label
        return self

    def vanity_domain(self, vanity_domain: str) -> "UpdatePullZoneData":
        """
        An optional domain name that can be used to access the cached files.

        Args:
            vanity_domain (str): The vanity domain to use.

        Returns:
            UpdatePullZoneData: The current object with the vanity domain set.
        """
        self._vanity_domain = vanity_domain
        return self

    def ssl_cert(self, ssl_cert: str) -> "UpdatePullZoneData":
        """
        Base 64 encoded SSL certificate (required if vanity_domain)

        Args:
            ssl_cert (str): Base64 encoded SSL certificate.

        Returns:
            UpdatePullZoneData: The current object with the SSL certificate set.
        """
        self._ssl_cert = ssl_cert
        return self

    def ssl_cert_key(self, ssl_cert_key: str) -> "UpdatePullZoneData":
        """
        Base 64 encoded SSL private key (required if vanity_domain)

        Args:
            ssl_cert_key (str): Base64 encoded SSL private key.

        Returns:
            UpdatePullZoneData: The current object with the SSL private key set.
        """
        self._ssl_cert_key = ssl_cert_key
        return self

    def cors(self, cors: bool) -> "UpdatePullZoneData":
        """
        Cross-origin resource sharing

        Args:
            cors (bool): Whether to enable CORS.

        Returns:
            UpdatePullZoneData: The current object with the CORS setting set.
        """
        self._cors = cors
        return self

    def gzip(self, gzip: bool) -> "UpdatePullZoneData":
        """
        Optional feature to compress files

        Args:
            gzip (bool): Whether to enable Gzip compression.

        Returns:
            UpdatePullZoneData: The current object with the Gzip compression setting set.
        """
        self._gzip = gzip
        return self

    def block_ai(self, block_ai: bool) -> "UpdatePullZoneData":
        """
        Optional feature to block AI bots

        Args:
            block_ai (bool): Whether to block AI bots.

        Returns:
            UpdatePullZoneData: The current object with the AI bot blocking setting set.
        """
        self._block_ai = block_ai
        return self

    def block_bad_bots(self, block_bad_bots: bool) -> "UpdatePullZoneData":
        """
        Optional feature to block malicious bots

        Args:
            block_bad_bots (bool): Whether to block potentially malicious bots.

        Returns:
            UpdatePullZoneData: The current object with the potentially malicious bot blocking setting set.
        """
        self._block_bad_bots = block_bad_bots
        return self

    def regions(self, regions: List[str]) -> "UpdatePullZoneData":
        """
        List of [Region ids](#operation/list-regions) for content delivery

        Args:
            regions (List[str]): List of region IDs.

        Returns:
            UpdatePullZoneData: The current object with the region list set.
        """
        self._regions = regions
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "label": self._label,
            "vanity_domain": self._vanity_domain,
            "ssl_cert": self._ssl_cert,
            "ssl_cert_key": self._ssl_cert_key,
            "cors": self._cors,
            "gzip": self._gzip,
            "block_ai": self._block_ai,
            "block_bad_bots": self._block_bad_bots,
            "regions": self._regions,
        }
        return {k: v for k, v in data.items() if v is not None}


class CreatePushZoneData:
    def __init__(self, label: str):
        """
        Data structure used for creating a Vultr CDN Push Zone

        Args:
            label (str): The user-supplied label.
        """
        self._label: str = label
        self._vanity_domain: Optional[str] = None
        self._ssl_cert: Optional[str] = None
        self._ssl_cert_key: Optional[str] = None
        self._cors: Optional[bool] = None
        self._gzip: Optional[bool] = None
        self._block_ai: Optional[bool] = None
        self._block_bad_bots: Optional[bool] = None

    def vanity_domain(self, vanity_domain: str) -> "CreatePushZoneData":
        """
        An optional domain name that can be used to access the cached files.

        Args:
            vanity_domain (str): The vanity domain to use.

        Returns:
            CreatePushZoneData: The current object with the vanity domain set.
        """
        self._vanity_domain = vanity_domain
        return self

    def ssl_cert(self, ssl_cert: str) -> "CreatePushZoneData":
        """
        Base 64 encoded SSL certificate (required if vanity_domain)

        Args:
            ssl_cert (str): Base64 encoded SSL certificate.

        Returns:
            CreatePushZoneData: The current object with the SSL certificate set.
        """
        self._ssl_cert = ssl_cert
        return self

    def ssl_cert_key(self, ssl_cert_key: str) -> "CreatePushZoneData":
        """
        Base 64 encoded SSL private key (required if vanity_domain)

        Args:
            ssl_cert_key (str): Base64 encoded SSL private key.

        Returns:
            CreatePushZoneData: The current object with the SSL private key set.
        """
        self._ssl_cert_key = ssl_cert_key
        return self

    def cors(self, cors: bool) -> "CreatePushZoneData":
        """
        Enable Cross-origin resource sharing

        Args:
            cors (bool): Whether to enable CORS.

        Returns:
            CreatePushZoneData: The current object with the CORS setting set.
        """
        self._cors = cors
        return self

    def gzip(self, gzip: bool) -> "CreatePushZoneData":
        """
        Enable Gzip compression

        Args:
            gzip (bool): Whether to enable Gzip compression.

        Returns:
            CreatePushZoneData: The current object with the Gzip compression setting set.
        """
        self._gzip = gzip
        return self

    def block_ai(self, block_ai: bool) -> "CreatePushZoneData":
        """
        Block AI bots

        Args:
            block_ai (bool): Whether to block AI bots.

        Returns:
            CreatePushZoneData: The current object with the AI bot blocking setting set.
        """
        self._block_ai = block_ai
        return self

    def block_bad_bots(self, block_bad_bots: bool) -> "CreatePushZoneData":
        """
        Block potentially malicious bots

        Args:
            block_bad_bots (bool): Whether to block potentially malicious bots.

        Returns:
            CreatePushZoneData: The current object with the potentially malicious bot blocking setting set.
        """
        self._block_bad_bots = block_bad_bots
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "label": self._label,
            "vanity_domain": self._vanity_domain,
            "ssl_cert": self._ssl_cert,
            "ssl_cert_key": self._ssl_cert_key,
            "cors": self._cors,
            "gzip": self._gzip,
            "block_ai": self._block_ai,
            "block_bad_bots": self._block_bad_bots,
        }
        return {k: v for k, v in data.items() if v is not None}


class UpdatePushZoneData:
    def __init__(self):
        """
        Data structure used for updating a Vultr CDN Push Zone
        """
        self._label: Optional[str] = None
        self._vanity_domain: Optional[str] = None
        self._ssl_cert: Optional[str] = None
        self._ssl_cert_key: Optional[str] = None
        self._cors: Optional[bool] = None
        self._gzip: Optional[bool] = None
        self._block_ai: Optional[bool] = None
        self._block_bad_bots: Optional[bool] = None
        self._regions: Optional[List[str]] = None

    def label(self, label: str) -> "UpdatePushZoneData":
        """
        The user-supplied label.

        Args:
            label (str): The user-supplied label.

        Returns:
            UpdatePushZoneData: The current object with the label set.
        """
        self._label = label
        return self

    def vanity_domain(self, vanity_domain: str) -> "UpdatePushZoneData":
        """
        An optional domain name that can be used to access the cached files.

        Args:
            vanity_domain (str): The vanity domain to use.

        Returns:
            UpdatePushZoneData: The current object with the vanity domain set.
        """
        self._vanity_domain = vanity_domain
        return self

    def ssl_cert(self, ssl_cert: str) -> "UpdatePushZoneData":
        """
        Base 64 encoded SSL certificate (required if vanity_domain)

        Args:
            ssl_cert (str): Base64 encoded SSL certificate.

        Returns:
            UpdatePushZoneData: The current object with the SSL certificate set.
        """
        self._ssl_cert = ssl_cert
        return self

    def ssl_cert_key(self, ssl_cert_key: str) -> "UpdatePushZoneData":
        """
        Base 64 encoded SSL private key (required if vanity_domain)

        Args:
            ssl_cert_key (str): Base64 encoded SSL private key.

        Returns:
            UpdatePushZoneData: The current object with the SSL private key set.
        """
        self._ssl_cert_key = ssl_cert_key
        return self

    def cors(self, cors: bool) -> "UpdatePushZoneData":
        """
        Cross-origin resource sharing

        Args:
            cors (bool): Whether to enable CORS.

        Returns:
            UpdatePushZoneData: The current object with the CORS setting set.
        """
        self._cors = cors
        return self

    def gzip(self, gzip: bool) -> "UpdatePushZoneData":
        """
        Optional feature to compress files

        Args:
            gzip (bool): Whether to enable Gzip compression.

        Returns:
            UpdatePushZoneData: The current object with the Gzip compression setting set.
        """
        self._gzip = gzip
        return self

    def block_ai(self, block_ai: bool) -> "UpdatePushZoneData":
        """
        Optional feature to block AI bots

        Args:
            block_ai (bool): Whether to block AI bots.

        Returns:
            UpdatePushZoneData: The current object with the AI bot blocking setting set.
        """
        self._block_ai = block_ai
        return self

    def block_bad_bots(self, block_bad_bots: bool) -> "UpdatePushZoneData":
        """
        Optional feature to block malicious bots

        Args:
            block_bad_bots (bool): Whether to block potentially malicious bots.

        Returns:
            UpdatePushZoneData: The current object with the potentially malicious bot blocking setting set.
        """
        self._block_bad_bots = block_bad_bots
        return self

    def regions(self, regions: List[str]) -> "UpdatePushZoneData":
        """
        List of [Region ids](#operation/list-regions) for content delivery

        Args:
            regions (List[str]): List of region IDs.

        Returns:
            UpdatePushZoneData: The current object with the region list set.
        """
        self._regions = regions
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "label": self._label,
            "vanity_domain": self._vanity_domain,
            "ssl_cert": self._ssl_cert,
            "ssl_cert_key": self._ssl_cert_key,
            "cors": self._cors,
            "gzip": self._gzip,
            "block_ai": self._block_ai,
            "block_bad_bots": self._block_bad_bots,
            "regions": self._regions,
        }
        return {k: v for k, v in data.items() if v is not None}


class CreatePushZoneFileData:
    def __init__(self, name: str, size: int):
        """
        Data structure used for creating a presigned post endpoint for uploading a file to a Vultr CDN Push Zone

        Args:
            name (str): The name of the file including extension.
            size (int): The size of the file in bytes.
        """
        self._name: str = name
        self._size: int = size

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "name": self._name,
            "size": self._size
        }