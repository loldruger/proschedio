import pytest
import logging
import os
import json
import asyncio

# Import specific functions and data classes
from vultr.apis.bare_metal import (
    list_bare_metals,
    get_bare_metal, update_bare_metal,
    get_bare_metal_ipv4, get_bare_metal_ipv6,
    create_bare_metal_reverse_ipv4, create_bare_metal_reverse_ipv6,
    set_bare_metal_reverse_ipv4, delete_bare_metal_reverse_ipv6,
    start_bare_metal, reboot_bare_metal, reinstall_bare_metal, halt_bare_metal,
    get_bare_metal_bandwidth, halt_bare_metals, reboot_bare_metals, start_bare_metals,
    get_bare_metal_user_data, get_bare_metal_available_upgrades, get_bare_metal_vnc_url,
    attach_vpc_to_bare_metal, detach_vpc_from_bare_metal, list_bare_metal_vpcs,
    attach_vpc2_to_bare_metal, detach_vpc2_from_bare_metal, list_bare_metal_vpc2s
)
from vultr.structs.bare_metal import (
    UpdateBareMetalData,
    CreateBareMetalReverseIPv4Data, CreateBareMetalReverseIPv6Data
)

logger = logging.getLogger(__name__)

# Helper function to get other required IDs/IPs or skip
def get_env_var_or_skip(var_name):
    value = os.environ.get(var_name)
    if not value:
        pytest.skip(f"Skipping test: {var_name} environment variable not set.")
    return value

