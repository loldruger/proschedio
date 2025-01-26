import pytest
import logging

from vultr.apis.vpc2 import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_vpc2s(api_key):
    """
    Test list_vpc2s function with different parameter combinations.
    """
    try:
        # Test case 1: List all VPC 2.0 networks
        result = await list_vpc2s()
        if result.get("status") != 200:
            raise Exception(f"list_vpc2s (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_vpc2s - no params) - Response Data:\n%s", result)

        # Test case 2: List VPC 2.0 networks with per_page
        result = await list_vpc2s(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_vpc2s(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_vpc2s - per_page) - Response Data:\n%s", result)

        # Test case 3: List VPC 2.0 networks with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_vpc2s(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_vpc2s(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_vpc2s - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_vpc2(api_key):
    """
    Test create_vpc2 function.
    """
    try:
        # Test case: Create a VPC 2.0 network (replace with your desired parameters)
        create_data = vpc2.CreateVpc2Data(region="ewr").description("test-vpc2").ip_block("10.0.0.0").prefix_length(24)
        result = await create_vpc2(data=create_data)

        if result.get("status") != 201 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_vpc2(api_key):
    """
    Test get_vpc2 function.
    """
    try:
        # Test case: Get VPC 2.0 network information (replace 'your_vpc_id' with a real VPC 2.0 ID)
        result = await get_vpc2(vpc_id="your_vpc_id")  # Replace 'your_vpc_id' with a real VPC 2.0 ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_vpc2(api_key):
    """
    Test update_vpc2 function.
    """
    try:
        # Test case: Update VPC 2.0 network information (replace 'your_vpc_id' with a real VPC 2.0 ID)
        result = await update_vpc2(vpc_id="your_vpc_id", description="updated-vpc2")  # Replace 'your_vpc_id' with a real VPC 2.0 ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_vpc2(api_key):
#     """
#     Test delete_vpc2 function.
#     """
#     try:
#         # Test case: Delete VPC 2.0 network (replace 'your_vpc_id' with a real VPC 2.0 ID)
#         result = await delete_vpc2(vpc_id="your_vpc_id")  # Replace 'your_vpc_id' with a real VPC 2.0 ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_vpc2_nodes(api_key):
    """
    Test list_vpc2_nodes function with different parameter combinations.
    """
    try:
        # Test case 1: List all nodes attached to a VPC 2.0 network (replace 'your_vpc_id' with a real VPC 2.0 ID)
        result = await list_vpc2_nodes(vpc_id="your_vpc_id") # Replace 'your_vpc_id' with a real VPC 2.0 ID
        if result.get("status") != 200:
            raise Exception(f"list_vpc2_nodes (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_vpc2_nodes - no params) - Response Data:\n%s", result)

        # Test case 2: List nodes with per_page
        result = await list_vpc2_nodes(vpc_id="your_vpc_id", per_page=50) # Replace 'your_vpc_id' with a real VPC 2.0 ID
        if result.get("status") != 200:
            raise Exception(f"list_vpc2_nodes(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_vpc2_nodes - per_page) - Response Data:\n%s", result)

        # Test case 3: List nodes with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_vpc_id' and 'your_cursor_here' with real values
        # result = await list_vpc2_nodes(vpc_id="your_vpc_id", cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_vpc2_nodes(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_vpc2_nodes - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_vpc2_nodes(api_key):
    """
    Test attach_vpc2_nodes function.
    """
    try:
        # Test case: Attach nodes to a VPC 2.0 network (replace with your desired parameters)
        attach_data = vpc2.AttachDetachVpc2NodesData(nodes=[["instance_id_1"], ["baremetal_id_1"]]) # Replace with your desired parameters
        result = await attach_vpc2_nodes(vpc_id="your_vpc_id", data=attach_data) # Replace 'your_vpc_id' with a real VPC 2.0 ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_vpc2_nodes(api_key):
    """
    Test detach_vpc2_nodes function.
    """
    try:
        # Test case: Detach nodes from a VPC 2.0 network (replace with your desired parameters)
        detach_data = vpc2.AttachDetachVpc2NodesData(nodes=[["instance_id_1"], ["baremetal_id_1"]]) # Replace with your desired parameters
        result = await detach_vpc2_nodes(vpc_id="your_vpc_id", data=detach_data) # Replace 'your_vpc_id' with a real VPC 2.0 ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")