import pytest
import logging

from vultr.apis.snapshots import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_snapshots(api_key):
    """
    Test list_snapshots function with different parameter combinations.
    """
    try:
        # Test case 1: List all snapshots
        result = await list_snapshots()
        if result.get("status") != 200:
            raise Exception(f"list_snapshots (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_snapshots - no params) - Response Data:\n%s", result)

        # Test case 2: List snapshots with per_page
        result = await list_snapshots(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_snapshots(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_snapshots - per_page) - Response Data:\n%s", result)

        # Test case 3: List snapshots with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_snapshots(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_snapshots(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_snapshots - cursor) - Response Data:\n%s", result)

        # Test case 4: List snapshots with description filter
        result = await list_snapshots(description="your_snapshot_description")  # Replace with your snapshot description
        if result.get("status") != 200:
            raise Exception(f"list_snapshots(description='your_snapshot_description') failed: {result}")
        logger.info("\nTest Case 4 (list_snapshots - description filter) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_snapshot(api_key):
    """
    Test create_snapshot function.
    """
    try:
        # Test case: Create a snapshot (replace with your desired parameters)
        create_data = snapshots.CreateSnapshotData(instance_id="your_instance_id").description("test-snapshot")  # Replace with your instance ID
        result = await create_snapshot(data=create_data)

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_snapshot(api_key):
    """
    Test get_snapshot function.
    """
    try:
        # Test case: Get snapshot information (replace 'your_snapshot_id' with a real snapshot ID)
        result = await get_snapshot(snapshot_id="your_snapshot_id")  # Replace 'your_snapshot_id' with a real snapshot ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_snapshot(api_key):
    """
    Test update_snapshot function.
    """
    try:
        # Test case: Update snapshot information (replace 'your_snapshot_id' with a real snapshot ID)
        result = await update_snapshot(snapshot_id="your_snapshot_id", description="updated-snapshot-description")  # Replace 'your_snapshot_id' with a real snapshot ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_snapshot(api_key):
#     """
#     Test delete_snapshot function.
#     """
#     try:
#         # Test case: Delete snapshot (replace 'your_snapshot_id' with a real snapshot ID)
#         result = await delete_snapshot(snapshot_id="your_snapshot_id")  # Replace 'your_snapshot_id' with a real snapshot ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_snapshot_from_url(api_key):
    """
    Test create_snapshot_from_url function.
    """
    try:
        # Test case: Create a snapshot from URL (replace with your desired parameters)
        create_data = snapshots.CreateSnapshotFromUrlData(url="https://example.com/image.raw").description("test-snapshot-from-url")
        result = await create_snapshot_from_url(data=create_data)

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")