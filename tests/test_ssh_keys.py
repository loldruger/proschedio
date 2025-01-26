import pytest
import logging

from vultr.apis.ssh_keys import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_ssh_keys(api_key):
    """
    Test list_ssh_keys function with different parameter combinations.
    """
    try:
        # Test case 1: List all SSH keys
        result = await list_ssh_keys()
        if result.get("status") != 200:
            raise Exception(f"list_ssh_keys (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_ssh_keys - no params) - Response Data:\n%s", result)

        # Test case 2: List SSH keys with per_page
        result = await list_ssh_keys(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_ssh_keys(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_ssh_keys - per_page) - Response Data:\n%s", result)

        # Test case 3: List SSH keys with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_ssh_keys(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_ssh_keys(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_ssh_keys - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_ssh_key(api_key):
    """
    Test create_ssh_key function.
    """
    try:
        # Test case: Create an SSH key (replace with your desired parameters)
        result = await create_ssh_key(name="test-ssh-key", ssh_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDV9K2kUQgV/...")  # Replace with your desired parameters

        if result.get("status") != 201 and result.get("status") != 400:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_ssh_key(api_key):
    """
    Test get_ssh_key function.
    """
    try:
        # Test case: Get SSH key information (replace 'your_ssh_key_id' with a real SSH key ID)
        result = await get_ssh_key(ssh_key_id="your_ssh_key_id")  # Replace 'your_ssh_key_id' with a real SSH key ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_ssh_key(api_key):
    """
    Test update_ssh_key function.
    """
    try:
        # Test case: Update SSH key information (replace 'your_ssh_key_id' with a real SSH key ID)
        result = await update_ssh_key(ssh_key_id="your_ssh_key_id", name="updated-ssh-key")  # Replace 'your_ssh_key_id' with a real SSH key ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_ssh_key(api_key):
#     """
#     Test delete_ssh_key function.
#     """
#     try:
#         # Test case: Delete SSH key (replace 'your_ssh_key_id' with a real SSH key ID)
#         result = await delete_ssh_key(ssh_key_id="your_ssh_key_id")  # Replace 'your_ssh_key_id' with a real SSH key ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")