from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Type

class BaseResource(ABC):
    """
    Abstract base class for all cloud resources managed by Proschedio.
    Each specific resource type (e.g., Instance, BlockStorage) across different
    providers should inherit from this or a more specialized base class.
    """

    def __init__(self, provider: Any, id: Optional[str] = None, **kwargs: Any):
        """
        Initializes the base resource.

        Args:
            provider: An instance of the provider client (e.g., VultrProvider).
            id (Optional[str]): The existing ID of the resource, if known.
            **kwargs (Any): Configuration properties for the resource.
        """
        self._provider = provider
        self._config_kwargs = kwargs 
        self._id: Optional[str] = id 
        self._properties: Dict[str, Any] = {} # Resource properties after creation/fetch

    @property
    def id(self) -> Optional[str]:
        """The unique identifier of the resource."""
        return self._id

    @property
    def properties(self) -> Dict[str, Any]:
        """The properties of the resource fetched from the provider."""
        return self._properties

    @property
    @abstractmethod
    def resource_type(self) -> str:
        """A string identifying the type of the resource (e.g., 'instance', 'block_storage')."""
        pass

    @abstractmethod
    async def create(self) -> 'BaseResource':
        """Creates the resource on the cloud provider using stored kwargs."""
        pass

    @abstractmethod
    async def delete(self) -> None:
        """Deletes the resource from the cloud provider using the stored ID."""
        pass

    @abstractmethod
    async def get(self) -> Optional['BaseResource']:
        """Fetches the current state of the resource from the cloud provider using the stored ID."""
        pass

    # Optional common methods
    # @abstractmethod
    # async def update(self, properties: Dict[str, Any]) -> 'BaseResource':
    #     pass
