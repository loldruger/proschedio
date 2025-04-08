from typing import Dict, Any, Type
import os

from .base import BaseProvider
from ..resources.instance import BaseInstance
# Import the concrete Vultr Instance class
from vultr.structs.instances import Instance as VultrInstance
# Import the function to set the Vultr API key (or handle key directly)
from vultr import set_key as set_vultr_key

class VultrProvider(BaseProvider):
    """
    Concrete implementation of BaseProvider for the Vultr cloud provider.
    """

    def _authenticate(self) -> None:
        """Authenticates using the Vultr API key from config or environment."""
        api_key = self._config.get("api_key") or os.environ.get("VULTR_API_KEY")
        if not api_key:
            raise ValueError("Vultr API key not found in config or VULTR_API_KEY environment variable.")
        # Set the key globally for the vultr library (or store it internally)
        set_vultr_key(api_key)
        print("Vultr API key configured.") # Use logger in real implementation

    @property
    def provider_name(self) -> str:
        return "vultr"

    def get_instance_manager(self) -> Type[BaseInstance]:
        """Returns the Vultr-specific Instance class."""
        # We return the class itself, not an instance
        return VultrInstance

    # Implement methods for other resource managers (BlockStorage, etc.)
    # def get_block_storage_manager(self) -> Type[BaseBlockStorage]:
    #     return VultrBlockStorage # Assuming VultrBlockStorage exists
