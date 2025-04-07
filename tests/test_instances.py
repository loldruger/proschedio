import pytest
import logging
import os
import json
import asyncio

# Import specific functions and data classes
from vultr.apis.instances import (
    list_instances, get_instance, update_instance,
    reinstall_instance, get_instance_bandwidth, get_instance_neighbors,
    list_instance_private_networks, list_instance_vpcs, list_instance_vpc2s,
    get_instance_iso_status, attach_instance_iso, detach_instance_iso,
    attach_instance_private_network, detach_instance_private_network,
    attach_instance_vpc, detach_instance_vpc,
    attach_instance_vpc2, detach_instance_vpc2,
    get_instance_backup_schedule, set_instance_backup_schedule,
    restore_instance, list_instance_ipv4, create_instance_ipv4,
    get_instance_ipv6, create_instance_reverse_ipv4, list_instance_reverse_ipv6,
    create_instance_reverse_ipv6, set_instance_reverse_ipv4,
    delete_instance_reverse_ipv6, halt_instance, get_instance_user_data,
    get_instance_upgrades
)
# Import data classes if needed for specific tests (e.g., update, backup schedule)
from vultr.structs import instances as instance_structs

logger = logging.getLogger(__name__)

# Helper function to get other required IDs/IPs or skip
def get_env_var_or_skip(var_name):
    value = os.environ.get(var_name)
    if not value:
        pytest.skip(f"Skipping test: {var_name} is not set.")
    return value

