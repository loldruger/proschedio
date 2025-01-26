import pytest
import logging

from vultr.apis.operating_systems import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_os_images(api_key):
    """
    Test list_os_images function with different parameter combinations.
    """
    try:
        # Test case 1: List all OS images
        result = await list_os_images()
        if result.get("status") != 200:
            raise Exception(f"list_os_images (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_os_images - no params) - Response Data:\n%s", result)

        # Test case 2: List OS images with per_page
        result = await list_os_images(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_os_images(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_os_images - per_page) - Response Data:\n%s", result)

        # Test case 3: List OS images with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_os_images(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_os_images(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_os_images - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")