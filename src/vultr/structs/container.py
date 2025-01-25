from typing import Optional, List, Literal


class CreateContainerRegistryData:
    def __init__(self, name: str, public: bool, region: str, plan: str):
        """
        Data structure used for creating a Vultr Container Registry Subscription

        Args:
            name (str): The globally unique name to reference this registry.
            public (bool): If true, this is a publically accessible registry allowing anyone to pull from it. If false, this registry is completely private.
            region (str): The name of the region you'd like to deploy this Registry in. Can get list of regions from /registry/region/list endpoint i.e. sjc.
            plan (str): The key of the plan you'd like to select which dictates how much storage you're allocated and the monthly cost. Can get list of plans from /plan/list endpoint i.e. start_up.
        """
        self._name: str = name
        self._public: bool = public
        self._region: str = region
        self._plan: str = plan

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "name": self._name,
            "public": self._public,
            "region": self._region,
            "plan": self._plan,
        }


class UpdateContainerRegistryData:
    def __init__(self, public: Optional[bool] = None, plan: Optional[str] = None):
        """
        Data structure used for updating a Vultr Container Registry Subscription

        Args:
            public (Optional[bool]): If true, this is a publically accessible registry allowing anyone to pull from it. If false, this registry is completely private.
            plan (Optional[str]): The key of the plan you'd like to upgrade to which dictates how much storage you're allocated and the monthly cost. Can get list of plans from /plan/list endpoint i.e. business.
        """
        self._public: Optional[bool] = public
        self._plan: Optional[str] = plan
    
    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "public": self._public,
            "plan": self._plan,
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateContainerRepositoryData:
    def __init__(self, description: str):
        """
        Data structure used for updating a Vultr Container Registry Repository

        Args:
            description (str): A description of the repository.
        """
        self._description: str = description

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "description": self._description,
        }

class UpdateContainerRobotData:
    def __init__(self):
        """
        Data structure used for updating a Vultr Container Registry Robot
        """
        self._description: Optional[str] = None
        self._disable: Optional[bool] = None
        self._duration: Optional[int] = None
        self._access: Optional[List[dict]] = None

    def description(self, description: str) -> "UpdateContainerRobotData":
        """
        Set the description of the robot.

        Args:
            description (str): The description of the robot.

        Returns:
            UpdateContainerRobotData: The current object with the description set.
        """
        self._description = description
        return self

    def disable(self, disable: bool) -> "UpdateContainerRobotData":
        """
        Set whether the robot is disabled.

        Args:
            disable (bool): Whether the robot is disabled.

        Returns:
            UpdateContainerRobotData: The current object with the disable setting set.
        """
        self._disable = disable
        return self

    def duration(self, duration: int) -> "UpdateContainerRobotData":
        """
        Set the duration in seconds for which the robot credentials are valid.

        Args:
            duration (int): The duration in seconds.

        Returns:
            UpdateContainerRobotData: The current object with the duration set.
        """
        self._duration = duration
        return self

    def access(self, access: List[dict]) -> "UpdateContainerRobotData":
        """
        Set the access rules for the robot.

        Args:
            access (List[dict]): A list of access rules. Each rule should be a dictionary with "action", "resource", and "effect" keys.

        Returns:
            UpdateContainerRobotData: The current object with the access rules set.
        """
        self._access = access
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "description": self._description,
            "disable": self._disable,
            "duration": self._duration,
            "access": self._access,
        }
        return {k: v for k, v in data.items() if v is not None}