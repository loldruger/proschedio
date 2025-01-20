import aiohttp

from typing import Final
from enum import IntEnum, auto
from http import HTTPMethod

class Provider(IntEnum):
    VULTR = auto()
    CUSTOM = auto()

    def __str__(self) -> str:
        match self:
            case Provider.VULTR:
                return "https://api.vultr.com/v2/"
            case Provider.CUSTOM:
                return "https://api.custom.com/v2/"
            case _:
                raise ValueError("Invalid provider")

class Url:
    def __init__(self, provider: Provider):
        self._provider = provider
        self._uri = ""
    
    def uri(self, token: str) -> 'Url':
        self._uri = token

        return self
    
    def assign(self, placeholder: str, value: str) -> 'Url':
        self._uri = self._uri.replace(f"{{{placeholder}}}", value)

        return self
    
    def to_str(self) -> str:
        return str(self._provider) + self._uri

class Request:
    def __init__(self, url: Url):
        self._url = url.to_str()
        self._method = None
        self._headers = {}
        self._params = {}
        self._body = None

    def set_method(self, method: HTTPMethod) -> 'Request':
        self._method = str(method)

        return self
    
    def add_header(self, key: str, value: str) -> 'Request':
        self._headers[key] = value

        return self
    
    def add_param(self, key: str, value: str) -> 'Request':
        self._params[key] = value

        return self
    
    def set_body(self, body: dict) -> 'Request':
        self._body = body

        return self
    
    async def request(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=self._method,
                url=self._url,
                headers=self._headers,
                params=self._params,
                json=self._body
            ) as response:
                return await response.json()
    

URL_ACCOUNT_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("account/bandwidth")

URL_APPLICATIONS: Final[Url] = Url(Provider.VULTR).uri("applications")

URL_BACKUPS: Final[Url] = Url(Provider.VULTR).uri("backups")

URL_BARE_METAL_IP4: Final[Url] = Url(Provider.VULTR).uri("bare-metal/{baremetal-id}/ipv4")
URL_BARE_METAL_IP6: Final[Url] = Url(Provider.VULTR).uri("bare-metal/{baremetal-id}/ipv6")

URL_ACCOUNT: Final[Url] = Url(Provider.VULTR).uri("account")

REQUEST_ACCOUNT: Final[Request] = Request(URL_ACCOUNT)\
    .set_method(HTTPMethod.GET)\
    .add_header("Authorization", "Bearer {token}")\
    .add_header("Content-Type", "application/json")\
    .set_body({
        "key": "value"
    })\
    .request()