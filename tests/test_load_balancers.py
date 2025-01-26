import pytest
import logging

from vultr.apis.load_balancers import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_load_balancers(api_key):
    """
    Test list_load_balancers function with different parameter combinations.
    """
    try:
        # Test case 1: List all load balancers
        result = await list_load_balancers()
        if result.get("status") != 200:
            raise Exception(f"list_load_balancers (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_load_balancers - no params) - Response Data:\n%s", result)

        # Test case 2: List load balancers with per_page
        result = await list_load_balancers(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_load_balancers(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_load_balancers - per_page) - Response Data:\n%s", result)

        # Test case 3: List load balancers with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_load_balancers(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_load_balancers(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_load_balancers - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_load_balancer(api_key):
    """
    Test create_load_balancer function.
    """
    try:
        # Test case: Create a load balancer (replace with your desired parameters)
        health_check = load_balancer.HealthCheck(protocol="http", port=80, path="/health", check_interval=5, response_timeout=2, unhealthy_threshold=5, healthy_threshold=5)
        forwarding_rule = load_balancer.ForwardingRule(frontend_protocol="http", frontend_port=80, backend_protocol="http", backend_port=8080)
        create_data = load_balancer.CreateLoadBalancerData(region="ewr").balancing_algorithm("roundrobin").health_check(health_check).forwarding_rules([forwarding_rule]).label("test-lb")
        result = await create_load_balancer(data=create_data)

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_load_balancer(api_key):
    """
    Test get_load_balancer function.
    """
    try:
        # Test case: Get load balancer information (replace 'your_load_balancer_id' with a real load balancer ID)
        result = await get_load_balancer(load_balancer_id="your_load_balancer_id")  # Replace 'your_load_balancer_id' with a real load balancer ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_load_balancer(api_key):
    """
    Test update_load_balancer function.
    """
    try:
        # Test case: Update load balancer information (replace 'your_load_balancer_id' with a real load balancer ID)
        health_check = load_balancer.HealthCheck(protocol="http", port=80, path="/health_updated", check_interval=5, response_timeout=2, unhealthy_threshold=5, healthy_threshold=5)
        forwarding_rule = load_balancer.ForwardingRule(frontend_protocol="http", frontend_port=8080, backend_protocol="http", backend_port=8081)
        update_data = load_balancer.UpdateLoadBalancerData().label("updated-lb").health_check(health_check).forwarding_rules([forwarding_rule])

        result = await update_load_balancer(load_balancer_id="your_load_balancer_id", data=update_data)  # Replace 'your_load_balancer_id' with a real load balancer ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_load_balancer(api_key):
#     """
#     Test delete_load_balancer function.
#     """
#     try:
#         # Test case: Delete load balancer (replace 'your_load_balancer_id' with a real load balancer ID)
#         result = await delete_load_balancer(load_balancer_id="your_load_balancer_id")  # Replace 'your_load_balancer_id' with a real load balancer ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_load_balancer_ssl(api_key):
#     """
#     Test delete_load_balancer_ssl function.
#     """
#     try:
#         # Test case: Delete load balancer SSL (replace 'your_load_balancer_id' with a real load balancer ID)
#         result = await delete_load_balancer_ssl(load_balancer_id="your_load_balancer_id")  # Replace 'your_load_balancer_id' with a real load balancer ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_load_balancer_auto_ssl(api_key):
#     """
#     Test delete_load_balancer_auto_ssl function.
#     """
#     try:
#         # Test case: Delete load balancer auto SSL (replace 'your_load_balancer_id' with a real load balancer ID)
#         result = await delete_load_balancer_auto_ssl(load_balancer_id="your_load_balancer_id")  # Replace 'your_load_balancer_id' with a real load balancer ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_load_balancer_forwarding_rules(api_key):
    """
    Test list_load_balancer_forwarding_rules function with different parameter combinations.
    """
    try:
        # Test case 1: List all load balancer forwarding rules (replace 'your_load_balancer_id' with a real load balancer ID)
        result = await list_load_balancer_forwarding_rules(load_balancer_id="your_load_balancer_id") # Replace 'your_load_balancer_id' with a real load balancer ID
        if result.get("status") != 200:
            raise Exception(f"list_load_balancer_forwarding_rules (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_load_balancer_forwarding_rules - no params) - Response Data:\n%s", result)

        # Test case 2: List load balancer forwarding rules with per_page
        result = await list_load_balancer_forwarding_rules(load_balancer_id="your_load_balancer_id", per_page=50) # Replace 'your_load_balancer_id' with a real load balancer ID
        if result.get("status") != 200:
            raise Exception(f"list_load_balancer_forwarding_rules(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_load_balancer_forwarding_rules - per_page) - Response Data:\n%s", result)

        # Test case 3: List load balancer forwarding rules with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_load_balancer_id' and 'your_cursor_here' with real values
        # result = await list_load_balancer_forwarding_rules(load_balancer_id="your_load_balancer_id", cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_load_balancer_forwarding_rules(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_load_balancer_forwarding_rules - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_load_balancer_forwarding_rule(api_key):
    """
    Test create_load_balancer_forwarding_rule function.
    """
    try:
        # Test case: Create a load balancer forwarding rule (replace with your desired parameters)
        forwarding_rule_data = load_balancer.ForwardingRule(frontend_protocol="http", frontend_port=80, backend_protocol="http", backend_port=8080)
        result = await create_load_balancer_forwarding_rule(load_balancer_id="your_load_balancer_id", data=forwarding_rule_data) # Replace 'your_load_balancer_id' with a real load balancer ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_load_balancer_forwarding_rule(api_key):
    """
    Test get_load_balancer_forwarding_rule function.
    """
    try:
        # Test case: Get load balancer forwarding rule information (replace with your desired parameters)
        result = await get_load_balancer_forwarding_rule(load_balancer_id="your_load_balancer_id", forwarding_rule_id="your_forwarding_rule_id") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_load_balancer_forwarding_rule(api_key):
#     """
#     Test delete_load_balancer_forwarding_rule function.
#     """
#     try:
#         # Test case: Delete load balancer forwarding rule (replace with your desired parameters)
#         result = await delete_load_balancer_forwarding_rule(load_balancer_id="your_load_balancer_id", forwarding_rule_id="your_forwarding_rule_id") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_load_balancer_firewall_rules(api_key):
    """
    Test list_load_balancer_firewall_rules function with different parameter combinations.
    """
    try:
        # Test case 1: List all load balancer firewall rules (replace 'your_load_balancer_id' with a real load balancer ID)
        result = await list_load_balancer_firewall_rules(load_balancer_id="your_load_balancer_id") # Replace 'your_load_balancer_id' with a real load balancer ID
        if result.get("status") != 200:
            raise Exception(f"list_load_balancer_firewall_rules (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_load_balancer_firewall_rules - no params) - Response Data:\n%s", result)

        # Test case 2: List load balancer firewall rules with per_page
        result = await list_load_balancer_firewall_rules(load_balancer_id="your_load_balancer_id", per_page=50) # Replace 'your_load_balancer_id' with a real load balancer ID
        if result.get("status") != 200:
            raise Exception(f"list_load_balancer_firewall_rules(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_load_balancer_firewall_rules - per_page) - Response Data:\n%s", result)

        # Test case 3: List load balancer firewall rules with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_load_balancer_id' and 'your_cursor_here' with real values
        # result = await list_load_balancer_firewall_rules(load_balancer_id="your_load_balancer_id", cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_load_balancer_firewall_rules(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_load_balancer_firewall_rules - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_load_balancer_firewall_rule(api_key):
    """
    Test get_load_balancer_firewall_rule function.
    """
    try:
        # Test case: Get load balancer firewall rule information (replace with your desired parameters)
        result = await get_load_balancer_firewall_rule(load_balancer_id="your_load_balancer_id", firewall_rule_id="your_firewall_rule_id") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")