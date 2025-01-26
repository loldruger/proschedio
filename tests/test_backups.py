import pytest
import logging

from vultr.apis.backups import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_backups(api_key):
    """
    Test list_backups function with different parameter combinations.
    """
    try:
        # Test case 1: List all backups
        result = await list_backups()
        if result.get("status") != 200:
            raise Exception(f"list_backups (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_backups - no params) - Response Data:\n%s", result)

        # Test case 2: List backups with per_page
        result = await list_backups(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_backups(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_backups - per_page) - Response Data:\n%s", result)

        # Test case 3: List backups with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_backups(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_backups(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_backups - cursor) - Response Data:\n%s", result)

        # Test case 4: List backups with instance_id filter
        result = await list_backups(instance_id="your_instance_id") # Replace your_instance_id with a real instance ID
        if result.get("status") != 200:
            raise Exception(f"list_backups(instance_id=...) failed: {result}")
        logger.info("\nTest Case 4 (list_backups - instance_id) - Response Data:\n%s", result)

        # Test case 5: List backups with all parameters
        # Replace 'your_cursor_here' and 'your_instance_id' with real values
        # result = await list_backups(per_page=25, cursor="your_cursor_here", instance_id="your_instance_id")
        # if result.get("status") != 200:
        #     raise Exception(f"list_backups(per_page=25, cursor=..., instance_id=...) failed: {result}")
        # logger.info("\nTest Case 5 (list_backups - all params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")


@pytest.mark.asyncio
async def test_get_backup(api_key):
    """
    Test get_backup function.
    """
    try:
        # Test case: Get backup information (replace 'your_backup_id' with a real backup ID)
        result = await get_backup(backup_id="your_backup_id")  # Replace 'your_backup_id' with a real backup ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")