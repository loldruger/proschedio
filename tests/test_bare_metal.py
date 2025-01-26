import pytest
import logging

from vultr.apis.bare_metal import *
from vultr.structs.bare_metal import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_bare_metals(api_key):
    """
    Test list_bare_metals function with different parameter combinations.
    """
    try:
        # Test case 1: List all bare metals
        result = await list_bare_metals()
        if result.get("status") != 200:
            raise Exception(f"list_bare_metals (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_bare_metals - no params) - Response Data:\n%s", result)

        # Test case 2: List bare metals with per_page
        result = await list_bare_metals(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_bare_metals(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_bare_metals - per_page) - Response Data:\n%s", result)

        # Test case 3: List bare metals with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_bare_metals(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_bare_metals(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_bare_metals - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_bare_metal(api_key):
    """
    Test create_bare_metal function.
    """
    try:
        # Test case: Create a bare metal instance (replace with your desired parameters)
        create_data = CreateBareMetalData(region="ewr", plan="vbm-4c-32gb") \
            .label("Test Bare Metal") \
            .os_id(387)
            # .enable_ipv6(True) # You can add more parameters as needed.

        result = await create_bare_metal(data=create_data)

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal(api_key):
    """
    Test get_bare_metal function.
    """
    try:
        # Test case: Get bare metal information (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal(baremetal_id="your_bare_metal_id")  # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_bare_metal(api_key):
    """
    Test update_bare_metal function.
    """
    try:
        # Test case: Update bare metal information (replace 'your_bare_metal_id' with a real bare metal ID)
        update_data = UpdateBareMetalData() \
            .label("Updated Bare Metal Label")
            # .enable_ipv6(False) # You can add more parameters as needed.

        result = await update_bare_metal(baremetal_id="your_bare_metal_id", data=update_data) # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_bare_metal(api_key):
#     """
#     Test delete_bare_metal function.
#     """
#     try:
#         # Test case: Delete bare metal (replace 'your_bare_metal_id' with a real bare metal ID)
#         result = await delete_bare_metal(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_ipv4(api_key):
    """
    Test get_bare_metal_ipv4 function.
    """
    try:
        # Test case: Get bare metal IPv4 information (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal_ipv4(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_ipv6(api_key):
    """
    Test get_bare_metal_ipv6 function.
    """
    try:
        # Test case: Get bare metal IPv6 information (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal_ipv6(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_bare_metal_reverse_ipv4(api_key):
    """
    Test create_bare_metal_reverse_ipv4 function.
    """
    try:
        # Test case: Create bare metal reverse IPv4 entry (replace with your desired parameters)
        create_data = CreateBareMetalReverseIPv4Data(ip="your_ipv4_address", reverse="your.reverse.domain") # Replace with your desired parameters

        result = await create_bare_metal_reverse_ipv4(baremetal_id="your_bare_metal_id", data=create_data) # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_bare_metal_reverse_ipv6(api_key):
    """
    Test create_bare_metal_reverse_ipv6 function.
    """
    try:
        # Test case: Create bare metal reverse IPv6 entry (replace with your desired parameters)
        create_data = CreateBareMetalReverseIPv6Data(ip="your_full_ipv6_address", reverse="your.reverse.domain") # Replace with your desired parameters

        result = await create_bare_metal_reverse_ipv6(baremetal_id="your_bare_metal_id", data=create_data) # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_set_bare_metal_reverse_ipv4(api_key):
    """
    Test set_bare_metal_reverse_ipv4 function.
    """
    try:
        # Test case: Set bare metal reverse IPv4 (replace with your desired parameters)
        result = await set_bare_metal_reverse_ipv4(baremetal_id="your_bare_metal_id", ip="your_ipv4_address") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_bare_metal_reverse_ipv6(api_key):
    """
    Test delete_bare_metal_reverse_ipv6 function.
    
    Note: This test will fail if
        1. the reverse IPv6 entry does not exist.
        2. there is not IPv6 address attached to the bare metal instance.
        3. there does not set a reverse DNS record for the IPv6 address.
    """
    try:
        # Test case: Delete bare metal reverse IPv6 (replace with your desired parameters)
        result = await delete_bare_metal_reverse_ipv6(baremetal_id="your_bare_metal_id", ipv6="your_full_ipv6_address") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_start_bare_metal(api_key):
    """
    Test start_bare_metal function.
    """
    try:
        # Test case: Start bare metal (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await start_bare_metal(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_reboot_bare_metal(api_key):
    """
    Test reboot_bare_metal function.
    """
    try:
        # Test case: Reboot bare metal (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await reboot_bare_metal(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_reinstall_bare_metal(api_key):
    """
    Test reinstall_bare_metal function.
    """
    try:
        # Test case: Reinstall bare metal (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await reinstall_bare_metal(baremetal_id="your_bare_metal_id", hostname="new-hostname") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_halt_bare_metal(api_key):
    """
    Test halt_bare_metal function.
    """
    try:
        # Test case: Halt bare metal (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await halt_bare_metal(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_bandwidth(api_key):
    """
    Test get_bare_metal_bandwidth function.
    """
    try:
        # Test case: Get bare metal bandwidth (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal_bandwidth(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_halt_bare_metals(api_key):
    """
    Test halt_bare_metals function.
    """
    try:
        # Test case: Halt multiple bare metals (replace with your desired bare metal IDs)
        result = await halt_bare_metals(baremetal_ids=["bare_metal_id_1", "bare_metal_id_2"]) # Replace with your desired bare metal IDs

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_reboot_bare_metals(api_key):
    """
    Test reboot_bare_metals function.
    """
    try:
        # Test case: Reboot multiple bare metals (replace with your desired bare metal IDs)
        result = await reboot_bare_metals(baremetal_ids=["bare_metal_id_1", "bare_metal_id_2"]) # Replace with your desired bare metal IDs

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_start_bare_metals(api_key):
    """
    Test start_bare_metals function.
    """
    try:
        # Test case: Start multiple bare metals (replace with your desired bare metal IDs)
        result = await start_bare_metals(baremetal_ids=["bare_metal_id_1", "bare_metal_id_2"]) # Replace with your desired bare metal IDs

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_user_data(api_key):
    """
    Test get_bare_metal_user_data function.
    """
    try:
        # Test case: Get bare metal user data (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal_user_data(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_available_upgrades(api_key):
    """
    Test get_bare_metal_available_upgrades function.
    """
    try:
        # Test case: Get bare metal available upgrades (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal_available_upgrades(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_vnc_url(api_key):
    """
    Test get_bare_metal_vnc_url function.
    """
    try:
        # Test case: Get bare metal VNC URL (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await get_bare_metal_vnc_url(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_vpc_to_bare_metal(api_key):
    """
    Test attach_vpc_to_bare_metal function.
    """
    try:
        # Test case: Attach VPC to bare metal (replace with your desired parameters)
        result = await attach_vpc_to_bare_metal(baremetal_id="your_bare_metal_id", vpc_id="your_vpc_id") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_vpc_from_bare_metal(api_key):
    """
    Test detach_vpc_from_bare_metal function.
    """
    try:
        # Test case: Detach VPC from bare metal (replace with your desired parameters)
        result = await detach_vpc_from_bare_metal(baremetal_id="your_bare_metal_id", vpc_id="your_vpc_id") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_bare_metal_vpcs(api_key):
    """
    Test list_bare_metal_vpcs function.
    """
    try:
        # Test case: List bare metal VPCs (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await list_bare_metal_vpcs(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_vpc2_to_bare_metal(api_key):
    """
    Test attach_vpc2_to_bare_metal function.
    """
    try:
        # Test case: Attach VPC2 to bare metal (replace with your desired parameters)
        result = await attach_vpc2_to_bare_metal(baremetal_id="your_bare_metal_id", vpc_id="your_vpc_id", ip_address="10.1.1.4") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_vpc2_from_bare_metal(api_key):
    """
    Test detach_vpc2_from_bare_metal function.
    """
    try:
        # Test case: Detach VPC2 from bare metal (replace with your desired parameters)
        result = await detach_vpc2_from_bare_metal(baremetal_id="your_bare_metal_id", vpc_id="your_vpc_id") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_bare_metal_vpc2s(api_key):
    """
    Test list_bare_metal_vpc2s function.
    """
    try:
        # Test case: List bare metal VPC2s (replace 'your_bare_metal_id' with a real bare metal ID)
        result = await list_bare_metal_vpc2s(baremetal_id="your_bare_metal_id") # Replace 'your_bare_metal_id' with a real bare metal ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")