from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

class BaseInstance(ABC):
    """
    Abstract base class for resources.
    """

    def __init__(self, provider: str, **kwargs: Any):
        self._provider = provider
        self._id = id
        self._config_kwargs = kwargs
        self._properties: dict[str, Any] = {}
        self._raw_data: dict[str, Any] = {}

    @property
    def id(self) -> Callable[[object], int]:
        return self._id

    @property
    def provider(self) -> str:
        return self._provider
    
    @property
    @abstractmethod
    def status(self) -> str | None:
        pass

    @property
    @abstractmethod
    def region(self) -> str | None:
        pass

    @property
    @abstractmethod
    def main_ip(self) -> str | None:
        pass

    @property
    @abstractmethod
    def provider_specific_data(self) -> dict[str, Any]:
        pass

    @abstractmethod
    async def create(self) -> 'BaseInstance':
        pass

    @abstractmethod
    async def delete(self) -> str | None:
        pass

    @abstractmethod
    async def get(self) -> 'BaseInstance | None':
        pass

    @abstractmethod
    async def reboot(self) -> str | None:
        pass

    @abstractmethod
    async def start(self) -> str | None:
        pass

    @abstractmethod
    async def halt(self) -> str | None:
        pass

    @abstractmethod
    async def execute_action(self, action_name: str, **kwargs: Any) -> Any:
        """
        Executes a provider-specific action.

        Args:
            action_name (str): The name of the action to execute (e.g., 'reinstall', 'set_backup_schedule').
            **kwargs: Parameters required by the specific action.

        Returns:
            Any: The result of the action, if any.

        Raises:
            NotImplementedError: If the action_name is not supported by the provider.
            ValueError: If required kwargs are missing or invalid.
        """
        pass