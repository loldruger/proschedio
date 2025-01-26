import pytest
import logging

from vultr.apis.vfs import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_vfs_regions(api_key):
    """
    Test list_vfs_regions function.
    """
    try:
        # Test case: List all VFS regions
        result = await list_vfs_regions()
        if result.get("status") != 200:
            raise Exception(f"list_vfs_regions failed: {result}")
        logger.info("\nTest Case (list_vfs_regions - no params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_vfs_subscriptions(api_key):
    """
    Test list_vfs_subscriptions function with different parameter combinations.
    """
    try:
        # Test case 1: List all VFS subscriptions
        result = await list_vfs_subscriptions()
        if result.get("status") != 200:
            raise Exception(f"list_vfs_subscriptions (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_vfs_subscriptions - no params) - Response Data:\n%s", result)

        # Test case 2: List VFS subscriptions with per_page
        result = await list_vfs_subscriptions(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_vfs_subscriptions(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_vfs_subscriptions - per_page) - Response Data:\n%s", result)

        # Test case 3: List VFS subscriptions with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_vfs_subscriptions(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_vfs_subscriptions(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_vfs_subscriptions - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_vfs_subscription(api_key):
    """
    Test create_vfs_subscription function.
    """
    try:
        # Test case: Create a VFS subscription (replace with your desired parameters)
        storage_size = vfs.StorageSize(gb=100)
        create_data = vfs.CreateVfsData(region="ewr", label="test-vfs", storage_size=storage_size)
        result = await create_vfs_subscription(data=create_data)

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_vfs_subscription(api_key):
    """
    Test get_vfs_subscription function.
    """
    try:
        # Test case: Get VFS subscription information (replace 'your_vfs_id' with a real VFS subscription ID)
        result = await get_vfs_subscription(vfs_id="your_vfs_id")  # Replace 'your_vfs_id' with a real VFS subscription ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_vfs_subscription(api_key):
    """
    Test update_vfs_subscription function.
    """
    try:
        # Test case: Update VFS subscription information (replace 'your_vfs_id' with a real VFS subscription ID)
        storage_size = vfs.StorageSize(gb=200)
        update_data = vfs.UpdateVfsData(label="updated-vfs", storage_size=storage_size)
        result = await update_vfs_subscription(vfs_id="your_vfs_id", data=update_data)  # Replace 'your_vfs_id' with a real VFS subscription ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_vfs_subscription(api_key):
#     """
#     Test delete_vfs_subscription function.
#     """
#     try:
#         # Test case: Delete VFS subscription (replace 'your_vfs_id' with a real VFS subscription ID)
#         result = await delete_vfs_subscription(vfs_id="your_vfs_id")  # Replace 'your_vfs_id' with a real VFS subscription ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_vfs_attachments(api_key):
    """
    Test list_vfs_attachments function.
    """
    try:
        # Test case: List VFS attachments (replace 'your_vfs_id' with a real VFS subscription ID)
        result = await list_vfs_attachments(vfs_id="your_vfs_id") # Replace 'your_vfs_id' with a real VFS subscription ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_vps_to_vfs(api_key):
    """
    Test attach_vps_to_vfs function.
    """
    try:
        # Test case: Attach VPS to VFS (replace with your desired parameters)
        result = await attach_vps_to_vfs(vfs_id="your_vfs_id", vps_id="your_vps_id") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_vfs_vps_attachment(api_key):
    """
    Test get_vfs_vps_attachment function.
    """
    try:
        # Test case: Get VFS-VPS attachment details (replace with your desired parameters)
        result = await get_vfs_vps_attachment(vfs_id="your_vfs_id", vps_id="your_vps_id") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_vps_from_vfs(api_key):
    """
    Test detach_vps_from_vfs function.
    """
    try:
        # Test case: Detach VPS from VFS (replace with your desired parameters)
        result = await detach_vps_from_vfs(vfs_id="your_vfs_id", vps_id="your_vps_id") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")