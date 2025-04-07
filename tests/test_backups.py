import pytest
import logging
import os  # Import os to read environment variable
import json  # Import json

# Import specific functions
from vultr.apis.backups import list_backups, get_backup

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_backups(vultr_client):  # Use vultr_client fixture
    """
    Tests the list_backups function by calling the API
    and asserting the response structure and types based on OpenAPI spec.
    """
    try:
        # Call the function with explicit None for optional args
        response_dict = await list_backups(
            instance_id=None,
            per_page=5,  # Request a small number for testing
            cursor=None
        )
        # Check status code
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        # Access the actual data from the 'data' key
        result = response_dict.get("data", {})

        logger.info(f"\nResponse Data (list_backups):\n{result}")  # Use f-string

        # Assert top-level keys exist
        assert "backups" in result, "Response should contain 'backups' key"
        assert "meta" in result, "Response should contain 'meta' key"

        # Assert data types
        assert isinstance(result["backups"], list), "'backups' should be a list"
        assert isinstance(result["meta"], dict), "'meta' should be a dictionary"

        # Assert meta structure
        assert "total" in result["meta"], "'meta' should contain 'total' key"
        assert "links" in result["meta"], "'meta' should contain 'links' key"
        assert isinstance(result["meta"]["total"], int), "'meta.total' should be an integer"
        assert isinstance(result["meta"]["links"], dict), "'meta.links' should be a dictionary"

        # Optionally, assert backup structure if list is not empty
        if result["backups"]:
            first_backup = result["backups"][0]
            assert "id" in first_backup, "Backup object should have 'id'"
            assert isinstance(first_backup["id"], str), "'id' should be a string"
            assert "date_created" in first_backup, "Backup object should have 'date_created'"
            assert isinstance(first_backup["date_created"], str), "'date_created' should be a string"
            assert "description" in first_backup, "Backup object should have 'description'"
            assert isinstance(first_backup["description"], str), "'description' should be a string"
            assert "size" in first_backup, "Backup object should have 'size'"
            assert isinstance(first_backup["size"], int), "'size' should be an integer"
            assert "status" in first_backup, "Backup object should have 'status'"
            assert isinstance(first_backup["status"], str), "'status' should be a string"
            # Add assertions for os_id, app_id if needed

    except Exception as e:
        logger.error(f"Error during test_list_backups: {e}", exc_info=True)  # Use f-string
        pytest.fail(f"Test failed with error: {e}")  # Use f-string


@pytest.mark.asyncio
async def test_get_backup(vultr_client):  # Use vultr_client fixture
    """
    Tests the get_backup function. Requires a valid backup ID
    set in the VULTR_TEST_BACKUP_ID environment variable.
    """
    backup_id = os.environ.get("VULTR_TEST_BACKUP_ID")
    if not backup_id:
        pytest.skip("Skipping test_get_backup: VULTR_TEST_BACKUP_ID environment variable not set.")

    try:
        # Call the function with the backup_id from env var
        response_dict = await get_backup(backup_id=backup_id)

        # Check status code
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        # Access the actual data from the 'data' key
        result = response_dict.get("data", {})

        logger.info(f"\nResponse Data (get_backup):\n{result}")  # Use f-string

        # Assert top-level structure
        assert "backup" in result, "Response should contain 'backup' key"
        backup_info = result["backup"]
        assert isinstance(backup_info, dict), "'backup' should be a dictionary"

        # Assert specific fields and types within 'backup' based on OpenAPI spec
        assert "id" in backup_info and backup_info["id"] == backup_id
        assert isinstance(backup_info["id"], str)
        assert "date_created" in backup_info and isinstance(backup_info["date_created"], str)
        assert "description" in backup_info and isinstance(backup_info["description"], str)
        assert "size" in backup_info and isinstance(backup_info["size"], int)
        assert "status" in backup_info and isinstance(backup_info["status"], str)
        # Add assertions for os_id, app_id if needed

    except Exception as e:
        logger.error(f"Error during test_get_backup: {e}", exc_info=True)  # Use f-string
        pytest.fail(f"Test failed with error: {e}")  # Use f-string