import pytest
import logging

from vultr.apis.plans import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_plans(api_key):
    """
    Test list_plans function with different parameter combinations.
    """
    try:
        # Test case 1: List all plans
        result = await list_plans()
        if result.get("status") != 200:
            raise Exception(f"list_plans (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_plans - no params) - Response Data:\n%s", result)

        # Test case 2: List plans with type filter
        result = await list_plans(type="vc2")
        if result.get("status") != 200:
            raise Exception(f"list_plans(type='vc2') failed: {result}")
        logger.info("\nTest Case 2 (list_plans - type filter) - Response Data:\n%s", result)

        # Test case 3: List plans with per_page
        result = await list_plans(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_plans(per_page=50) failed: {result}")
        logger.info("\nTest Case 3 (list_plans - per_page) - Response Data:\n%s", result)

        # Test case 4: List plans with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_plans(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_plans(cursor=...) failed: {result}")
        # logger.info("\nTest Case 4 (list_plans - cursor) - Response Data:\n%s", result)

        # Test case 5: List plans with os filter
        result = await list_plans(os="windows")
        if result.get("status") != 200:
            raise Exception(f"list_plans(os='windows') failed: {result}")
        logger.info("\nTest Case 5 (list_plans - os filter) - Response Data:\n%s", result)

        # Test case 6: List plans with multiple filters
        result = await list_plans(type="vhf", per_page=25)
        if result.get("status") != 200:
            raise Exception(f"list_plans(type='vhf', per_page=25) failed: {result}")
        logger.info("\nTest Case 6 (list_plans - multiple filters) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")