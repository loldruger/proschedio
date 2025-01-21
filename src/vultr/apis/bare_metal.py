from http import HTTPMethod
import json
from typing import Optional
from proschedio import composer
from vultr import const, get_key

async def get_bare_metal_instances(per_page: int, cursor: str):
    return await composer.Request(const.URL_BARE_METAL)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_param("per_page", per_page)\
        .add_param("cursor", cursor)\
        .request()

class BareMetalInstance:
    def __init__(self, region: str, plan: str):
        self.region: str = region
        self.plan: str = plan
        self.script_id: Optional[str] = None
        self.enable_ipv6: Optional[bool] = None
        self.sshkey_id: Optional[list][str] = None
        self.user_data: Optional[str] = None
        self.label: Optional[str] = None
        self.activation_email: Optional[bool] = None
        self.hostname: Optional[str] = None
        self.reserved_ipv4: Optional[str] = None
        self.os_id: Optional[int] = -None
        self.snapshot_id: Optional[str] = None
        self.app_id: Optional[int] = -None
        self.image_id: Optional[str] = None
        self.persistent_pxe: Optional[bool] = None
        self.attach_vpc2: Optional[list][str] = None
        self.detach_vpc2: Optional[list][str] = None
        self.enable_vpc2: Optional[bool] = None
        self.tags: Optional[list][str] = None
        self.user_scheme: Optional[str] = None
        self.mdisk_mode: Optional[str] = None
        self.app_variables: Optional[dict] = None

    def __str__(self) -> str:
        data = {
            "region": self.region,
            "plan": self.plan,
            "script_id": self.script_id,
            "enable_ipv6": self.enable_ipv6,
            "sshkey_id": self.sshkey_id,
            "user_data": self.user_data,
            "label": self.label,
            "activation_email": self.activation_email,
            "hostname": self.hostname,
            "reserved_ipv4": self.reserved_ipv4,
            "os_id": self.os_id,
            "snapshot_id": self.snapshot_id,
            "app_id": self.app_id,
            "image_id": self.image_id,
            "persistent_pxe": self.persistent_pxe,
            "attach_vpc2": self.attach_vpc2,
            "detach_vpc2": self.detach_vpc2,
            "enable_vpc2": self.enable_vpc2,
            "tags": self.tags,
            "user_scheme": self.user_scheme,
            "mdisk_mode": self.mdisk_mode,
            "app_variables": self.app_variables,
        }
        filtered_data = {k: v for k, v in data.items() if v is not None}
        return json.dumps(filtered_data)

async def create_bare_metal_instance(data: dict):
    return await composer.Request(const.URL_BARE_METAL)\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body(data)\
        .request()

