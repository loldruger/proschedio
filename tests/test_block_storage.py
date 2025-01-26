import pytest
import logging

from vultr.apis.block_storage import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_block_storage(api_key):
    """
    Test list_block_storage function with different parameter combinations.
    """
    try:
        # Test case 1: List all block storage
        result = await list_block_storage()
        if result.get("status") != 200:
            raise Exception(f"list_block_storage (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_block_storage - no params) - Response Data:\n%s", result)

        # Test case 2: List block storage with per_page
        result = await list_block_storage(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_block_storage(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_block_storage - per_page) - Response Data:\n%s", result)

        # Test case 3: List block storage with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_block_storage(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_block_storage(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_block_storage - cursor) - Response Data:\n%s", result)

        # Test case 4: List block storage with per_page and cursor
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_block_storage(per_page=25, cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_block_storage(per_page=25, cursor=...) failed: {result}")
        # logger.info("\nTest Case 4 (list_block_storage - per_page and cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_block_storage(api_key):
    """
    Test create_block_storage function.
    """
    try:
        # Test case: Create a block storage (replace with your desired parameters)
        result = await create_block_storage(region="ewr", size_gb=10, label="test-block-storage")

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_block_storage_by_id(api_key):
    """
    Test get_block_storage_by_id function.
    """
    try:
        # Test case: Get block storage information (replace 'your_block_storage_id' with a real block storage ID)
        result = await get_block_storage_by_id(block_id="your_block_storage_id") # Replace 'your_block_storage_id' with a real block storage ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_block_storage_by_id(api_key):
    """
    Test update_block_storage_by_id function.
    """
    try:
        # Test case: Update block storage information (replace 'your_block_storage_id' with a real block storage ID)
        result = await update_block_storage_by_id(block_id="your_block_storage_id", label="updated-label", size_gb=20) # Replace 'your_block_storage_id' with a real block storage ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_block_storage_by_id(api_key):
    """
    Test delete_block_storage_by_id function.
    """
    try:
        # Test case: Delete block storage (replace 'your_block_storage_id' with a real block storage ID)
        result = await delete_block_storage_by_id(block_id="your_block_storage_id") # Replace 'your_block_storage_id' with a real block storage ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_block_storage(api_key):
    """
    Test attach_block_storage function.
    """
    try:
        # Test case: Attach block storage (replace with your desired parameters)
        result = await attach_block_storage(block_id="your_block_storage_id", instance_id="your_instance_id", live=True) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_block_storage(api_key):
    """
    Test detach_block_storage function.
    """
    try:
        # Test case: Detach block storage (replace with your desired parameters)
        result = await detach_block_storage(block_id="your_block_storage_id", live=True) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")