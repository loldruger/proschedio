from typing import Optional, List, Literal, Dict, Any
import time
import asyncio

# Import the base class
from proschedio.resources.instance import BaseInstance
# Import Vultr API functions needed for implementation
from vultr.apis import instances as vultr_instance_api
# Import the CreateInstanceData struct from its new location
# This is needed internally by the create method
from proschedio.apiV2.structs.instance import CreateInstanceData

class Instance(BaseInstance):
    """Represents a Vultr VPS Instance resource, implementing the BaseInstance interface."""

    def __init__(self, provider: Any, id: Optional[str] = None, **kwargs: Any):
        super().__init__(provider=provider, id=id, **kwargs)
        self._raw_data: Dict[str, Any] = {}

    async def create(self) -> 'Instance':
        """Creates the Vultr instance based on the stored kwargs."""
        config = self._config_kwargs

        if 'region' not in config or 'plan' not in config:
            raise ValueError("Missing required parameters 'region' or 'plan' for instance creation.")

        create_data = CreateInstanceData(region=config['region'], plan=config['plan'])
        if 'os_id' in config: create_data.os_id(config['os_id'])
        if 'hostname' in config: create_data.hostname(config['hostname'])
        if 'label' in config: create_data.label(config['label'])
        if 'tags' in config: create_data.tags(config['tags'])
        if 'backups' in config: create_data.backups(config['backups'])
        if 'ddos_protection' in config: create_data.ddos_protection(config['ddos_protection'])

        response = await vultr_instance_api.create_instance(create_data)

        if response.get("status") != 202:
            raise Exception(f"Vultr instance creation failed: {response}")

        instance_info = response.get("data", {}).get("instance", {})
        if not instance_info or not instance_info.get("id"):
            raise Exception("Could not get instance details from creation response")

        self._id = instance_info.get("id")
        self._raw_data = instance_info
        self._properties = instance_info

        if config.get('wait_for_ready', False):
            await self._wait_until_ready(
                timeout=config.get('wait_timeout', 300),
                interval=config.get('wait_interval', 10)
            )
            await self.get()

        return self

    async def delete(self) -> None:
        """Deletes the Vultr instance using the stored ID."""
        if not self.id:
            raise ValueError("Cannot delete resource without an ID.")
        response = await vultr_instance_api.delete_instance(instance_id=self.id)
        if response.get("status") != 204:
            raise Exception(f"Vultr instance deletion failed for ID {self.id}: {response}")
        self._id = None
        self._properties = {}
        self._raw_data = {}

    async def get(self) -> Optional['Instance']:
        """Fetches the current state of the Vultr instance using the stored ID."""
        if not self.id:
            raise ValueError("Cannot get resource without an ID.")

        response = await vultr_instance_api.get_instance(instance_id=self.id)
        if response.get("status") == 404:
            self._id = None
            self._properties = {}
            self._raw_data = {}
            return None
        if response.get("status") != 200:
            raise Exception(f"Failed to get Vultr instance {self.id}: {response}")

        instance_info = response.get("data", {}).get("instance", {})
        if not instance_info:
             raise Exception(f"Instance data missing in get response for {self.id}")

        self._raw_data = instance_info
        self._properties = instance_info
        self._id = instance_info.get("id")
        return self

    @property
    def status(self) -> Optional[str]:
        return self._properties.get("status")

    @property
    def region(self) -> Optional[str]:
        return self._properties.get("region")

    @property
    def main_ip(self) -> Optional[str]:
        return self._properties.get("main_ip")

    @property
    def hostname(self) -> Optional[str]:
        return self._properties.get("hostname")

    @property
    def label(self) -> Optional[str]:
        return self._properties.get("label")

    @property
    def plan(self) -> Optional[str]:
        return self._properties.get("plan")

    @property
    def date_created(self) -> Optional[str]:
        return self._properties.get("date_created")

    @property
    def tags(self) -> Optional[List[str]]:
        return self._properties.get("tags")

    @property
    def provider_specific_data(self) -> Dict[str, Any]:
        return self._raw_data

    async def _wait_until_ready(self, timeout: int, interval: int):
        """Internal helper to wait for instance to become active."""
        if not self.id:
            return

        start_time = time.monotonic()
        while time.monotonic() - start_time < timeout:
            await asyncio.sleep(interval)
            instance_state = await self.get()
            if instance_state and instance_state.status == "active" and instance_state._properties.get("server_status") == "ok":
                print(f"Instance {self.id} is ready.")
                return
            print(f"Waiting for instance {self.id}... Current status: {instance_state.status if instance_state else 'N/A'}")

        raise TimeoutError(f"Instance {self.id} did not become ready within {timeout} seconds.")

    @property
    def server_status(self) -> Optional[str]:
        return self._properties.get("server_status")

    def __str__(self) -> str:
        return f"VultrInstance(id={self.id}, status={self.status}, region={self.region}, ip={self.main_ip})"

    def __repr__(self) -> str:
        return self.__str__()