from http import HTTPMethod
from proschedio import composer
from vultr import const, get_key
from vultr.structs.bare_metal import BareMetalCreateData, BareMetalUpdateData

async def get_bare_metal_instances(per_page: int, cursor: str):
    return await composer.Request(const.URL_BARE_METAL)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_param("per_page", per_page)\
        .add_param("cursor", cursor)\
        .request()

async def create_bare_metal_instance(data: BareMetalCreateData):
    """
    Create a new Bare Metal Instance in a `region` with the desired `plan`.\n
    Choose one of the following to deploy the instance:
    - os_id
    - snapshot_id
    - app_id
    - image_id

    Supply other attributes as desired.
    """
    return await composer.Request(const.URL_BARE_METAL)\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body(data.to_json())\
        .request()

async def get_bare_metal_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def update_bare_metal_by_id(baremetal_id: str, data: BareMetalUpdateData):
    return await composer.Request(const.URL_BARE_METAL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.PATCH)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body(data)\
        .request()

async def delete_bare_metal_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.DELETE)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_bare_metal_ipv4_addresses_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_IPV4.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_bare_metal_ipv6_addresses_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_IPV6.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bear {get_key()}")\
        .request()

async def create_bare_metal_ipv4_reverse_by_id(baremetal_id: str, ip: str, reverse: str):
    return await composer.Request(const.URL_BARE_METAL_IPV4_REVERSE.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "ip": ip,
            "reverse": reverse
        })\
        .request()

async def set_default_reverse_dns_by_id(baremetal_id: str, ipv4: str):
    return await composer.Request(const.URL_BARE_METAL_IPV4_REVERSE_DEFAULT.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "ip": ipv4
        })\
        .request()

async def delete_bare_metal_ipv6_reverse_by_id(baremetal_id: str, ipv6: str):
    return await composer.Request(const.URL_BARE_METAL_IPV6_REVERSE_IPV6.assign("baremetal-id", baremetal_id).assign("ipv6", ipv6))\
        .set_method(HTTPMethod.DELETE)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_param("ip", ipv6)\
        .request()

async def start_bare_metal_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_START.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bear {get_key()}")\
        .request()