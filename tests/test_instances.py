import pytest
import logging

from vultr.apis.instances import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_instances(api_key):
    """
    Test list_instances function with different parameter combinations.
    """
    try:
        # Test case 1: List all instances
        result = await list_instances()
        if result.get("status") != 200:
            raise Exception(f"list_instances (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_instances - no params) - Response Data:\n%s", result)

        # Test case 2: List instances with per_page
        result = await list_instances(filters=instance.ListInstancesData().per_page(50))
        if result.get("status") != 200:
            raise Exception(f"list_instances(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_instances - per_page) - Response Data:\n%s", result)

        # Test case 3: List instances with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_instances(filters=instance.ListInstancesData().cursor("your_cursor_here"))
        # if result.get("status") != 200:
        #     raise Exception(f"list_instances(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_instances - cursor) - Response Data:\n%s", result)

        # Test case 4: List instances with region filter
        result = await list_instances(filters=instance.ListInstancesData().region("ewr"))
        if result.get("status") != 200:
            raise Exception(f"list_instances(region='ewr') failed: {result}")
        logger.info("\nTest Case 4 (list_instances - region) - Response Data:\n%s", result)

        # Test case 5: List instances with label filter
        result = await list_instances(filters=instance.ListInstancesData().label("your_instance_label")) # Replace with your label
        if result.get("status") != 200:
            raise Exception(f"list_instances(label='your_instance_label') failed: {result}")
        logger.info("\nTest Case 5 (list_instances - label) - Response Data:\n%s", result)

        # Test case 6: List instances with tag filter
        result = await list_instances(filters=instance.ListInstancesData().tag("your_instance_tag")) # Replace with your tag
        if result.get("status") != 200:
            raise Exception(f"list_instances(tag='your_instance_tag') failed: {result}")
        logger.info("\nTest Case 6 (list_instances - tag) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_instance(api_key):
    """
    Test create_instance function.
    """
    try:
        # Test case: Create an instance (replace with your desired parameters)
        create_data = instance.CreateInstanceData(region="ewr", plan="vc2-1c-1gb") \
            .label("test-instance") \
            .os_id(387) \
            .enable_ipv6(True)

        result = await create_instance(data=create_data)

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance(api_key):
    """
    Test get_instance function.
    """
    try:
        # Test case: Get instance information (replace 'your_instance_id' with a real instance ID)
        result = await get_instance(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_instance(api_key):
    """
    Test update_instance function.
    """
    try:
        # Test case: Update instance information (replace 'your_instance_id' with a real instance ID)
        update_data = instance.UpdateInstanceData().label("updated-instance-label").enable_ipv6(False)
        result = await update_instance(instance_id="your_instance_id", data=update_data)  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_instance(api_key):
#     """
#     Test delete_instance function.
#     """
#     try:
#         # Test case: Delete instance (replace 'your_instance_id' with a real instance ID)
#         result = await delete_instance(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_reinstall_instance(api_key):
    """
    Test reinstall_instance function.
    """
    try:
        # Test case: Reinstall instance (replace 'your_instance_id' with a real instance ID)
        result = await reinstall_instance(instance_id="your_instance_id", hostname="reinstalled-hostname")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_bandwidth(api_key):
    """
    Test get_instance_bandwidth function.
    """
    try:
        # Test case: Get instance bandwidth (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_bandwidth(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_neighbors(api_key):
    """
    Test get_instance_neighbors function.
    """
    try:
        # Test case: Get instance neighbors (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_neighbors(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_private_networks(api_key):
    """
    Test list_instance_private_networks function.
    """
    try:
        # Test case: List instance private networks (replace 'your_instance_id' with a real instance ID)
        result = await list_instance_private_networks(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_vpcs(api_key):
    """
    Test list_instance_vpcs function.
    """
    try:
        # Test case: List instance VPCs (replace 'your_instance_id' with a real instance ID)
        result = await list_instance_vpcs(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_vpc2s(api_key):
    """
    Test list_instance_vpc2s function.
    """
    try:
        # Test case: List instance VPC 2.0 networks (replace 'your_instance_id' with a real instance ID)
        result = await list_instance_vpc2s(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_iso_status(api_key):
    """
    Test get_instance_iso_status function.
    """
    try:
        # Test case: Get instance ISO status (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_iso_status(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_instance_iso(api_key):
    """
    Test attach_instance_iso function.
    """
    try:
        # Test case: Attach ISO to instance (replace with your desired parameters)
        result = await attach_instance_iso(instance_id="your_instance_id", iso_id="your_iso_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_instance_iso(api_key):
    """
    Test detach_instance_iso function.
    """
    try:
        # Test case: Detach ISO from instance (replace 'your_instance_id' with a real instance ID)
        result = await detach_instance_iso(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_instance_private_network(api_key):
    """
    Test attach_instance_private_network function.
    """
    try:
        # Test case: Attach private network to instance (replace with your desired parameters)
        result = await attach_instance_private_network(instance_id="your_instance_id", network_id="your_network_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_instance_private_network(api_key):
    """
    Test detach_instance_private_network function.
    """
    try:
        # Test case: Detach private network from instance (replace with your desired parameters)
        result = await detach_instance_private_network(instance_id="your_instance_id", network_id="your_network_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_instance_vpc(api_key):
    """
    Test attach_instance_vpc function.
    """
    try:
        # Test case: Attach VPC to instance (replace with your desired parameters)
        result = await attach_instance_vpc(instance_id="your_instance_id", vpc_id="your_vpc_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_instance_vpc(api_key):
    """
    Test detach_instance_vpc function.
    """
    try:
        # Test case: Detach VPC from instance (replace with your desired parameters)
        result = await detach_instance_vpc(instance_id="your_instance_id", vpc_id="your_vpc_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_attach_instance_vpc2(api_key):
    """
    Test attach_instance_vpc2 function.
    """
    try:
        # Test case: Attach VPC 2.0 to instance (replace with your desired parameters)
        result = await attach_instance_vpc2(instance_id="your_instance_id", vpc_id="your_vpc2_id", ip_address="10.1.1.4")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_detach_instance_vpc2(api_key):
    """
    Test detach_instance_vpc2 function.
    """
    try:
# Test case: Detach VPC 2.0 from instance (replace with your desired parameters)
        result = await detach_instance_vpc2(instance_id="your_instance_id", vpc_id="your_vpc2_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_backup_schedule(api_key):
    """
    Test get_instance_backup_schedule function.
    """
    try:
        # Test case: Get instance backup schedule (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_backup_schedule(instance_id="your_instance_id")  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_set_instance_backup_schedule(api_key):
    """
    Test set_instance_backup_schedule function.
    """
    try:
        # Test case: Set instance backup schedule (replace with your desired parameters)
        backup_schedule_data = instance.SetInstanceBackupScheduleData(type="daily")
        result = await set_instance_backup_schedule(instance_id="your_instance_id", data=backup_schedule_data)  # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_restore_instance(api_key):
    """
    Test restore_instance function.
    """
    try:
        # Test case: Restore instance from backup (replace with your desired parameters)
        result = await restore_instance(instance_id="your_instance_id", backup_id="your_backup_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_ipv4(api_key):
    """
    Test list_instance_ipv4 function.
    """
    try:
        # Test case: List instance IPv4 information (replace 'your_instance_id' with a real instance ID)
        result = await list_instance_ipv4(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_instance_ipv4(api_key):
    """
    Test create_instance_ipv4 function.
    """
    try:
        # Test case: Create instance IPv4 (replace 'your_instance_id' with a real instance ID)
        result = await create_instance_ipv4(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_ipv6(api_key):
    """
    Test get_instance_ipv6 function.
    """
    try:
        # Test case: Get instance IPv6 information (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_ipv6(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_instance_reverse_ipv4(api_key):
    """
    Test create_instance_reverse_ipv4 function.
    """
    try:
        # Test case: Create instance reverse IPv4 (replace with your desired parameters)
        result = await create_instance_reverse_ipv4(instance_id="your_instance_id", ip="your_ip_address", reverse="your.reverse.dns") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_reverse_ipv6(api_key):
    """
    Test list_instance_reverse_ipv6 function.
    """
    try:
        # Test case: List instance reverse IPv6 (replace 'your_instance_id' with a real instance ID)
        result = await list_instance_reverse_ipv6(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_instance_reverse_ipv6(api_key):
    """
    Test create_instance_reverse_ipv6 function.
    """
    try:
        # Test case: Create instance reverse IPv6 (replace with your desired parameters)
        result = await create_instance_reverse_ipv6(instance_id="your_instance_id", ip="your_ipv6_address", reverse="your.reverse.dns") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_set_instance_reverse_ipv4(api_key):
    """
    Test set_instance_reverse_ipv4 function.
    """
    try:
        # Test case: Set instance reverse IPv4 (replace with your desired parameters)
        result = await set_instance_reverse_ipv4(instance_id="your_instance_id", ip="your_ip_address") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_instance_reverse_ipv6(api_key):
#     """
#     Test delete_instance_reverse_ipv6 function.
#     """
#     try:
#         # Test case: Delete instance reverse IPv6 (replace with your desired parameters)
#         result = await delete_instance_reverse_ipv6(instance_id="your_instance_id", ipv6="your_ipv6_address") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_halt_instance(api_key):
    """
    Test halt_instance function.
    """
    try:
        # Test case: Halt instance (replace 'your_instance_id' with a real instance ID)
        result = await halt_instance(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_user_data(api_key):
    """
    Test get_instance_user_data function.
    """
    try:
        # Test case: Get instance user data (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_user_data(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_upgrades(api_key):
    """
    Test get_instance_upgrades function.
    """
    try:
        # Test case: Get instance upgrades (replace 'your_instance_id' with a real instance ID)
        result = await get_instance_upgrades(instance_id="your_instance_id") # Replace 'your_instance_id' with a real instance ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")