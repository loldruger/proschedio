from typing import List, Literal, Optional
from vultr.structs import instances as data
from vultr.apis import instances as api
from vultr.apis.instances import create_instance
from vultr.structs.instances import CreateInstanceData

class InstanceBuilder:
    def __init__(self, data: CreateInstanceData, failure_policy: str, retry_policy: dict):
        self._data = data
        self._failure_policy = failure_policy
        self._retry_policy = retry_policy

    async def apply(self):
        """
        Applies the instance creation request by calling the API.
        Handles retries based on the policy (basic implementation).
        """
        print(f"Applying instance creation with data: {self._data.to_json()}")
        try:
            result = await create_instance(self._data)
            print(f"API call result: {result}")
            return result
        except Exception as e:
            print(f"Error during API call: {e}")
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
        print("Creating InstanceBuilder...")
        builder = InstanceBuilder(data, self._failure_policy, self._retry_policy)
        self.instance_builders.append(builder)
        return builder


