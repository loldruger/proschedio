import pytest
import logging

from vultr.apis.account import get_account_info, get_account_bandwidth

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_get_account_info(vultr_client):
    """
    Tests the get_account_info function by calling the API directly
    and asserting the response structure and types based on OpenAPI spec.
    """
    try:
        # Call the function directly - it returns a dict { "status": ..., "data": ... }
        response_dict = await get_account_info()
        # Check status code (optional but recommended)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        # Access the actual data from the 'data' key
        result = response_dict.get("data", {})

        logger.info(f"\nResponse Data:\n{result}")

        assert isinstance(result, dict), "Response data should be a dictionary"
        assert "account" in result, "Response data should contain 'account' key"

        account_info = result["account"]
        assert isinstance(account_info, dict), "'account' should be a dictionary"

        assert "name" in account_info and isinstance(account_info["name"], str)
        assert "email" in account_info and isinstance(account_info["email"], str)
        assert "acls" in account_info and isinstance(account_info["acls"], list)
        assert "balance" in account_info and isinstance(account_info["balance"], (int, float))
        assert "pending_charges" in account_info and isinstance(account_info["pending_charges"], (int, float))
        assert "last_payment_date" in account_info
        assert "last_payment_amount" in account_info and isinstance(account_info["last_payment_amount"], (int, float))

        if account_info["acls"]:
            assert all(isinstance(acl, str) for acl in account_info["acls"])

    except Exception as e:
        logger.error(f"Error during test_get_account_info: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_account_bandwidth(vultr_client):
    """
    Tests the get_account_bandwidth function by calling the API directly
    and asserting the response structure and types based on OpenAPI spec.
    """
    try:
        # Call the function directly - it returns a dict { "status": ..., "data": ... }
        response_dict = await get_account_bandwidth()
        # Check status code (optional but recommended)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        # Access the actual data from the 'data' key
        result = response_dict.get("data", {})

        logger.info(f"\nResponse Data:\n{result}")

        bandwidth_key = "bandwidth"
        assert isinstance(result, dict), "Response data should be a dictionary"
        assert bandwidth_key in result, f"Response data should contain '{bandwidth_key}' key"

        bandwidth_data = result[bandwidth_key]
        assert isinstance(bandwidth_data, dict), f"'{bandwidth_key}' should be a dictionary"

        assert "previous_month" in bandwidth_data
        assert "current_month_to_date" in bandwidth_data
        assert "current_month_projected" in bandwidth_data

        current_month = bandwidth_data["current_month_to_date"]
        assert isinstance(current_month, dict)
        assert "timestamp_start" in current_month and isinstance(current_month["timestamp_start"], str)
        assert "timestamp_end" in current_month and isinstance(current_month["timestamp_end"], str)
        assert "gb_in" in current_month and isinstance(current_month["gb_in"], (int, float))
        assert "gb_out" in current_month and isinstance(current_month["gb_out"], (int, float))
        assert "total_instance_hours" in current_month and isinstance(current_month["total_instance_hours"], (int, float))
        assert "total_instance_count" in current_month and isinstance(current_month["total_instance_count"], int)
        assert "instance_bandwidth_credits" in current_month and isinstance(current_month["instance_bandwidth_credits"], (int, float))
        assert "free_bandwidth_credits" in current_month and isinstance(current_month["free_bandwidth_credits"], (int, float))
        assert "purchased_bandwidth_credits" in current_month and isinstance(current_month["purchased_bandwidth_credits"], (int, float))
        assert "overage" in current_month and isinstance(current_month["overage"], (int, float))
        assert "overage_unit_cost" in current_month and isinstance(current_month["overage_unit_cost"], (int, float))
        assert "overage_cost" in current_month and isinstance(current_month["overage_cost"], (int, float))

    except Exception as e:
        logger.error(f"Error during test_get_account_bandwidth: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")