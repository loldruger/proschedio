from typing import Optional, List, Literal

class CreateUserData:
    def __init__(self, email: str, name: str, password: str):
        """
        Data structure used for creating a Vultr User.

        Args:
            email (str): The User's email address.
            name (str): The User's name.
            password (str): The User's password.
        """
        self._email: str = email
        self._name: str = name
        self._password: str = password
        self._api_enabled: Optional[bool] = None
        self._acls: Optional[List[Literal[
            "abuse",
            "alerts",
            "billing",
            "dns",
            "firewall",
            "loadbalancer",
            "manage_users",
            "objstore",
            "provisioning",
            "subscriptions",
            "subscriptions_view",
            "support",
            "upgrade",
        ]]] = None

    def api_enabled(self, api_enabled: bool) -> "CreateUserData":
        """
        Set whether API access is permitted for this User.

        Args:
            api_enabled (bool): Whether API access is permitted.

        Returns:
            CreateUserData: The current object with the API enabled setting set.
        """
        self._api_enabled = api_enabled
        return self

    def acls(self, acls: List[Literal[
            "abuse",
            "alerts",
            "billing",
            "dns",
            "firewall",
            "loadbalancer",
            "manage_users",
            "objstore",
            "provisioning",
            "subscriptions",
            "subscriptions_view",
            "support",
            "upgrade",
        ]]) -> "CreateUserData":
        """
        Set the array of permissions granted.

        Args:
            acls (List[Literal["abuse", "alerts", "billing", "dns", "firewall", "loadbalancer", "manage_users", "objstore", "provisioning", "subscriptions", "subscriptions_view", "support", "upgrade"]]): The array of permissions.

        Returns:
            CreateUserData: The current object with the permissions set.
        """
        self._acls = acls
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "email": self._email,
            "name": self._name,
            "password": self._password,
            "api_enabled": self._api_enabled,
            "acls": self._acls,
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateUserData:
    def __init__(self):
        """
        Data structure used for updating a Vultr User.
        """
        self._email: Optional[str] = None
        self._name: Optional[str] = None
        self._password: Optional[str] = None
        self._api_enabled: Optional[bool] = None
        self._acls: Optional[List[Literal[
            "abuse",
            "alerts",
            "billing",
            "dns",
            "firewall",
            "loadbalancer",
            "manage_users",
            "objstore",
            "provisioning",
            "subscriptions",
            "subscriptions_view",
            "support",
            "upgrade",
        ]]] = None

    def email(self, email: str) -> "UpdateUserData":
        """
        Set the User's email address.

        Args:
            email (str): The User's email address.

        Returns:
            UpdateUserData: The current object with the email address set.
        """
        self._email = email
        return self

    def name(self, name: str) -> "UpdateUserData":
        """
        Set the User's name.

        Args:
            name (str): The User's name.

        Returns:
            UpdateUserData: The current object with the name set.
        """
        self._name = name
        return self

    def password(self, password: str) -> "UpdateUserData":
        """
        Set the User's password.

        Args:
            password (str): The User's password.

        Returns:
            UpdateUserData: The current object with the password set.
        """
        self._password = password
        return self
    
    def api_enabled(self, api_enabled: bool) -> "UpdateUserData":
        """
        Set whether API access is permitted for this User.

        Args:
            api_enabled (bool): Whether API access is permitted.

        Returns:
            UpdateUserData: The current object with the API enabled setting set.
        """
        self._api_enabled = api_enabled
        return self
    
    def acls(self, acls: List[Literal[
            "abuse",
            "alerts",
            "billing",
            "dns",
            "firewall",
            "loadbalancer",
            "manage_users",
            "objstore",
            "provisioning",
            "subscriptions",
            "subscriptions_view",
            "support",
            "upgrade",
        ]]) -> "UpdateUserData":
        """
        Set the array of permissions granted.

        Args:
            acls (List[Literal["abuse", "alerts", "billing", "dns", "firewall", "loadbalancer", "manage_users", "objstore", "provisioning", "subscriptions", "subscriptions_view", "support", "upgrade"]]): The array of permissions.

        Returns:
            UpdateUserData: The current object with the permissions set.
        """
        self._acls = acls
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "email": self._email,
            "name": self._name,
            "password": self._password,
            "api_enabled": self._api_enabled,
            "acls": self._acls,
        }
        return {k: v for k, v in data.items() if v is not None}