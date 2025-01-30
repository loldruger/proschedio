from typing import List, Literal, Optional
from vultr.structs import instances as data
from vultr.apis import instances as api

class Vultr:
    def __init__(self):
        self.failiure_policy: Literal["continue", "stop", "retry", "rollback"] = "stop"
        self.retry_interval: int = 300
        self.retry_attempts: int = 3

        self.instance: List[VultrInstance] = []
    
    def __str__(self) -> str:
        return str({
            "failiure_policy": self.failiure_policy,
            "retry_interval": self.retry_interval,
            "retry_attempts": self.retry_attempts,
            "instance": self.instance
        })
    
    def set_failiure_policy(self, policy: Literal["continue", "stop", "retry", "rollback"]) -> 'Vultr':
        self.failiure_policy = policy
        return self

    def set_retry_policy(self, interval: int, attempts: int) -> 'Vultr':
        self.retry_interval = interval
        self.retry_attempts = attempts

        return self

    def new_instance(self, data: data.CreateInstanceData) -> 'VultrInstance':
        instance = VultrInstance(parent=self, data=data)
        self.instance.append(instance)

        return instance
    
    def delete_instance(self, instance_id: str) -> 'Vultr':
        pass

class VultrInstance:
    def __init__(self, parent: Vultr, data: data.CreateInstanceData):
        self.parent = parent
        self.data = data
        self.block_storage: List[str] = []

    def __str__(self) -> str:
        return str({
            "data": self.data.to_json(),
            "block_storage": self.block_storage
        })

    def attatch_block_storage(self, block_storage_id: str) -> 'VultrInstance':
        self.block_storage.append(block_storage_id)
        return self
    
    def detach_block_storage(self, block_storage_id: str) -> 'VultrInstance':
        self.block_storage.remove(block_storage_id)
        return self
    
    def apply(self) -> 'Vultr':
        return self.parent


