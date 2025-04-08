from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List

class BaseInstance(ABC):
    """
    Abstract base class representing a generic cloud instance resource.
    All provider-specific instance classes should inherit from this.
    """

    @property
    @abstractmethod
    def id(self) -> Optional[str]:
        """Unique identifier for the instance."""
        pass

    @property
    @abstractmethod
    def status(self) -> Optional[str]:
        """Current status of the instance (e.g., running, stopped, pending)."""
        pass

    @property
    @abstractmethod
    def region(self) -> Optional[str]:
        """Region where the instance is located."""
        pass

    @property
    @abstractmethod
    def main_ip(self) -> Optional[str]:
        """Main public IP address."""
        pass

    @property
    @abstractmethod
    def hostname(self) -> Optional[str]:
        """Hostname of the instance."""
        pass

    @property
    @abstractmethod
    def label(self) -> Optional[str]:
        """User-defined label for the instance."""
        pass

    @property
    @abstractmethod
    def plan(self) -> Optional[str]:
        """Identifier for the instance plan/size/type."""
        pass

    @property
    @abstractmethod
    def date_created(self) -> Optional[str]:
        """Timestamp when the instance was created."""
        pass

    @property
    @abstractmethod
    def tags(self) -> Optional[List[str]]:
        """List of tags associated with the instance."""
        pass

    # Add other common properties as needed, e.g., os, ram, disk, vcpu_count

    @property
    @abstractmethod
    def provider_specific_data(self) -> Dict[str, Any]:
        """Access the raw data returned by the provider's API."""
        pass

    # Optional: Define common actions as abstract methods
    # @abstractmethod
    # async def delete(self) -> None:
    #     pass
    #
    # @abstractmethod
    # async def stop(self) -> None:
    #     pass
    #
    # @abstractmethod
    # async def start(self) -> None:
    #     pass
    #
    # @abstractmethod
    # async def reboot(self) -> None:
    #     pass
