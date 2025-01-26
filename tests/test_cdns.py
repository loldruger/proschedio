import pytest
import logging

from vultr.apis.cdns import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_cdn_pull_zones(api_key):
    """
    Test list_cdn_pull_zones function.
    """
    try:
        # Test case: List all CDN pull zones
        result = await list_cdn_pull_zones()
        if result.get("status") != 200:
            raise Exception(f"list_cdn_pull_zones failed: {result}")
        logger.info("\nTest Case (list_cdn_pull_zones - no params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_cdn_pull_zone(api_key):
    """
    Test create_cdn_pull_zone function.
    """
    try:
        # Test case: Create a CDN pull zone (replace with your desired parameters)
        create_data = cdns.CreatePullZoneData(label="test-cdn-pull-zone", origin_scheme="https", origin_domain="your-origin-domain.com") # Replace with your desired parameters
        result = await create_cdn_pull_zone(data=create_data)

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_cdn_pull_zone(api_key):
    """
    Test get_cdn_pull_zone function.
    """
    try:
        # Test case: Get CDN pull zone information (replace 'your_pull_zone_id' with a real pull zone ID)
        result = await get_cdn_pull_zone(pullzone_id="your_pull_zone_id") # Replace 'your_pull_zone_id' with a real pull zone ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_cdn_pull_zone(api_key):
    """
    Test update_cdn_pull_zone function.
    """
    try:
        # Test case: Update CDN pull zone information (replace 'your_pull_zone_id' with a real pull zone ID)
        update_data = cdns.UpdatePullZoneData()
        update_data.label = "updated-cdn-pull-zone"

        result = await update_cdn_pull_zone(pullzone_id="your_pull_zone_id", data=update_data) # Replace 'your_pull_zone_id' with a real pull zone ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_cdn_pull_zone(api_key):
    """
    Test delete_cdn_pull_zone function.
    """
    try:
        # Test case: Delete CDN pull zone (replace 'your_pull_zone_id' with a real pull zone ID)
        result = await delete_cdn_pull_zone(pullzone_id="your_pull_zone_id") # Replace 'your_pull_zone_id' with a real pull zone ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_purge_cdn_pull_zone_cache(api_key):
    """
    Test purge_cdn_pull_zone_cache function.
    """
    try:
        # Test case: Purge CDN pull zone cache (replace 'your_pull_zone_id' with a real pull zone ID)
        result = await purge_cdn_pull_zone_cache(pullzone_id="your_pull_zone_id") # Replace 'your_pull_zone_id' with a real pull zone ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_cdn_push_zones(api_key):
    """
    Test list_cdn_push_zones function.
    """
    try:
        # Test case: List all CDN push zones
        result = await list_cdn_push_zones()

        if result.get("status") != 200:
            raise Exception(f"list_cdn_push_zones failed: {result}")
        logger.info("\nTest Case (list_cdn_push_zones - no params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_cdn_push_zone(api_key):
    """
    Test create_cdn_push_zone function.
    """
    try:
        # Test case: Create a CDN push zone (replace with your desired parameters)
        create_data = cdns.CreatePushZoneData(label="test-cdn-push-zone") # Replace with your desired parameters
        result = await create_cdn_push_zone(data=create_data)

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_cdn_push_zone(api_key):
    """
    Test get_cdn_push_zone function.
    """
    try:
        # Test case: Get CDN push zone information (replace 'your_push_zone_id' with a real push zone ID)
        result = await get_cdn_push_zone(pushzone_id="your_push_zone_id") # Replace 'your_push_zone_id' with a real push zone ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_cdn_push_zone(api_key):
    """
    Test update_cdn_push_zone function.
    """
    try:
        # Test case: Update CDN push zone information (replace 'your_push_zone_id' with a real push zone ID)
        update_data = cdns.UpdatePushZoneData()
        update_data.label = "updated-cdn-push-zone"
        result = await update_cdn_push_zone(pushzone_id="your_push_zone_id", data=update_data) # Replace 'your_push_zone_id' with a real push zone ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_cdn_push_zone(api_key):
    """
    Test delete_cdn_push_zone function.
    """
    try:
        # Test case: Delete CDN push zone (replace 'your_push_zone_id' with a real push zone ID)
        result = await delete_cdn_push_zone(pushzone_id="your_push_zone_id") # Replace 'your_push_zone_id' with a real push zone ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_cdn_push_zone_files(api_key):
    """
    Test list_cdn_push_zone_files function.
    """
    try:
        # Test case: List CDN push zone files (replace 'your_push_zone_id' with a real push zone ID)
        result = await list_cdn_push_zone_files(pushzone_id="your_push_zone_id") # Replace 'your_push_zone_id' with a real push zone ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_cdn_push_zone_file(api_key):
    """
    Test create_cdn_push_zone_file function.
    """
    try:
        # Test case: Create a CDN push zone file (replace with your desired parameters)
        create_data = cdns.CreatePushZoneFileData(name="test-file.txt", size=1024) # Replace with your desired parameters
        result = await create_cdn_push_zone_file(pushzone_id="your_push_zone_id", data=create_data) # Replace 'your_push_zone_id' with a real push zone ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_cdn_push_zone_file(api_key):
    """
    Test get_cdn_push_zone_file function.
    """
    try:
        # Test case: Get CDN push zone file information (replace with your desired parameters)
        result = await get_cdn_push_zone_file(pushzone_id="your_push_zone_id", file_name="your_file_name") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_cdn_push_zone_file(api_key):
    """
    Test delete_cdn_push_zone_file function.
    """
    try:
        # Test case: Delete CDN push zone file (replace with your desired parameters)
        result = await delete_cdn_push_zone_file(pushzone_id="your_push_zone_id", file_name="your_file_name") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")