@pytest.mark.asyncio
async def test_list_instances(vultr_client): # Use vultr_client fixture
    """
    Tests list_instances function.
    """
    try:
        # Call list_instances with filters=None
        response_dict = await list_instances(filters=None)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_instances):\n{result}")

        assert "instances" in result, "Response should contain 'instances' key"
        assert isinstance(result["instances"], list), "'instances' should be a list"
        assert "meta" in result, "Response should contain 'meta' key"

    except Exception as e:
        logger.error(f"Error during test_list_instances: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

# --- Tests requiring an Instance ID ---
# Use the managed_instance fixture

@pytest.mark.asyncio
async def test_get_instance(vultr_client, managed_instance): # Add fixture
    """
    Tests the get_instance function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance):\n{result}")

        assert "instance" in result, "Response should contain 'instance' key"
        inst_info = result["instance"]
        assert isinstance(inst_info, dict), "'instance' should be a dictionary"
        assert inst_info.get("id") == instance_id
        assert "region" in inst_info
        assert "plan" in inst_info
        assert "status" in inst_info
        assert "main_ip" in inst_info
        # Add more detailed assertions based on the instance schema

    except Exception as e:
        logger.error(f"Error during test_get_instance: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_instance(vultr_client, managed_instance): # Add fixture
    """
    Tests update_instance function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        new_label = f"Updated-Label-{instance_id[:4]}"
        update_data = instance_structs.UpdateInstanceData().label(new_label)
        response_dict = await update_instance(instance_id=instance_id, data=update_data)
        # Expect 202 Accepted for update
        assert response_dict.get("status") == 202, f"API returned status {response_dict.get('status')}"
        logger.info(f"\nUpdate Instance {instance_id} successful.")

        # Optionally, verify the update
        await asyncio.sleep(5) # Give some time for update to potentially reflect
        get_response = await get_instance(instance_id=instance_id)
        updated_label = get_response.get("data", {}).get("instance", {}).get("label")
        assert updated_label == new_label, f"Label was not updated. Expected {new_label}, got {updated_label}"

    except Exception as e:
        logger.error(f"Error during test_update_instance: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_reinstall_instance(vultr_client, managed_instance): # Add fixture
    """
    Tests reinstall_instance function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        new_hostname = f"reinstall-{instance_id[:4]}"
        response_dict = await reinstall_instance(instance_id=instance_id, hostname=new_hostname)
        # Expect 202 Accepted for reinstall
        assert response_dict.get("status") == 202, f"API returned status {response_dict.get('status')}"
        logger.info(f"\nReinstall Instance {instance_id} successful.")
        # Note: Reinstall takes time, verifying hostname change immediately might fail.

    except Exception as e:
        logger.error(f"Error during test_reinstall_instance: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_bandwidth(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_bandwidth function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_bandwidth(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_bandwidth):\n{result}")

        assert "bandwidth" in result, "Response should contain 'bandwidth' key"
        assert isinstance(result["bandwidth"], dict), "'bandwidth' should be a dictionary"
        # Check for date keys within bandwidth
        assert any(key.startswith('20') for key in result["bandwidth"]), "Bandwidth data should contain date keys"

    except Exception as e:
        logger.error(f"Error during test_get_instance_bandwidth: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_neighbors(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_neighbors function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_neighbors(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_neighbors):\n{result}")

        assert "neighbors" in result, "Response should contain 'neighbors' key"
        assert isinstance(result["neighbors"], list), "'neighbors' should be a list"
        # Structure of neighbors list items can be asserted if needed

    except Exception as e:
        logger.error(f"Error during test_get_instance_neighbors: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_vpcs(vultr_client, managed_instance): # Add fixture
    """
    Tests list_instance_vpcs function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await list_instance_vpcs(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_instance_vpcs):\n{result}")

        assert "vpcs" in result, "Response should contain 'vpcs' key"
        assert isinstance(result["vpcs"], list), "'vpcs' should be a list"
        assert "meta" in result # Check for meta object

    except Exception as e:
        logger.error(f"Error during test_list_instance_vpcs: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_iso_status(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_iso_status function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_iso_status(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_iso_status):\n{result}")

        assert "iso_status" in result, "Response should contain 'iso_status' key"
        assert "state" in result["iso_status"], "'iso_status' should contain 'state' key"
        # ISO is likely not attached, so state should be 'ready' or similar
        assert result["iso_status"]["state"] == "ready"

    except Exception as e:
        logger.error(f"Error during test_get_instance_iso_status: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_backup_schedule(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_backup_schedule function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_backup_schedule(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_backup_schedule):\n{result}")

        assert "backup_schedule" in result, "Response should contain 'backup_schedule' key"
        schedule = result["backup_schedule"]
        assert "enabled" in schedule # Check for key fields
        assert "type" in schedule
        assert "next_scheduled_time_utc" in schedule
        assert "hour" in schedule
        assert "dow" in schedule
        assert "dom" in schedule

    except Exception as e:
        logger.error(f"Error during test_get_instance_backup_schedule: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_set_instance_backup_schedule(vultr_client, managed_instance): # Add fixture
    """
    Tests set_instance_backup_schedule function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        # Test setting a daily schedule
        backup_schedule_data = instance_structs.SetInstanceBackupScheduleData(type="daily", hour=3)
        response_dict = await set_instance_backup_schedule(instance_id=instance_id, data=backup_schedule_data)
        assert response_dict.get("status") == 204, f"Set daily schedule failed: {response_dict.get('data')}"
        logger.info(f"\nSet daily backup schedule for {instance_id} successful.")

        # Verify the schedule was set (optional but good)
        await asyncio.sleep(2)
        get_response = await get_instance_backup_schedule(instance_id=instance_id)
        schedule = get_response.get("data", {}).get("backup_schedule", {})
        assert schedule.get("type") == "daily"
        assert schedule.get("hour") == 3

        # Test disabling backups (set type to empty or specific disable value if API supports it)
        disable_schedule_data = instance_structs.SetInstanceBackupScheduleData(type="")
        response_dict_disable = await set_instance_backup_schedule(instance_id=instance_id, data=disable_schedule_data)
        assert response_dict_disable.get("status") == 204, f"Disable schedule failed: {response_dict_disable.get('data')}"
        logger.info(f"\nDisable backup schedule for {instance_id} successful.")

        # Verify disabled (optional)
        await asyncio.sleep(2)
        get_response_disabled = await get_instance_backup_schedule(instance_id=instance_id)
        schedule_disabled = get_response_disabled.get("data", {}).get("backup_schedule", {})
        assert not schedule_disabled.get("enabled") # Check if enabled is false

    except Exception as e:
        logger.error(f"Error during test_set_instance_backup_schedule: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_ipv4(vultr_client, managed_instance): # Add fixture
    """
    Tests list_instance_ipv4 function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await list_instance_ipv4(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_instance_ipv4):\n{result}")

        assert "ipv4s" in result, "Response should contain 'ipv4s' key"
        assert isinstance(result["ipv4s"], list), "'ipv4s' should be a list"
        assert "meta" in result # Check for meta object
        if result["ipv4s"]:
            first_ip = result["ipv4s"][0]
            assert "ip" in first_ip
            assert "netmask" in first_ip
            assert "gateway" in first_ip
            assert "type" in first_ip

    except Exception as e:
        logger.error(f"Error during test_list_instance_ipv4: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_ipv6(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_ipv6 function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_ipv6(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_ipv6):\n{result}")

        assert "ipv6s" in result, "Response should contain 'ipv6s' key"
        assert isinstance(result["ipv6s"], list), "'ipv6s' should be a list"
        assert "meta" in result # Check for meta object
        if result["ipv6s"]:
            first_ip = result["ipv6s"][0]
            assert "ip" in first_ip
            assert "network" in first_ip
            assert "network_size" in first_ip
            assert "type" in first_ip

    except Exception as e:
        logger.error(f"Error during test_get_instance_ipv6: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_instance_reverse_ipv6(vultr_client, managed_instance): # Add fixture
    """
    Tests list_instance_reverse_ipv6 function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await list_instance_reverse_ipv6(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_instance_reverse_ipv6):\n{result}")

        assert "reverse_ipv6s" in result, "Response should contain 'reverse_ipv6s' key"
        assert isinstance(result["reverse_ipv6s"], list), "'reverse_ipv6s' should be a list"
        assert "meta" in result # Check for meta object
        # Structure of reverse_ipv6s items can be asserted if needed

    except Exception as e:
        logger.error(f"Error during test_list_instance_reverse_ipv6: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_user_data(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_user_data function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_user_data(instance_id=instance_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_user_data):\n{result}")

        assert "user_data" in result, "Response should contain 'user_data' key"
        assert "data" in result["user_data"], "'user_data' should contain 'data' key"
        assert isinstance(result["user_data"]["data"], str), "'user_data.data' should be a string"
        # User data might be empty if not provided during creation

    except Exception as e:
        logger.error(f"Error during test_get_instance_user_data: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_instance_upgrades(vultr_client, managed_instance): # Add fixture
    """
    Tests get_instance_upgrades function using the managed instance.
    """
    instance_id = managed_instance # Use ID from fixture
    try:
        response_dict = await get_instance_upgrades(instance_id=instance_id, type="all") # Explicit type
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_instance_upgrades):\n{result}")

        assert "upgrades" in result, "Response should contain 'upgrades' key"
        assert isinstance(result["upgrades"], dict), "'upgrades' should be a dictionary"
        # Check for expected upgrade types if needed (e.g., 'os', 'applications', 'plans')

    except Exception as e:
        logger.error(f"Error during test_get_instance_upgrades: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

# --- Tests requiring specific external resources (Skip by default) ---

@pytest.mark.skip(reason="Requires specific ISO ID (VULTR_TEST_ISO_ID).")
@pytest.mark.asyncio
async def test_attach_detach_instance_iso(vultr_client, managed_instance):
    """
    Tests attaching and detaching ISO. Requires VULTR_TEST_ISO_ID.
    """
    instance_id = managed_instance
    iso_id = get_env_var_or_skip("VULTR_TEST_ISO_ID")
    try:
        # Attach
        logger.info(f"Attaching ISO {iso_id} to instance {instance_id}")
        attach_resp = await attach_instance_iso(instance_id=instance_id, iso_id=iso_id)
        assert attach_resp.get("status") == 202, f"Attach ISO failed: {attach_resp.get('data')}"
        await asyncio.sleep(5) # Wait for attach

        # Verify status
        status_resp = await get_instance_iso_status(instance_id=instance_id)
        assert status_resp.get("data", {}).get("iso_status", {}).get("state") == "iso_attached"

        # Detach
        logger.info(f"Detaching ISO from instance {instance_id}")
        detach_resp = await detach_instance_iso(instance_id=instance_id)
        assert detach_resp.get("status") == 202, f"Detach ISO failed: {detach_resp.get('data')}"
        await asyncio.sleep(5) # Wait for detach

        # Verify status again
        status_resp_after = await get_instance_iso_status(instance_id=instance_id)
        assert status_resp_after.get("data", {}).get("iso_status", {}).get("state") == "ready"

    except Exception as e:
        logger.error(f"Error during test_attach_detach_instance_iso: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.skip(reason="Requires specific VPC ID (VULTR_TEST_VPC_ID).")
@pytest.mark.asyncio
async def test_attach_detach_instance_vpc(vultr_client, managed_instance):
    """
    Tests attaching and detaching VPC. Requires VULTR_TEST_VPC_ID.
    """
    instance_id = managed_instance
    vpc_id = get_env_var_or_skip("VULTR_TEST_VPC_ID")
    try:
        # Attach
        logger.info(f"Attaching VPC {vpc_id} to instance {instance_id}")
        attach_resp = await attach_instance_vpc(instance_id=instance_id, vpc_id=vpc_id)
        assert attach_resp.get("status") == 204, f"Attach VPC failed: {attach_resp.get('data')}"
        await asyncio.sleep(5)

        # Verify list contains the VPC
        list_resp = await list_instance_vpcs(instance_id=instance_id)
        attached_vpcs = [vpc.get("id") for vpc in list_resp.get("data", {}).get("vpcs", [])]
        assert vpc_id in attached_vpcs

        # Detach
        logger.info(f"Detaching VPC {vpc_id} from instance {instance_id}")
        detach_resp = await detach_instance_vpc(instance_id=instance_id, vpc_id=vpc_id)
        assert detach_resp.get("status") == 204, f"Detach VPC failed: {detach_resp.get('data')}"
        await asyncio.sleep(5)

        # Verify list no longer contains the VPC
        list_resp_after = await list_instance_vpcs(instance_id=instance_id)
        attached_vpcs_after = [vpc.get("id") for vpc in list_resp_after.get("data", {}).get("vpcs", [])]
        assert vpc_id not in attached_vpcs_after

    except Exception as e:
        logger.error(f"Error during test_attach_detach_instance_vpc: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

# Add similar skipped tests for VPC2, Private Network, Reverse DNS, Restore if needed,
# ensuring they use the managed_instance fixture and appropriate env vars for other IDs.

# Removed test_create_instance and test_delete_instance

# Deprecated tests (can be removed or kept skipped)
@pytest.mark.skip(reason="Private Networks are deprecated.")
@pytest.mark.asyncio
async def test_list_instance_private_networks(vultr_client, managed_instance):
    pass

@pytest.mark.skip(reason="Private Networks are deprecated.")
@pytest.mark.asyncio
async def test_attach_instance_private_network(vultr_client, managed_instance):
    pass

@pytest.mark.skip(reason="Private Networks are deprecated.")
@pytest.mark.asyncio
async def test_detach_instance_private_network(vultr_client, managed_instance):
    pass

@pytest.mark.skip(reason="VPC2 is deprecated.")
@pytest.mark.asyncio
async def test_list_instance_vpc2s(vultr_client, managed_instance):
    pass

@pytest.mark.skip(reason="VPC2 is deprecated.")
@pytest.mark.asyncio
async def test_attach_instance_vpc2(vultr_client, managed_instance):
    pass

@pytest.mark.skip(reason="VPC2 is deprecated.")
@pytest.mark.asyncio
async def test_detach_instance_vpc2(vultr_client, managed_instance):
    pass

# Action tests using managed instance
@pytest.mark.asyncio
async def test_halt_instance(vultr_client, managed_instance):
    """
    Tests halt_instance function using the managed instance.
    """
    instance_id = managed_instance
    try:
        logger.info(f"Halting instance {instance_id}")
        response_dict = await halt_instance(instance_id=instance_id)
        assert response_dict.get("status") == 204, f"Halt instance failed: {response_dict.get('data')}"
        logger.info(f"Instance {instance_id} halt successful.")
        # Add verification if needed (e.g., check power_status after delay)
    except Exception as e:
        logger.error(f"Error during test_halt_instance: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

# Reverse DNS tests (require specific IPs and domain)
@pytest.mark.skip(reason="Requires VULTR_TEST_IPV4, VULTR_TEST_IPV6, VULTR_TEST_REVERSE_DOMAIN")
@pytest.mark.asyncio
async def test_instance_reverse_dns(vultr_client, managed_instance):
    instance_id = managed_instance
    ipv4 = get_env_var_or_skip("VULTR_TEST_IPV4")
    ipv6 = get_env_var_or_skip("VULTR_TEST_IPV6")
    reverse_domain = get_env_var_or_skip("VULTR_TEST_REVERSE_DOMAIN")
    pass

# Restore test (requires specific backup/snapshot ID)
@pytest.mark.skip(reason="Requires VULTR_TEST_BACKUP_ID or VULTR_TEST_SNAPSHOT_ID")
@pytest.mark.asyncio
async def test_restore_instance(vultr_client, managed_instance):
    instance_id = managed_instance
    backup_id = os.environ.get("VULTR_TEST_BACKUP_ID")
    snapshot_id = os.environ.get("VULTR_TEST_SNAPSHOT_ID")
    if not backup_id and not snapshot_id:
        pytest.skip("Skipping restore test: Neither VULTR_TEST_BACKUP_ID nor VULTR_TEST_SNAPSHOT_ID is set.")

    restore_from = {"backup_id": backup_id} if backup_id else {"snapshot_id": snapshot_id}
    try:
        logger.info(f"Restoring instance {instance_id} from {restore_from}")
        response_dict = await restore_instance(instance_id=instance_id, **restore_from)
        assert response_dict.get("status") == 202, f"Restore instance failed: {response_dict.get('data')}"
        logger.info(f"Instance {instance_id} restore initiated.")
    except Exception as e:
        logger.error(f"Error during test_restore_instance: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

# Create IPv4 test (might fail if limit reached)
@pytest.mark.skip(reason="May fail if IPv4 limit is reached.")
@pytest.mark.asyncio
async def test_create_instance_ipv4(vultr_client, managed_instance):
    instance_id = managed_instance
    try:
        logger.info(f"Creating IPv4 for instance {instance_id}")
        response_dict = await create_instance_ipv4(instance_id=instance_id)
        assert response_dict.get("status") == 202, f"Create IPv4 failed: {response_dict.get('data')}"
        logger.info(f"IPv4 creation initiated for {instance_id}.")
        # Add verification if needed (check list_instance_ipv4 after delay)
    except Exception as e:
        logger.error(f"Error during test_create_instance_ipv4: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")