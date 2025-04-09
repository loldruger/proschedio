# src/proschedio/apiV2/actions/instance.py
# Functions related to specific actions performed on Vultr instances.

import json
import logging
import os
from http import HTTPMethod
from typing import Optional, List, Literal

from const import ProviderRegistry, ProviderUrl
from request import Request, RequestReturnType

from ..dataclass import instance as instance_structs

logger = logging.getLogger(__name__)


class Action:
    @staticmethod
    def instance(provider_url: ProviderUrl)-> 'ActionInstance':
        return ActionInstance(provider_url)

class ActionInstance:
    def __init__(self, provider_url: ProviderUrl):
        self.provider_url = provider_url

    async def reinstall_instance(self, instance_id: str, hostname: Optional[str]) -> RequestReturnType:
        """
        Reinstall a Vultr Instance using an optional `hostname`. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_reinstall(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json")

        if hostname is not None:
            request.set_body(json.dumps({"hostname": hostname}))
        
        return await request.request()

    async def get_instance_bandwidth(self, instance_id: str, date_range: Optional[int]) -> RequestReturnType:
        """
        Get bandwidth information about a Vultr Instance. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_bandwidth(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if date_range is not None:
            request.add_param("date_range", date_range)
        
        return await request.request()

    async def get_instance_neighbors(self, instance_id: str) -> RequestReturnType:
        """
        Get a list of other instances in the same location as this Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_neighbors(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def list_instance_vpcs(self, instance_id: str, per_page: Optional[int], cursor: Optional[str]) -> RequestReturnType:
        """
        List the VPCs for a Vultr Instance. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_vpcs(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", per_page)
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    async def get_instance_iso_status(self, instance_id: str) -> RequestReturnType:
        """
        Get the ISO status for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_iso(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def attach_instance_iso(self, instance_id: str, iso_id: str) -> RequestReturnType:
        """
        Attach an ISO to a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_iso_attach(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"iso_id": iso_id})) \
            .request()

    async def detach_instance_iso(self, instance_id: str) -> RequestReturnType:
        """
        Detach the ISO from a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_iso_detach(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .set_body(json.dumps({})) \
            .request()

    async def attach_instance_vpc(self, instance_id: str, vpc_id: str) -> RequestReturnType:
        """
        Attach a VPC to a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_vpcs_attach(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"vpc_id": vpc_id})) \
            .request()

    async def detach_instance_vpc(self, instance_id: str, vpc_id: str) -> RequestReturnType:
        """
        Detach a VPC from a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_vpcs_detach(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"vpc_id": vpc_id})) \
            .request()

    async def get_instance_backup_schedule(self, instance_id: str) -> RequestReturnType:
        """
        Get the backup schedule for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_backup_schedule(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def set_instance_backup_schedule(self, instance_id: str, data: instance_structs.SetInstanceBackupScheduleData) -> RequestReturnType:
        """
        Set the backup schedule for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_backup_schedule(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(data.to_json()) \
            .request()

    async def restore_instance(self, instance_id: str, backup_id: Optional[str], snapshot_id: Optional[str]) -> RequestReturnType:
        """
        Restore a Vultr Instance from a backup or snapshot. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_restore(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json")

        if backup_id is not None:
            request.set_body(json.dumps({"backup_id": backup_id}))
        elif snapshot_id is not None:
            request.set_body(json.dumps({"snapshot_id": snapshot_id}))
        # else: # Consider raising an error if neither is provided
        #     raise ValueError("Either backup_id or snapshot_id must be provided for restore.")

        return await request.request()

    async def list_instance_ipv4(self, instance_id: str, public_network: Optional[bool], per_page: Optional[int], cursor: Optional[str]) -> RequestReturnType:
        """
        List the IPv4 information for a Vultr Instance. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_ipv4(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if public_network is not None:
            request.add_param("public_network", public_network)
        if per_page is not None:
            request.add_param("per_page", per_page)
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    async def create_instance_ipv4(self, instance_id: str, reboot: Optional[bool]) -> RequestReturnType:
        """
        Create an IPv4 address for a Vultr Instance. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_ipv4(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json")
        
        if reboot is not None:
            request.set_body(json.dumps({"reboot": reboot}))

        return await request.request()

    async def get_instance_ipv6(self, instance_id: str) -> RequestReturnType:
        """
        Get the IPv6 information for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_ipv6(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def create_instance_reverse_ipv4(self, instance_id: str, ip: str, reverse: str) -> RequestReturnType:
        """
        Create a reverse IPv4 entry for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_ipv4_reverse(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"ip": ip, "reverse": reverse})) \
            .request()

    async def list_instance_reverse_ipv6(self, instance_id: str) -> RequestReturnType:
        """
        List the reverse IPv6 information for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_ipv6_reverse(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def create_instance_reverse_ipv6(self, instance_id: str, ip: str, reverse: str) -> RequestReturnType:
        """
        Create a reverse IPv6 entry for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_ipv6_reverse(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"ip": ip, "reverse": reverse})) \
            .request()

    async def set_instance_reverse_ipv4(self, instance_id: str, ip: str) -> RequestReturnType:
        """
        Set a reverse DNS entry for an IPv4 address of a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_ipv4_reverse_default(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"ip": ip})) \
            .request()

    async def delete_instance_reverse_ipv6(self, instance_id: str, ipv6: str) -> RequestReturnType:
        """
        Delete the reverse IPv6 for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_ipv6_reverse_by_ipv6(self.provider_url).assign("instance-id", instance_id).assign("ipv6", ipv6)) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def halt_instance(self, instance_id: str) -> RequestReturnType:
        """
        Halt a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_halt(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def get_instance_user_data(self, instance_id: str) -> RequestReturnType:
        """
        Get the user data for a Vultr Instance. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_user_data(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    async def get_instance_upgrades(self, instance_id: str, type: Optional[Literal["all", "applications", "os", "plans"]]) -> RequestReturnType:
        """
        Get available upgrades for a Vultr Instance. (Vultr specific)
        """
        request = Request(ProviderRegistry.get_url_instance_upgrades(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if type is not None:
            request.add_param("type", type)

        return await request.request()

    async def reboot_instances(self, instance_ids: List[str]) -> RequestReturnType:
        """
        Reboot multiple Vultr Instances. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_reboot()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"instance_ids": instance_ids})) \
            .request()

    async def start_instances(self, instance_ids: List[str]) -> RequestReturnType:
        """
        Start multiple Vultr Instances. (Vultr specific)
        """
        return await Request(ProviderRegistry.get_url_instance_start()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"instance_ids": instance_ids})) \
            .request()

# Note: Deprecated functions related to private networks and vpc2 are omitted.