@pytest.mark.asyncio
async def test_list_bare_metals(vultr_client):
    """
    Tests the list_bare_metals function.
    """
    try:
        response_dict = await list_bare_metals(per_page=5, cursor=None)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_bare_metals):\n{result}")

        assert "bare_metals" in result, "Response should contain 'bare_metals' key"
        assert "meta" in result, "Response should contain 'meta' key"
        assert isinstance(result["bare_metals"], list), "'bare_metals' should be a list"
        assert isinstance(result["meta"], dict), "'meta' should be a dictionary"
        assert "total" in result["meta"]
        assert "links" in result["meta"]

        if result["bare_metals"]:
            first_bm = result["bare_metals"][0]
            assert "id" in first_bm and isinstance(first_bm["id"], str)
            assert "region" in first_bm and isinstance(first_bm["region"], str)
            assert "plan" in first_bm and isinstance(first_bm["plan"], str)
            assert "status" in first_bm and isinstance(first_bm["status"], str)
            assert "main_ip" in first_bm and isinstance(first_bm["main_ip"], str)

    except Exception as e:
        logger.error(f"Error during test_list_bare_metals: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal(vultr_client, managed_baremetal_instance):
    """
    Tests the get_bare_metal function using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal):\n{result}")

        assert "bare_metal" in result, "Response should contain 'bare_metal' key"
        bm_info = result["bare_metal"]
        assert isinstance(bm_info, dict), "'bare_metal' should be a dictionary"
        assert bm_info.get("id") == baremetal_id
        assert "region" in bm_info
        assert "plan" in bm_info
        assert "status" in bm_info
        assert "main_ip" in bm_info

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_ipv4(vultr_client, managed_baremetal_instance):
    """
    Tests the get_bare_metal_ipv4 function using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal_ipv4(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal_ipv4):\n{result}")

        assert "ipv4" in result, "Response should contain 'ipv4' key"
        assert isinstance(result["ipv4"], list), "'ipv4' should be a list"
        if result["ipv4"]:
            first_ip = result["ipv4"][0]
            assert "ip" in first_ip
            assert "netmask" in first_ip
            assert "gateway" in first_ip
            assert "type" in first_ip

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal_ipv4: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_ipv6(vultr_client, managed_baremetal_instance):
    """
    Tests the get_bare_metal_ipv6 function using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal_ipv6(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal_ipv6):\n{result}")

        assert "ipv6" in result, "Response should contain 'ipv6' key"
        assert isinstance(result["ipv6"], list), "'ipv6' should be a list"
        if result["ipv6"]:
            first_ip = result["ipv6"][0]
            assert "ip" in first_ip
            assert "network" in first_ip
            assert "network_size" in first_ip
            assert "type" in first_ip

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal_ipv6: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_bandwidth(vultr_client, managed_baremetal_instance):
    """
    Tests the get_bare_metal_bandwidth function using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal_bandwidth(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal_bandwidth):\n{result}")

        assert "bandwidth" in result, "Response should contain 'bandwidth' key"
        assert isinstance(result["bandwidth"], dict), "'bandwidth' should be a dictionary"

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal_bandwidth: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_user_data(vultr_client, managed_baremetal_instance):
    """
    Tests the get_bare_metal_user_data function using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal_user_data(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal_user_data):\n{result}")

        assert "user_data" in result, "Response should contain 'user_data' key"
        assert "data" in result["user_data"], "'user_data' should contain 'data' key"
        assert isinstance(result["user_data"]["data"], str), "'user_data.data' should be a string"

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal_user_data: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_available_upgrades(vultr_client, managed_baremetal_instance):
    """
    Tests get_bare_metal_available_upgrades using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal_available_upgrades(baremetal_id=baremetal_id, type="all")
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal_available_upgrades):\n{result}")

        assert "upgrades" in result, "Response should contain 'upgrades' key"
        assert isinstance(result["upgrades"], dict), "'upgrades' should be a dictionary"

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal_available_upgrades: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_bare_metal_vnc_url(vultr_client, managed_baremetal_instance):
    """
    Tests get_bare_metal_vnc_url using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await get_bare_metal_vnc_url(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (get_bare_metal_vnc_url):\n{result}")

        assert "vnc" in result, "Response should contain 'vnc' key"
        assert "url" in result["vnc"], "'vnc' should contain 'url' key"
        assert isinstance(result["vnc"]["url"], str), "'vnc.url' should be a string"

    except Exception as e:
        logger.error(f"Error during test_get_bare_metal_vnc_url: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_bare_metal_vpcs(vultr_client, managed_baremetal_instance):
    """
    Tests list_bare_metal_vpcs using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await list_bare_metal_vpcs(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_bare_metal_vpcs):\n{result}")

        assert "vpcs" in result, "Response should contain 'vpcs' key"
        assert isinstance(result["vpcs"], list), "'vpcs' should be a list"

    except Exception as e:
        logger.error(f"Error during test_list_bare_metal_vpcs: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_bare_metal_vpc2s(vultr_client, managed_baremetal_instance):
    """
    Tests list_bare_metal_vpc2s using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        response_dict = await list_bare_metal_vpc2s(baremetal_id=baremetal_id)
        assert response_dict.get("status") == 200, f"API returned status {response_dict.get('status')}"
        result = response_dict.get("data", {})
        logger.info(f"\nResponse Data (list_bare_metal_vpc2s):\n{result}")

        assert "vpc2s" in result, "Response should contain 'vpc2s' key"
        assert isinstance(result["vpc2s"], list), "'vpc2s' should be a list"

    except Exception as e:
        logger.error(f"Error during test_list_bare_metal_vpc2s: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_bare_metal(vultr_client, managed_baremetal_instance):
    """
    Tests update_bare_metal function using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    try:
        update_data = UpdateBareMetalData().label(f"Updated-Label-{baremetal_id[:4]}")
        response_dict = await update_bare_metal(baremetal_id=baremetal_id, data=update_data)
        assert response_dict.get("status") == 202, f"API returned status {response_dict.get('status')}"
        logger.info(f"\nUpdate Bare Metal {baremetal_id} successful.")

    except Exception as e:
        logger.error(f"Error during test_update_bare_metal: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_bare_metal_actions(vultr_client, managed_baremetal_instance):
    """
    Tests start, halt, reboot actions using the managed instance.
    """
    baremetal_id = managed_baremetal_instance
    actions_to_test = [
        (halt_bare_metal, 204),
        (start_bare_metal, 204),
        (reboot_bare_metal, 204),
    ]

    for action_func, expected_status in actions_to_test:
        try:
            logger.info(f"Testing action: {action_func.__name__} on {baremetal_id}")
            if action_func == reinstall_bare_metal:
                response_dict = await action_func(baremetal_id=baremetal_id, hostname=f"reinstall-{baremetal_id[:4]}")
            else:
                response_dict = await action_func(baremetal_id=baremetal_id)

            assert response_dict.get("status") == expected_status, \
                f"{action_func.__name__} returned status {response_dict.get('status')}, expected {expected_status}"
            logger.info(f"Action {action_func.__name__} successful.")
            await asyncio.sleep(5)

        except Exception as e:
            logger.error(f"Error during {action_func.__name__}: {e}", exc_info=True)
            pytest.fail(f"Test failed during {action_func.__name__}: {e}")

@pytest.mark.asyncio
async def test_bare_metal_reverse_dns(vultr_client, managed_baremetal_instance):
    """
    Tests reverse DNS functions using the managed instance.
    Requires VULTR_TEST_IPV4, VULTR_TEST_IPV6, VULTR_TEST_REVERSE_DOMAIN.
    """
    baremetal_id = managed_baremetal_instance
    ipv4 = get_env_var_or_skip("VULTR_TEST_IPV4")
    ipv6 = get_env_var_or_skip("VULTR_TEST_IPV6")
    reverse_domain = get_env_var_or_skip("VULTR_TEST_REVERSE_DOMAIN")

    try:
        logger.info(f"Creating reverse IPv4 for {ipv4} -> {reverse_domain}")
        create_data_v4 = CreateBareMetalReverseIPv4Data(ip=ipv4, reverse=reverse_domain)
        response_dict_create_v4 = await create_bare_metal_reverse_ipv4(baremetal_id=baremetal_id, data=create_data_v4)
        assert response_dict_create_v4.get("status") == 204, "Create reverse IPv4 failed"
        logger.info("Create reverse IPv4 successful.")
        await asyncio.sleep(2)

        logger.info(f"Setting default reverse IPv4 for {ipv4}")
        response_dict_set_default = await set_bare_metal_reverse_ipv4(baremetal_id=baremetal_id, ip=ipv4)
        assert response_dict_set_default.get("status") == 204, "Set default reverse IPv4 failed"
        logger.info("Set default reverse IPv4 successful.")
        await asyncio.sleep(2)

        logger.info(f"Creating reverse IPv6 for {ipv6} -> {reverse_domain}")
        create_data_v6 = CreateBareMetalReverseIPv6Data(ip=ipv6, reverse=reverse_domain)
        response_dict_create_v6 = await create_bare_metal_reverse_ipv6(baremetal_id=baremetal_id, data=create_data_v6)
        assert response_dict_create_v6.get("status") == 204, "Create reverse IPv6 failed"
        logger.info("Create reverse IPv6 successful.")
        await asyncio.sleep(2)

        logger.info(f"Deleting reverse IPv6 for {ipv6}")
        response_dict_delete_v6 = await delete_bare_metal_reverse_ipv6(baremetal_id=baremetal_id, ipv6=ipv6)
        assert response_dict_delete_v6.get("status") == 204, "Delete reverse IPv6 failed"
        logger.info("Delete reverse IPv6 successful.")

    except Exception as e:
        logger.error(f"Error during test_bare_metal_reverse_dns: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_bare_metal_vpc_attach_detach(vultr_client, managed_baremetal_instance):
    """
    Tests attaching and detaching VPC using the managed instance.
    Requires VULTR_TEST_VPC_ID.
    """
    baremetal_id = managed_baremetal_instance
    vpc_id = get_env_var_or_skip("VULTR_TEST_VPC_ID")

    try:
        logger.info(f"Attaching VPC {vpc_id} to Bare Metal {baremetal_id}")
        response_attach = await attach_vpc_to_bare_metal(baremetal_id=baremetal_id, vpc_id=vpc_id)
        assert response_attach.get("status") == 204, "Attach VPC failed"
        logger.info("Attach VPC successful.")
        await asyncio.sleep(5)

        logger.info(f"Detaching VPC {vpc_id} from Bare Metal {baremetal_id}")
        response_detach = await detach_vpc_from_bare_metal(baremetal_id=baremetal_id, vpc_id=vpc_id)
        assert response_detach.get("status") == 204, "Detach VPC failed"
        logger.info("Detach VPC successful.")

    except Exception as e:
        logger.error(f"Error during test_bare_metal_vpc_attach_detach: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_bare_metal_vpc2_attach_detach(vultr_client, managed_baremetal_instance):
    """
    Tests attaching and detaching VPC2 using the managed instance.
    Requires VULTR_TEST_VPC2_ID.
    """
    baremetal_id = managed_baremetal_instance
    vpc2_id = os.environ.get("VULTR_TEST_VPC2_ID")
    if not vpc2_id:
        pytest.skip("Skipping VPC2 test: VULTR_TEST_VPC2_ID not set.")

    try:
        logger.info(f"Attaching VPC2 {vpc2_id} to Bare Metal {baremetal_id}")
        response_attach = await attach_vpc2_to_bare_metal(baremetal_id=baremetal_id, vpc_id=vpc2_id, ip_address=None)
        assert response_attach.get("status") == 204, "Attach VPC2 failed"
        logger.info("Attach VPC2 successful.")
        await asyncio.sleep(5)

        logger.info(f"Detaching VPC2 {vpc2_id} from Bare Metal {baremetal_id}")
        response_detach = await detach_vpc2_from_bare_metal(baremetal_id=baremetal_id, vpc_id=vpc2_id)
        assert response_detach.get("status") == 204, "Detach VPC2 failed"
        logger.info("Detach VPC2 successful.")

    except Exception as e:
        logger.error(f"Error during test_bare_metal_vpc2_attach_detach: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.skip(reason="Skipping bulk tests by default.")
@pytest.mark.asyncio
async def test_bulk_bare_metal_actions(vultr_client):
    """
    Tests bulk actions (halt, reboot, start). Requires multiple BM IDs.
    """
    baremetal_ids_str = os.environ.get("VULTR_TEST_BAREMETAL_IDS")
    if not baremetal_ids_str:
        pytest.skip("Skipping bulk test: VULTR_TEST_BAREMETAL_IDS not set.")
    baremetal_ids = [id.strip() for id in baremetal_ids_str.split(',')]
    if len(baremetal_ids) < 2:
        pytest.skip("Skipping bulk test: Need at least 2 IDs in VULTR_TEST_BAREMETAL_IDS.")

    bulk_actions = [
        (halt_bare_metals, 204),
        (start_bare_metals, 204),
        (reboot_bare_metals, 204),
    ]

    for action_func, expected_status in bulk_actions:
        try:
            logger.info(f"Testing bulk action: {action_func.__name__} on {baremetal_ids}")
            response_dict = await action_func(baremetal_ids=baremetal_ids)
            assert response_dict.get("status") == expected_status, \
                f"Bulk {action_func.__name__} returned status {response_dict.get('status')}, expected {expected_status}"
            logger.info(f"Bulk action {action_func.__name__} successful.")
            await asyncio.sleep(10)

        except Exception as e:
            logger.error(f"Error during bulk {action_func.__name__}: {e}", exc_info=True)
            pytest.fail(f"Test failed during bulk {action_func.__name__}: {e}")