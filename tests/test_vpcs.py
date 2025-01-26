import pytest
import logging

from vultr.apis.vpcs import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_vpcs(api_key):
    """
    Test list_vpcs function with different parameter combinations.
    """
    try:
        # Test case 1: List all VPCs
        result = await list_vpcs()
        if result.get("status") != 200:
            raise Exception(f"list_vpcs (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_vpcs - no params) - Response Data:\n%s", result)

        # Test case 2: List VPCs with per_page
        result = await list_vpcs(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_vpcs(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_vpcs - per_page) - Response Data:\n%s", result)

        # Test case 3: List VPCs with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_vpcs(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_vpcs(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_vpcs - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_vpc(api_key):
    """
    Test create_vpc function.
    """
    try:
        # Test case: Create a VPC (replace with your desired parameters)
        create_data = vpcs.CreateVpcData(region="ewr").description("test-vpc").v4_subnet("10.99.0.0").v4_subnet_mask(24)
        result = await create_vpc(data=create_data)

        if result.get("status") != 201 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_vpc(api_key):
    """
    Test get_vpc function.
    """
    try:
        # Test case: Get VPC information (replace 'your_vpc_id' with a real VPC ID)
        result = await get_vpc(vpc_id="your_vpc_id")  # Replace 'your_vpc_id' with a real VPC ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_vpc(api_key):
    """
    Test update_vpc function.
    """
    try:
        # Test case: Update VPC information (replace 'your_vpc_id' with a real VPC ID)
        result = await update_vpc(vpc_id="your_vpc_id", description="updated-vpc")  # Replace 'your_vpc_id' with a real VPC ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_vpc(api_key):
#     """
#     Test delete_vpc function.
#     """
#     try:
#         # Test case: Delete VPC (replace 'your_vpc_id' with a real VPC ID)
#         result = await delete_vpc(vpc_id="your_vpc_id")  # Replace 'your_vpc_id' with a real VPC ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")