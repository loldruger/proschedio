from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

from .base import BaseResource

class BaseInstance(BaseResource):
    """
    Abstract base class for compute instance resources.
    Inherits from BaseResource and adds instance-specific abstract properties.
    """

    def __init__(self, provider: Any, id: Optional[str] = None, **kwargs: Any):
        super().__init__(provider=provider, id=id, **kwargs)

    @property
    def resource_type(self) -> str:
        # Concrete implementation for instance type
        return "instance"

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

    # Add other common abstract properties as needed (os, ram, disk, etc.)

    # Optional common actions specific to instances
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
