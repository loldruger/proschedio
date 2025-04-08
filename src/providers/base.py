from abc import ABC, abstractmethod
from typing import Dict, Any, Type

# Forward reference for type hinting
from ..resources.base import BaseResource
from ..resources.instance import BaseInstance
# Import other base resource types as they are defined
# from ..resources.block_storage import BaseBlockStorage

class BaseProvider(ABC):
    """
    Abstract base class for all cloud provider integrations.
    Responsible for authenticating and interacting with a specific cloud provider's API
    and managing the lifecycle of resources for that provider.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the provider with necessary configuration (e.g., API keys).

        Args:
            config (Dict[str, Any]): Provider-specific configuration.
        """
        self._config = config
        self._authenticate()

    @abstractmethod
    def _authenticate(self) -> None:
        """Handles provider-specific authentication."""
        pass

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Returns the name of the cloud provider (e.g., 'vultr', 'aws')."""
        pass

    # --- Resource Factory Methods --- 
    # These methods instantiate the provider-specific resource classes.

    @abstractmethod
    def get_instance_manager(self) -> Type[BaseInstance]:
        """Returns the provider-specific class for managing Instance resources."""
        pass

    # Example for another resource type
    # @abstractmethod
    # def get_block_storage_manager(self) -> Type[BaseBlockStorage]:
    #     """Returns the provider-specific class for managing BlockStorage resources."""
    #     pass

    # --- Direct Resource Creation/Get (Alternative or Additional Approach) ---
    # Alternatively, the provider could directly handle creation/getting

    # @abstractmethod
    # async def create_instance(self, config: Dict[str, Any]) -> BaseInstance:
    #     """Creates an instance resource with the given config."""
    #     pass
    #
    # @abstractmethod
    # async def get_instance(self, resource_id: str) -> Optional[BaseInstance]:
    #     """Gets an existing instance resource by its ID."""
    #     pass

    # Add methods for other resource types (block_storage, etc.)
