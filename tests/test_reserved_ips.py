import pytest
import logging

from vultr.apis.reserved_ips import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_reserved_ips(api_key):
    """
    Test list_reserved_ips function with different parameter combinations.
    """
    try:
        # Test case 1: List all reserved IPs
        result = await list_reserved_ips()
        if result.get("status") != 200:
            raise Exception(f"list_reserved_ips (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_reserved_ips - no params) - Response Data:\n%s", result)

        # Test case 2: List reserved IPs with per_page
        result = await list_reserved_ips(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_reserved_ips(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_reserved_ips - per_page) - Response Data:\n%s", result)

        # Test case 3: List reserved IPs with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_reserved_ips(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_reserved_ips(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_reserved_ips - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_reserved_ip(api_key):
    """
    Test create_reserved_ip function.
    """
    try:
        # Test case: Create a reserved IP (replace with your desired parameters)
        create_data = reserved_ips.CreateReservedIpData(region="ewr", ip_type="v4").label("test-reserved-ip")
        result = await create_reserved_ip(data=create_data)

        if result.get("status") != 201 and result.get("status") != 409:  # 409 Conflict is acceptable if already exists
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_reserved_ip(api_key):
    """
    Test get_reserved_ip function.
    """
    try:
        # Test case: Get reserved IP information (replace 'your_reserved_ip_id' with a real reserved IP ID)
        result = await get_reserved_ip(reserved_ip="your_reserved_ip_id")  # Replace 'your_reserved_ip_id' with a real reserved IP ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_reserved_ip(api_key):
    """
    Test update_reserved_ip function.
    """
    try:
        # Test case: Update reserved IP information (replace 'your_reserved_ip_id' with a real reserved IP ID)
        result = await update_reserved_ip(reserved_ip="your_reserved_ip_id", label="updated-reserved-ip")  # Replace 'your_reserved_ip_id' with a real reserved IP ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_reserved_ip(api_key):
#     """
#     Test delete_reserved_ip function.
#     """
#     try:
#         # Test case: Delete reserved IP (replace 'your_reserved_ip_id' with a real reserved IP ID)
#         result = await delete_reserved_ip(reserved_ip="your_reserved_ip_id")  # Replace 'your_reserved_ip_id' with a real reserved IP ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_reserved_ip(api_key):
    """
    Test attach_reserved_ip function.
    """
    try:
        # Test case: Attach reserved IP (replace with your desired parameters)
        result = await attach_reserved_ip(reserved_ip="your_reserved_ip_id", instance_id="your_instance_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_reserved_ip(api_key):
    """
    Test detach_reserved_ip function.
    """
    try:
        # Test case: Detach reserved IP (replace 'your_reserved_ip_id' with a real reserved IP ID)
        result = await detach_reserved_ip(reserved_ip="your_reserved_ip_id")  # Replace 'your_reserved_ip_id' with a real reserved IP ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_convert_to_reserved_ip(api_key):
    """
    Test convert_to_reserved_ip function.
    """
    try:
        # Test case: Convert to reserved IP (replace with your desired parameters)
        convert_data = reserved_ips.ConvertIpToReservedIpData(ip_address="your_ip_address").label("test-converted-reserved-ip")
        result = await convert_to_reserved_ip(data=convert_data)
        
        if result.get("status") != 201 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")