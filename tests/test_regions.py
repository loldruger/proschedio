import pytest
import logging

from vultr.apis.regions import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_regions(api_key):
    """
    Test list_regions function with different parameter combinations.
    """
    try:
        # Test case 1: List all regions
        result = await list_regions()
        if result.get("status") != 200:
            raise Exception(f"list_regions (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_regions - no params) - Response Data:\n%s", result)

        # Test case 2: List regions with per_page
        result = await list_regions(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_regions(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_regions - per_page) - Response Data:\n%s", result)

        # Test case 3: List regions with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_regions(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_regions(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_regions - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_available_plans_in_region(api_key):
    """
    Test get_available_plans_in_region function with different parameter combinations.
    """
    try:
        # Test case 1: Get available plans in a region (replace 'your_region_id' with a real region ID)
        result = await get_available_plans_in_region(region_id="your_region_id") # Replace 'your_region_id' with a real region ID
        if result.get("status") != 200:
            raise Exception(f"get_available_plans_in_region (no type) failed: {result}")
        logger.info("\nTest Case 1 (get_available_plans_in_region - no type) - Response Data:\n%s", result)

        # Test case 2: Get available plans in a region with type filter
        result = await get_available_plans_in_region(region_id="your_region_id", type="vc2") # Replace 'your_region_id' with a real region ID
        if result.get("status") != 200:
            raise Exception(f"get_available_plans_in_region(type='vc2') failed: {result}")
        logger.info("\nTest Case 2 (get_available_plans_in_region - type filter) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")