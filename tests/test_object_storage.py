import pytest
import logging

from vultr.apis.object_storage import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_object_storages(api_key):
    """
    Test list_object_storages function with different parameter combinations.
    """
    try:
        # Test case 1: List all object storages
        result = await list_object_storages()
        if result.get("status") != 200:
            raise Exception(f"list_object_storages (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_object_storages - no params) - Response Data:\n%s", result)

        # Test case 2: List object storages with per_page
        result = await list_object_storages(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_object_storages(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_object_storages - per_page) - Response Data:\n%s", result)

        # Test case 3: List object storages with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_object_storages(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_object_storages(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_object_storages - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_object_storage(api_key):
    """
    Test create_object_storage function.
    """
    try:
        # Test case: Create an object storage (replace 'your_cluster_id' with a real cluster ID)
        create_data = object_storage.CreateObjectStorageData(cluster_id=1)
        result = await create_object_storage(data=create_data)

        if result.get("status") != 202 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_object_storage(api_key):
    """
    Test get_object_storage function.
    """
    try:
        # Test case: Get object storage information (replace 'your_object_storage_id' with a real object storage ID)
        result = await get_object_storage(object_storage_id="your_object_storage_id")  # Replace 'your_object_storage_id' with a real object storage ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_object_storage(api_key):
    """
    Test update_object_storage function.
    """
    try:
        # Test case: Update object storage information (replace 'your_object_storage_id' with a real object storage ID)
        result = await update_object_storage(object_storage_id="your_object_storage_id", label="updated-object-storage")  # Replace 'your_object_storage_id' with a real object storage ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_object_storage(api_key):
#     """
#     Test delete_object_storage function.
#     """
#     try:
#         # Test case: Delete object storage (replace 'your_object_storage_id' with a real object storage ID)
#         result = await delete_object_storage(object_storage_id="your_object_storage_id")  # Replace 'your_object_storage_id' with a real object storage ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_regenerate_object_storage_keys(api_key):
    """
    Test regenerate_object_storage_keys function.
    """
    try:
        # Test case: Regenerate object storage keys (replace 'your_object_storage_id' with a real object storage ID)
        result = await regenerate_object_storage_keys(object_storage_id="your_object_storage_id")  # Replace 'your_object_storage_id' with a real object storage ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_object_storage_clusters(api_key):
    """
    Test list_object_storage_clusters function with different parameter combinations.
    """
    try:
        # Test case 1: List all object storage clusters
        result = await list_object_storage_clusters()
        if result.get("status") != 200:
            raise Exception(f"list_object_storage_clusters (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_object_storage_clusters - no params) - Response Data:\n%s", result)

        # Test case 2: List object storage clusters with per_page
        result = await list_object_storage_clusters(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_object_storage_clusters(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_object_storage_clusters - per_page) - Response Data:\n%s", result)

        # Test case 3: List object storage clusters with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_object_storage_clusters(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_object_storage_clusters(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_object_storage_clusters - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")