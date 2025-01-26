import pytest
import logging

from vultr.apis.plans_metal import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_metal_plans(api_key):
    """
    Test list_metal_plans function with different parameter combinations.
    """
    try:
        # Test case 1: List all Bare Metal plans
        result = await list_metal_plans()
        if result.get("status") != 200:
            raise Exception(f"list_metal_plans (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_metal_plans - no params) - Response Data:\n%s", result)

        # Test case 2: List Bare Metal plans with per_page
        result = await list_metal_plans(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_metal_plans(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_metal_plans - per_page) - Response Data:\n%s", result)

        # Test case 3: List Bare Metal plans with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_metal_plans(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_metal_plans(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_metal_plans - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")