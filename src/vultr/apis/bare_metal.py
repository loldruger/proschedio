from http import HTTPMethod
from proschedio import composer
from vultr import const, get_key
from vultr.structs.bare_metal import BareMetalCreateData, BareMetalUpdateData

async def get_instances(per_page: int, cursor: str):
    return await composer.Request(const.URL_BARE_METAL)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_param("per_page", per_page)\
        .add_param("cursor", cursor)\
        .request()

async def create_instance(data: BareMetalCreateData):
    return await composer.Request(const.URL_BARE_METAL)\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body(data.to_json())\
        .request()

async def get_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def update_by_id(baremetal_id: str, data: BareMetalUpdateData):
    return await composer.Request(const.URL_BARE_METAL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.PATCH)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body(data)\
        .request()

async def delete_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.DELETE)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_ipv4_addresses_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_IPV4.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_ipv6_addresses_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_IPV6.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bear {get_key()}")\
        .request()

async def create_ipv4_reverse_by_id(baremetal_id: str, ip: str, reverse: str):
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

async def delete_ipv6_reverse_by_id(baremetal_id: str, ipv6: str):
    return await composer.Request(const.URL_BARE_METAL_IPV6_REVERSE_IPV6.assign("baremetal-id", baremetal_id).assign("ipv6", ipv6))\
        .set_method(HTTPMethod.DELETE)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_param("ip", ipv6)\
        .request()

async def start_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_START.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bear {get_key()}")\
        .request()

async def reboot_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_REBOOT.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def reinstall_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_REINSTALL.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def halt_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_HALT.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_bandwidth_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METAL_BANDWIDTH.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def start_by_ids(baremetal_ids: list[str]):
    return await composer.Request(const.URL_BARE_METALS_START)\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "baremetal_ids": baremetal_ids
        })\
        .request()

async def reboot_by_ids(baremetal_ids: list[str]):
    return await composer.Request(const.URL_BARE_METALS_REBOOT)\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "baremetal_ids": baremetal_ids
        })\
        .request()

async def halt_by_ids(baremetal_ids: list[str]):
    return await composer.Request(const.URL_BARE_METALS_HALT)\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "baremetal_ids": baremetal_ids
        })\
        .request()

async def get_user_data_by_ids(baremetal_ids: list[str]):
    return await composer.Request(const.URL_BARE_METALS_USER_DATA)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "baremetal_ids": baremetal_ids
        })\
        .request()

async def get_available_upgrades_by_ids(baremetal_ids: list[str]):
    return await composer.Request(const.URL_BARE_METALS_ID_AVAILABLE_UPGRADES)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "baremetal_ids": baremetal_ids
        })\
        .request()

async def get_vnc_by_id(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METALS_ID_VNC.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def attach_vpc(baremetal_id: str, vpc_id: str):
    return await composer.Request(const.URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "vpc_id": vpc_id
        })\
        .request()

async def detach_vpc(baremetal_id: str, vpc_id: str):
    return await composer.Request(const.URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "vpc_id": vpc_id
        })\
        .request()

async def get_vpc_attached_list(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METALS_VPCS.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def attach_vpc2(baremetal_id: str, vpc_id: str, ip_address: str):
    return await composer.Request(const.URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "vpc_id": vpc_id,
            "ip_address": ip_address
        })\
        .request()

async def detach_vpc2(baremetal_id: str, vpc_id: str):
    return await composer.Request(const.URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.POST)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "vpc_id": vpc_id
        })\
        .request()

async def get_vpc2_attached_list(baremetal_id: str):
    return await composer.Request(const.URL_BARE_METALS_VPCS2.assign("baremetal-id", baremetal_id))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()