import pytest
import logging

from vultr.apis.firewall import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_firewall_groups(api_key):
    """
    Test list_firewall_groups function with different parameter combinations.
    """
    try:
        # Test case 1: List all firewall groups
        result = await list_firewall_groups()
        if result.get("status") != 200:
            raise Exception(f"list_firewall_groups (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_firewall_groups - no params) - Response Data:\n%s", result)

        # Test case 2: List firewall groups with per_page
        result = await list_firewall_groups(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_firewall_groups(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_firewall_groups - per_page) - Response Data:\n%s", result)

        # Test case 3: List firewall groups with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_firewall_groups(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_firewall_groups(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_firewall_groups - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_firewall_group(api_key):
    """
    Test create_firewall_group function.
    """
    try:
        # Test case: Create a firewall group (replace with your desired parameters)
        create_data = firewall.CreateFirewallGroupData(description="test-firewall-group")
        result = await create_firewall_group(data=create_data)

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_firewall_group(api_key):
    """
    Test get_firewall_group function.
    """
    try:
        # Test case: Get firewall group information (replace 'your_firewall_group_id' with a real firewall group ID)
        result = await get_firewall_group(firewall_group_id="your_firewall_group_id")  # Replace 'your_firewall_group_id' with a real firewall group ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_firewall_group(api_key):
    """
    Test update_firewall_group function.
    """
    try:
        # Test case: Update firewall group information (replace 'your_firewall_group_id' with a real firewall group ID)
        update_data = firewall.UpdateFirewallGroupData(description="updated-firewall-group")
        result = await update_firewall_group(firewall_group_id="your_firewall_group_id", data=update_data)  # Replace 'your_firewall_group_id' with a real firewall group ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_firewall_group(api_key):
#     """
#     Test delete_firewall_group function.
#     """
#     try:
#         # Test case: Delete firewall group (replace 'your_firewall_group_id' with a real firewall group ID)
#         result = await delete_firewall_group(firewall_group_id="your_firewall_group_id")  # Replace 'your_firewall_group_id' with a real firewall group ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_firewall_group_rules(api_key):
    """
    Test list_firewall_group_rules function with different parameter combinations.
    """
    try:
        # Test case 1: List all firewall group rules (replace 'your_firewall_group_id' with a real firewall group ID)
        result = await list_firewall_group_rules(firewall_group_id="your_firewall_group_id") # Replace 'your_firewall_group_id' with a real firewall group ID
        if result.get("status") != 200:
            raise Exception(f"list_firewall_group_rules (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_firewall_group_rules - no params) - Response Data:\n%s", result)

        # Test case 2: List firewall group rules with per_page
        result = await list_firewall_group_rules(firewall_group_id="your_firewall_group_id", per_page=50) # Replace 'your_firewall_group_id' with a real firewall group ID
        if result.get("status") != 200:
            raise Exception(f"list_firewall_group_rules(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_firewall_group_rules - per_page) - Response Data:\n%s", result)

        # Test case 3: List firewall group rules with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_firewall_group_id' and 'your_cursor_here' with real values
        # result = await list_firewall_group_rules(firewall_group_id="your_firewall_group_id", cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_firewall_group_rules(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_firewall_group_rules - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_firewall_group_rule(api_key):
    """
    Test create_firewall_group_rule function.
    """
    try:
        # Test case: Create a firewall group rule (replace with your desired parameters)
        create_data = firewall.CreateFirewallRuleData(ip_type="v4", protocol="tcp", subnet="0.0.0.0", subnet_size=0)
        result = await create_firewall_group_rule(firewall_group_id="your_firewall_group_id", data=create_data) # Replace 'your_firewall_group_id' with a real firewall group ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_firewall_group_rule(api_key):
    """
    Test get_firewall_group_rule function.
    """
    try:
        # Test case: Get firewall group rule information (replace with your desired parameters)
        result = await get_firewall_group_rule(firewall_group_id="your_firewall_group_id", firewall_rule_id="your_firewall_rule_id") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_firewall_group_rule(api_key):
#     """
#     Test delete_firewall_group_rule function.
#     """
#     try:
#         # Test case: Delete firewall group rule (replace with your desired parameters)
#         result = await delete_firewall_group_rule(firewall_group_id="your_firewall_group_id", firewall_rule_id="your_firewall_rule_id") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")