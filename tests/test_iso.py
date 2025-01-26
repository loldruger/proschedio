import pytest
import logging

from vultr.apis.iso import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_isos(api_key):
    """
    Test list_isos function with different parameter combinations.
    """
    try:
        # Test case 1: List all ISOs
        result = await list_isos()
        if result.get("status") != 200:
            raise Exception(f"list_isos (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_isos - no params) - Response Data:\n%s", result)

        # Test case 2: List ISOs with per_page
        result = await list_isos(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_isos(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_isos - per_page) - Response Data:\n%s", result)

        # Test case 3: List ISOs with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_isos(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_isos(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_isos - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_iso(api_key):
    """
    Test create_iso function.
    """
    try:
        # Test case: Create an ISO (replace with your desired URL)
        result = await create_iso(url="https://example.com/my-iso.iso")  # Replace with your desired URL

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_iso(api_key):
    """
    Test get_iso function.
    """
    try:
        # Test case: Get ISO information (replace 'your_iso_id' with a real ISO ID)
        result = await get_iso(iso_id="your_iso_id")  # Replace 'your_iso_id' with a real ISO ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_iso(api_key):
#     """
#     Test delete_iso function.
#     """
#     try:
#         # Test case: Delete ISO (replace 'your_iso_id' with a real ISO ID)
#         result = await delete_iso(iso_id="your_iso_id")  # Replace 'your_iso_id' with a real ISO ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_public_isos(api_key):
    """
    Test list_public_isos function.
    """
    try:
        # Test case: List all public ISOs
        result = await list_public_isos()
        if result.get("status") != 200:
            raise Exception(f"list_public_isos failed: {result}")
        logger.info("\nTest Case (list_public_isos - no params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")