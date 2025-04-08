import asyncio
import time
import logging
from typing import List, Literal, Optional
from vultr.structs.instances import CreateInstanceData, Instance
from vultr.apis.instances import create_instance, get_instance
from proschedio.resources.instance import BaseInstance

logger = logging.getLogger(__name__)

class InstanceBuilder:
    def __init__(self, data: CreateInstanceData, failure_policy: str, retry_policy: dict):
        self._data = data
        self._failure_policy = failure_policy
        self._retry_policy = retry_policy

    async def _wait_for_ready(self, instance_id: str, timeout: int, interval: int) -> Instance:
        """Polls the instance status until it's active and ok, or until timeout.

        Returns:
            Instance: The final Instance object upon success.
        """
        start_time = time.monotonic()
        logger.info(f"Waiting for instance {instance_id} to become ready (timeout={timeout}s, interval={interval}s)...")
        while time.monotonic() - start_time < timeout:
            try:
                response = await get_instance(instance_id=instance_id)
                if response.get("status") != 200:
                    logger.warning(f"Polling instance {instance_id}: Received status {response.get('status')}. Retrying...")
                    await asyncio.sleep(interval)
                    continue

                instance_data = response.get("data", {}).get("instance", {})
                if not instance_data:
                    logger.warning(f"Polling instance {instance_id}: 'instance' data not found in response. Retrying...")
                    await asyncio.sleep(interval)
                    continue

                current_instance = Instance.from_dict(instance_data)
                logger.debug(f"Polling instance {instance_id}: status='{current_instance.status}', server_status='{current_instance.server_status}'")

                if current_instance.status == "active" and current_instance.server_status == "ok":
                    logger.info(f"Instance {instance_id} is ready.")
                    return current_instance

            except Exception as e:
                logger.error(f"Error polling instance {instance_id}: {e}", exc_info=True)

            await asyncio.sleep(interval)

        raise TimeoutError(f"Instance {instance_id} did not become ready within {timeout} seconds.")

    async def apply(self, wait: bool = False, timeout: int = 300, interval: int = 10) -> BaseInstance:
        """
        Applies the instance creation request.

        Args:
            wait: If True, waits for the instance to become fully active before returning.
            timeout: Maximum time in seconds to wait if wait=True.
            interval: Interval in seconds between status checks if wait=True.

        Returns:
            BaseInstance: An object implementing the BaseInstance interface, representing the created resource.
        """
        logger.info(f"Applying instance creation with data: {self._data.to_json()}, wait={wait}")
        try:
            create_response = await create_instance(self._data)
            logger.debug(f"Initial API call result: {create_response}")

            if create_response.get("status") != 202:
                raise Exception(f"Instance creation failed with status {create_response.get('status')}: {create_response.get('data')}")

            instance_data = create_response.get("data", {}).get("instance", {})
            if not instance_data:
                raise Exception("Could not get instance data from creation response.")

            initial_instance = Instance.from_dict(instance_data)
            if not initial_instance.id:
                 raise Exception("Could not get instance ID from creation response.")

            if wait:
                final_instance = await self._wait_for_ready(initial_instance.id, timeout, interval)
                return final_instance
            else:
                logger.info(f"Instance creation initiated (apply called with wait=False): {initial_instance}")
                return initial_instance

        except Exception as e:
            logger.error(f"Error during instance apply: {e}", exc_info=True)
            raise

class Vultr:
    def __init__(self):
        self._failure_policy: Literal["fail", "retry"] = "fail"
        self._retry_policy: dict = {"interval": 0, "attempts": 0}
        self.instance_builders: List[InstanceBuilder] = []

    def __str__(self) -> str:
        return str({
            "failiure_policy": self._failure_policy,
            "retry_interval": self._retry_policy["interval"],
            "retry_attempts": self._retry_policy["attempts"],
        })

    def set_failure_policy(self, policy: Literal["fail", "retry"]) -> 'Vultr':
        self._failure_policy = policy
        print(f"Set failure policy to: {policy}")
        return self

    def set_retry_policy(self, interval: int, attempts: int) -> 'Vultr':
        self._retry_policy = {"interval": interval, "attempts": attempts}
        print(f"Set retry policy to: interval={interval}, attempts={attempts}")
        return self

    def new_instance(self, data: CreateInstanceData) -> InstanceBuilder:
        logger.info("Creating InstanceBuilder...")
        builder = InstanceBuilder(data, self._failure_policy, self._retry_policy)
        self.instance_builders.append(builder)
        return builder


