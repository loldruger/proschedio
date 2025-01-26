import pytest
import logging

from vultr.apis.subaccounts import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_subaccounts(api_key):
    """
    Test list_subaccounts function with different parameter combinations.
    """
    try:
        # Test case 1: List all subaccounts
        result = await list_subaccounts()
        if result.get("status") != 200:
            raise Exception(f"list_subaccounts (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_subaccounts - no params) - Response Data:\n%s", result)

        # Test case 2: List subaccounts with per_page
        result = await list_subaccounts(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_subaccounts(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_subaccounts - per_page) - Response Data:\n%s", result)

        # Test case 3: List subaccounts with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_subaccounts(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_subaccounts(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_subaccounts - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_subaccount(api_key):
    """
    Test create_subaccount function.
    """
    try:
        # Test case: Create a subaccount (replace with your desired parameters)
        create_data = subaccount.CreateSubaccountData(email="testuser@example.com", subaccount_name="Test Subaccount", subaccount_id="test-subaccount")
        result = await create_subaccount(data=create_data)

        if result.get("status") != 201 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")