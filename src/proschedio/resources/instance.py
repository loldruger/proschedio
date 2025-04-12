import os
import logging
from http import HTTPMethod
from typing import Any

from ..const import ProviderUrl
from ..request import Request, RequestReturnType
from src.proschedio.resources.instance_base import BaseInstance
from .instance_config import InstanceConfig
from ..dataclass import instance as instance_structs

logger = logging.getLogger(__name__)

class Resource:
    @staticmethod
    def instance(provider: str, region: str, plan: str, config: InstanceConfig) -> 'ResourceInstance':
        return ResourceInstance(provider=provider, region=region, plan=plan, config=config)
        
class ResourceInstance(BaseInstance):
    def __init__(self, provider: str, region: str, plan: str, config: InstanceConfig):
        self.provider = provider
        self.region = region
        self.plan = plan
        self.config = config

    async def list(self, filters: instance_structs.ListInstancesData | None) -> RequestReturnType:
        """
        List all VPS instances in your account.
        """
        request = Request(ProviderUrl.get_url_instances(self.provider_url)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}")

        if filters is not None:
            # Apply filters using the filter object's method
            filters.apply_params(request)

        return await request.request()

    async def create(self) -> RequestReturnType:
        """
        Create a new Vultr VPS Instance.
        """
        return await Request(ProviderUrl.get_url_instances_base(self.provider_url)) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
            .add_header("Content-Type", "application/json") \
            .set_body(self.config) \
            .request()

    async def get(self, instance_id: str) -> RequestReturnType:
        """
        Get information about a Vultr Instance.
        """
        return await Request(ProviderUrl.get_url_instance_by_id(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
            .request()

    async def update(self, instance_id: str, data: instance_structs.UpdateInstanceData) -> RequestReturnType:
        """
        Update information for a Vultr Instance.
        """
        return await Request(ProviderUrl.get_url_instance_by_id(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
            .add_header("Content-Type", "application/json") \
            .set_body(self.config) \
            .request()

    async def delete(self, instance_id: str) -> RequestReturnType:
        """
        Delete a Vultr Instance.
        """
        return await Request(ProviderUrl.get_url_instance_by_id(self.provider_url).assign("instance-id", instance_id)) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
            .request()
    
    async def reboot(self) -> str | None:
        raise NotImplementedError

    async def start(self) -> str | None:
        raise NotImplementedError

    async def halt(self) -> str | None:
        raise NotImplementedError

    async def execute_action(self, action_name: str, **kwargs: Any) -> Any:
        raise NotImplementedError
    
    @property
    def id(self) -> str | None:
        raise NotImplementedError

    @property
    def status(self) -> str | None:
        raise NotImplementedError

    @property
    def region(self) -> str | None:
        raise NotImplementedError

    @property
    def main_ip(self) -> str | None:
        raise NotImplementedError

    @property
    def hostname(self) -> str | None:
        raise NotImplementedError

    @property
    def label(self) -> str | None:
        raise NotImplementedError

    @property
    def plan(self) -> str | None:
        raise NotImplementedError

    @property
    def date_created(self) -> str | None:
        raise NotImplementedError

    @property
    def tags(self) -> instance_structs.List[str] | None:
        raise NotImplementedError

    @property
    def provider_specific_data(self) -> dict[str, Any]:
        raise NotImplementedError
