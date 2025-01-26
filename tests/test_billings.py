import pytest
import logging

from vultr.apis.billings import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_get_billing_history(api_key):
    """
    Test get_billing_history function with different parameter combinations.
    """
    try:
        # Test case 1: Get billing history (no params)
        result = await get_billing_history()
        if result.get("status") != 200:
            raise Exception(f"get_billing_history (no params) failed: {result}")
        logger.info("\nTest Case 1 (get_billing_history - no params) - Response Data:\n%s", result)

        # Test case 2: Get billing history with per_page
        result = await get_billing_history(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"get_billing_history(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (get_billing_history - per_page) - Response Data:\n%s", result)

        # Test case 3: Get billing history with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await get_billing_history(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"get_billing_history(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (get_billing_history - cursor) - Response Data:\n%s", result)

        # Test case 4: Get billing history with per_page and cursor
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await get_billing_history(per_page=25, cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"get_billing_history(per_page=25, cursor=...) failed: {result}")
        # logger.info("\nTest Case 4 (get_billing_history - per_page and cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_billing_invoices(api_key):
    """
    Test get_billing_invoices function with different parameter combinations.
    """
    try:
        # Test case 1: Get all billing invoices
        result = await get_billing_invoices()
        if result.get("status") != 200:
            raise Exception(f"get_billing_invoices (no params) failed: {result}")
        logger.info("\nTest Case 1 (get_billing_invoices - no params) - Response Data:\n%s", result)

        # Test case 2: Get billing invoices with per_page
        result = await get_billing_invoices(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"get_billing_invoices(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (get_billing_invoices - per_page) - Response Data:\n%s", result)

        # Test case 3: Get billing invoices with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await get_billing_invoices(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"get_billing_invoices(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (get_billing_invoices - cursor) - Response Data:\n%s", result)

        # Test case 4: Get billing invoices with per_page and cursor
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await get_billing_invoices(per_page=25, cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"get_billing_invoices(per_page=25, cursor=...) failed: {result}")
        # logger.info("\nTest Case 4 (get_billing_invoices - per_page and cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_billing_invoice_by_id(api_key):
    """
    Test get_billing_invoice_by_id function.
    """
    try:
        # Test case: Get billing invoice information (replace 'your_invoice_id' with a real invoice ID)
        result = await get_billing_invoice_by_id(invoice_id="your_invoice_id") # Replace 'your_invoice_id' with a real invoice ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_billing_invoice_items(api_key):
    """
    Test get_billing_invoice_items function with different parameter combinations.
    """
    try:
        # Test case 1: Get billing invoice items (replace 'your_invoice_id' with a real invoice ID)
        result = await get_billing_invoice_items(invoice_id="your_invoice_id") # Replace 'your_invoice_id' with a real invoice ID
        if result.get("status") != 200:
            raise Exception(f"get_billing_invoice_items (no params) failed: {result}")
        logger.info("\nTest Case 1 (get_billing_invoice_items - no params) - Response Data:\n%s", result)

        # Test case 2: Get billing invoice items with per_page
        result = await get_billing_invoice_items(invoice_id="your_invoice_id", per_page=50) # Replace 'your_invoice_id' with a real invoice ID
        if result.get("status") != 200:
            raise Exception(f"get_billing_invoice_items(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (get_billing_invoice_items - per_page) - Response Data:\n%s", result)

        # Test case 3: Get billing invoice items with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_invoice_id' and 'your_cursor_here' with real values
        # result = await get_billing_invoice_items(invoice_id="your_invoice_id", cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"get_billing_invoice_items(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (get_billing_invoice_items - cursor) - Response Data:\n%s", result)

        # Test case 4: Get billing invoice items with per_page and cursor
        # Replace 'your_invoice_id' and 'your_cursor_here' with real values
        # result = await get_billing_invoice_items(invoice_id="your_invoice_id", per_page=25, cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"get_billing_invoice_items(per_page=25, cursor=...) failed: {result}")
        # logger.info("\nTest Case 4 (get_billing_invoice_items - per_page and cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_pending_charges(api_key):
    """
    Test get_pending_charges function.
    """
    try:
        # Test case: Get pending charges
        result = await get_pending_charges()

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")