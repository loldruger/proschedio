from typing import Dict, Any, Optional, Type
import importlib
import logging # Import logging

from .providers.base import BaseProvider
from .resources.base import BaseResource
from .resources.instance import BaseInstance
# Import other base resource types as needed

logger = logging.getLogger(__name__) # Setup logger

class ResourceManager:
    """
    Manages the creation and retrieval of cloud resources using configured providers.
    """
    def __init__(self, provider_config: Dict[str, Dict[str, Any]]):
        """
        Initializes the ResourceManager with provider configurations.

        Args:
            provider_config (Dict[str, Dict[str, Any]]): 
                A dictionary where keys are provider names (e.g., 'vultr') 
                and values are configuration dictionaries for each provider.
                Example: {'vultr': {'api_key': '...'}} 
        """
        self._providers: Dict[str, BaseProvider] = {}
        self._provider_config = provider_config
        logger.info("ResourceManager initialized.")

    def _get_provider(self, provider_name: str) -> BaseProvider:
        """Gets or initializes a provider instance."""
        if provider_name not in self._providers:
            logger.debug(f"Initializing provider: {provider_name}")
            if provider_name not in self._provider_config:
                logger.error(f"Configuration for provider '{provider_name}' not found.")
                raise ValueError(f"Configuration for provider '{provider_name}' not found.")
            
            # Construct module and class names dynamically
            provider_module_name = f"proschedio.providers.{provider_name}"
            # Simple capitalization for class name (e.g., vultr -> VultrProvider)
            provider_class_name = f"{provider_name.capitalize()}Provider"
            
            try:
                provider_module = importlib.import_module(provider_module_name)
                provider_class: Type[BaseProvider] = getattr(provider_module, provider_class_name)
                logger.debug(f"Successfully loaded provider class: {provider_class_name}")
            except (ImportError, AttributeError) as e:
                logger.error(f"Could not load provider '{provider_name}'. Ensure '{provider_module_name}.{provider_class_name}' exists: {e}", exc_info=True)
                raise ImportError(f"Could not load provider '{provider_name}'. Ensure '{provider_module_name}.{provider_class_name}' exists: {e}")

            # Instantiate the provider with its specific config
            provider_instance = provider_class(self._provider_config[provider_name])
            self._providers[provider_name] = provider_instance
            logger.info(f"Provider '{provider_name}' initialized and authenticated.")
            
        return self._providers[provider_name]

    async def create_instance(self, provider_name: str, config: Dict[str, Any]) -> BaseInstance:
        """
        Creates a compute instance using the specified provider and configuration.

        Args:
            provider_name (str): The name of the provider (e.g., 'vultr').
            config (Dict[str, Any]): Configuration for the instance resource.

        Returns:
            BaseInstance: The created instance object.
        """
        logger.info(f"Request to create instance with provider '{provider_name}' and config: {config}")
        provider = self._get_provider(provider_name)
        # Get the specific resource class (e.g., VultrInstance) from the provider
        InstanceManagerClass: Type[BaseInstance] = provider.get_instance_manager()
        
        # Instantiate the specific resource manager (e.g., VultrInstance)
        instance_resource = InstanceManagerClass(provider=provider, config=config)
        
        # Call the create method on the resource object
        logger.debug(f"Calling create() on {InstanceManagerClass.__name__}...")
        created_instance = await instance_resource.create()
        logger.info(f"Successfully created instance: ID={created_instance.id}")
        return created_instance

    # Add methods for other resource types (create_block_storage, etc.)
    # async def create_block_storage(...)

    async def get_instance(self, provider_name: str, resource_id: str) -> Optional[BaseInstance]:
        """
        Gets an existing compute instance by its ID.

        Args:
            provider_name (str): The name of the provider.
            resource_id (str): The unique ID of the instance resource.

        Returns:
            Optional[BaseInstance]: The instance object if found, otherwise None.
        """
        logger.info(f"Request to get instance '{resource_id}' from provider '{provider_name}'.")
        provider = self._get_provider(provider_name)
        InstanceManagerClass: Type[BaseInstance] = provider.get_instance_manager()
        
        # Instantiate a temporary resource object to call get
        # Note: Passing an empty config might be problematic if __init__ needs it.
        # Consider a classmethod get(provider, id) on BaseResource/BaseInstance for a cleaner approach.
        temp_instance_resource = InstanceManagerClass(provider=provider, config={}) 
        temp_instance_resource._id = resource_id # Manually set ID for get() to work
        
        logger.debug(f"Calling get() on {InstanceManagerClass.__name__} for ID: {resource_id}...")
        fetched_instance = await temp_instance_resource.get()
        if fetched_instance:
            logger.info(f"Successfully fetched instance: ID={fetched_instance.id}")
        else:
            logger.info(f"Instance with ID '{resource_id}' not found on provider '{provider_name}'.")
        return fetched_instance

    async def delete_instance(self, provider_name: str, resource_id: str) -> None:
        """
        Deletes an existing compute instance by its ID.

        Args:
            provider_name (str): The name of the provider.
            resource_id (str): The unique ID of the instance resource.
        """
        logger.info(f"Request to delete instance '{resource_id}' from provider '{provider_name}'.")
        provider = self._get_provider(provider_name)
        InstanceManagerClass: Type[BaseInstance] = provider.get_instance_manager()
        
        # Instantiate a temporary resource object to call delete
        temp_instance_resource = InstanceManagerClass(provider=provider, config={})
        temp_instance_resource._id = resource_id # Manually set ID for delete() to work

        logger.debug(f"Calling delete() on {InstanceManagerClass.__name__} for ID: {resource_id}...")
        await temp_instance_resource.delete()
        logger.info(f"Successfully initiated deletion for instance: ID={resource_id}")

    # Add get/delete methods for other resource types
