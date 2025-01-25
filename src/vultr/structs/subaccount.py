class CreateSubaccountData:
    def __init__(self, email: str, subaccount_name: str, subaccount_id: str):
        """
        Data structure used for creating a Vultr Subaccount.

        Args:
            email (str): Create a new sub-account with this email address.
            subaccount_name (str): Your name for this sub-account.
            subaccount_id (str): Your ID for this sub-account.
        """
        self._email: str = email
        self._subaccount_name: str = subaccount_name
        self._subaccount_id: str = subaccount_id

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "email": self._email,
            "subaccount_name": self._subaccount_name,
            "subaccount_id": self._subaccount_id,
        }