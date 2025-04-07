import os
import pytest
import asyncio
import pytest_asyncio
import logging
import colorlog

from vultr.vultr import Vultr
from vultr import set_key
# Import necessary API functions and data classes
from vultr.apis.plans_metal import list_metal_plans
from vultr.apis.operating_systems import list_os_images
from vultr.apis.bare_metal import create_bare_metal, delete_bare_metal, get_bare_metal
from vultr.structs.bare_metal import CreateBareMetalData
from vultr.apis.plans import list_plans
from vultr.apis.instances import create_instance, delete_instance, get_instance
from vultr.structs.instances import CreateInstanceData

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    }
))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@pytest.fixture(scope="session")
def api_key():
    """Fixture to get the API key from environment variable."""
    key = os.environ.get("VULTR_API_KEY")
    if not key:
        pytest.skip("VULTR_API_KEY environment variable not set")
    set_key(key)
    return key

@pytest_asyncio.fixture # Function scope (default)
async def vultr_client(api_key):
    """Fixture to provide an initialized Vultr API client for each test function."""
    client = Vultr()
    yield client
    # No cleanup needed here as Vultr class doesn't manage sessions directly

@pytest_asyncio.fixture # Function scope
async def managed_baremetal_instance(api_key):
    """
    Creates a bare metal instance using the cheapest plan and a compatible OS
    for the test function, and deletes it afterwards. Yields the instance ID.
    WARNING: This will be slow as it runs for every test function using it.
    """
    cheapest_plan_id = None
    region = None
    os_id_to_use = None
    baremetal_id = None
    min_cost = float('inf')
    compatible_os_found = False

    try:
        # 1. Find the cheapest bare metal plan and a valid region
        logger.info("Finding cheapest bare metal plan...")
        plans_response = await list_metal_plans(per_page=500, cursor=None)
        if plans_response.get("status") != 200:
            pytest.fail(f"Failed to list metal plans: {plans_response.get('data')}")
        plans = plans_response.get("data", {}).get("plans_metal", [])
        if not plans:
            pytest.skip("No bare metal plans found to create an instance.")
        for plan in plans:
            cost = plan.get("monthly_cost")
            locations = plan.get("locations")
            if cost is not None and locations and cost < min_cost:
                min_cost = cost
                cheapest_plan_id = plan.get("id")
                region = locations[0]
        if not cheapest_plan_id or not region:
             pytest.skip("Could not determine a suitable cheap bare metal plan or region.")
        logger.info(f"Selected cheapest plan: {cheapest_plan_id} in region {region} (${min_cost}/mo)")


        # 2. Find compatible OS IDs (try common server OS families)
        logger.info("Finding compatible OS ID...")
        os_response = await list_os_images(per_page=500, cursor=None)
        if os_response.get("status") != 200:
             pytest.fail(f"Failed to list operating systems: {os_response.get('data')}")

        oses = os_response.get("data", {}).get("os", [])
        # Prioritize common server OS families
        preferred_families = ["ubuntu", "centos", "debian", "rocky", "alma"]
        candidate_oses = []
        # Use generator expression style to build the list
        candidate_oses.extend(
            os_info.get("id")
            for os_info in oses
            if os_info.get("family", "").lower() in preferred_families and "x64" in os_info.get("arch", "").lower() and os_info.get("id")
        )
        # Add others as fallback
        candidate_oses.extend(
             os_info.get("id")
             for os_info in oses
             if os_info.get("family", "").lower() not in preferred_families and "x64" in os_info.get("arch", "").lower() and os_info.get("id")
        )


        if not candidate_oses:
            pytest.skip("Could not find any suitable x64 OS IDs.")

        # 3. Try creating the instance with candidate OS IDs until success
        for current_os_id in candidate_oses:
            logger.info(f"Attempting creation with OS ID: {current_os_id}...")
            create_data = CreateBareMetalData(region=region, plan=cheapest_plan_id)
            create_data.os_id = current_os_id
            create_data.label = f"pytest-managed-bm-{current_os_id}"

            create_response = await create_bare_metal(data=create_data)
            status = create_response.get("status")
            data = create_response.get("data", {})

            if status == 202: # Success (Accepted)
                baremetal_info = data.get("bare_metal", {})
                baremetal_id = baremetal_info.get("id")
                if not baremetal_id:
                     pytest.fail(f"Created bare metal instance with OS {current_os_id} but could not get ID.")
                os_id_to_use = current_os_id
                compatible_os_found = True
                logger.info(f"Successfully requested creation with OS ID: {os_id_to_use}. Instance ID: {baremetal_id}")
                break # Exit loop on successful creation request
            elif status == 400 and "This OS currently cannot be used with the selected plan" in data.get("error", ""):
                logger.warning(f"OS ID {current_os_id} is not compatible with plan {cheapest_plan_id}. Trying next OS.")
                continue # Try next OS
            else:
                # Fail for any other error
                pytest.fail(f"Failed to create bare metal instance with OS {current_os_id}. Status: {status}, Data: {data}")

        if not compatible_os_found:
            pytest.skip(f"Could not find a compatible OS for plan {cheapest_plan_id} after trying candidates.")

        logger.info(f"Waiting a bit for instance {baremetal_id} provisioning...")
        await asyncio.sleep(30)

        # 4. Yield the ID to the tests
        yield baremetal_id

    finally:
        # 5. Teardown: Delete the instance after tests run
        if baremetal_id:
            logger.info(f"Tearing down: Deleting bare metal instance {baremetal_id}...")
            try:
                # Add a loop to wait for the instance to become active before deleting,
                # as deleting a 'pending' instance might fail. Max wait 5 minutes.
                max_wait_seconds = 300
                wait_interval = 15
                elapsed_wait = 0
                instance_status = "pending"
                while instance_status != "active" and elapsed_wait < max_wait_seconds:
                    logger.info(f"Waiting for instance {baremetal_id} to become active (current: {instance_status})... ({elapsed_wait}/{max_wait_seconds}s)")
                    await asyncio.sleep(wait_interval)
                    elapsed_wait += wait_interval
                    try:
                        get_resp = await get_bare_metal(baremetal_id=baremetal_id)
                        if get_resp.get("status") == 200:
                            instance_status = get_resp.get("data", {}).get("bare_metal", {}).get("status", "unknown")
                        else:
                            logger.warning(f"Could not get instance status for {baremetal_id} during teardown wait. Status: {get_resp.get('status')}")
                            break # Exit loop if we can't get status
                    except Exception as get_e:
                        logger.error(f"Exception getting instance status for {baremetal_id} during teardown wait: {get_e}")
                        break # Exit loop on error

                if instance_status != "active":
                     logger.warning(f"Instance {baremetal_id} did not become active within {max_wait_seconds}s. Attempting deletion anyway.")

                delete_response = await delete_bare_metal(baremetal_id=baremetal_id)
                if delete_response.get("status") == 204:
                    logger.info(f"Successfully deleted bare metal instance {baremetal_id}.")
                else:
                    # Log error but don't fail the teardown if deletion fails
                    logger.error(f"Failed to delete bare metal instance {baremetal_id}. Status: {delete_response.get('status')}, Data: {delete_response.get('data')}")
            except Exception as e:
                 logger.error(f"Exception during bare metal instance deletion ({baremetal_id}): {e}", exc_info=True)
        else:
             logger.info("No bare metal instance ID to delete in teardown.")

@pytest_asyncio.fixture # Function scope (default)
async def managed_instance(api_key):
    """
    Creates a VPS instance using the cheapest non-free vc2 plan and a compatible OS
    (prioritizing os_id 2136) for the test function, and deletes it afterwards.
    Yields the instance ID.
    WARNING: This will be slow as it runs for every test function using it.
    """
    cheapest_plan_id = None
    region = None
    os_id_to_use = None
    instance_id = None
    min_cost = float('inf') # Keep track of min_cost for logging/selection
    compatible_os_found = False
    preferred_os_id = 2136 # OS ID to try first

    try:
        # 1. Find the cheapest vc2 plan (excluding free tier) and a valid region
        logger.info("Finding cheapest compatible non-free vc2 plan...")
        plans_response = await list_plans(type="vc2", per_page=500, cursor=None, os=None) # Corrected: Added os=None
        if plans_response.get("status") != 200:
            pytest.fail(f"Failed to list vc2 plans: {plans_response.get('data')}")

        plans = plans_response.get("data", {}).get("plans", [])
        if not plans:
            pytest.skip("No vc2 plans found.")

        # Filter out the free tier plan and sort by monthly cost
        non_free_plans = [
            p for p in plans
            if p.get("id") != "vc2-1c-0.5gb-free" and p.get("monthly_cost") is not None and p.get("locations")
        ]
        sorted_plans = sorted(non_free_plans, key=lambda p: p["monthly_cost"])

        if not sorted_plans:
             pytest.skip("Could not determine a suitable cheap non-free vc2 plan or region.")

        # Select the cheapest non-free plan
        cheapest_plan = sorted_plans[0]
        cheapest_plan_id = cheapest_plan.get("id")
        region = cheapest_plan.get("locations")[0]
        min_cost = cheapest_plan.get("monthly_cost") # Get the actual min cost
        logger.info(f"Selected cheapest non-free plan: {cheapest_plan_id} in region {region} (${min_cost}/mo)")

        # 2. Try creating with preferred OS ID first (using the selected non-free plan)
        logger.info(f"Attempting instance creation with preferred OS ID: {preferred_os_id}...")
        # Use method chaining for CreateInstanceData
        create_data = CreateInstanceData(region=region, plan=cheapest_plan_id)\
            .os_id(preferred_os_id)\
            .label(f"pytest-managed-vps-{preferred_os_id}")

        create_response = await create_instance(data=create_data)
        status = create_response.get("status")
        data = create_response.get("data", {})

        if status == 202: # Success
            instance_info = data.get("instance", {})
            instance_id = instance_info.get("id")
            if not instance_id:
                 pytest.fail(f"Created instance with OS {preferred_os_id} but could not get ID.")
            os_id_to_use = preferred_os_id
            compatible_os_found = True
            logger.info(f"Successfully requested creation with preferred OS ID: {os_id_to_use}. Instance ID: {instance_id}")
        elif status == 400 and ("Invalid operating system" in data.get("error", "") or "Invalid plan" in data.get("error", "") or "Invalid region" in data.get("error", "")):
            logger.warning(f"Preferred OS ID {preferred_os_id} is not compatible with plan {cheapest_plan_id}. Finding other compatible OS...")
            # Proceed to find other compatible OS if preferred one fails
        else:
            # Fail for any other unexpected error
            pytest.fail(f"Failed to create instance with preferred OS {preferred_os_id}. Status: {status}, Data: {data}")

        # 3. If preferred OS failed, find and try other compatible OS IDs
        if not compatible_os_found:
            logger.info("Finding other compatible OS IDs...")
            os_response = await list_os_images(per_page=500, cursor=None)
            if os_response.get("status") != 200:
                 pytest.fail(f"Failed to list operating systems: {os_response.get('data')}")

            oses = os_response.get("data", {}).get("os", [])
            candidate_oses = [
                os_info.get("id")
                for os_info in oses
                if "x64" in os_info.get("arch", "").lower() and os_info.get("id") and os_info.get("id") != preferred_os_id # Exclude the preferred one we already tried
            ]

            if not candidate_oses:
                pytest.skip("Could not find any suitable alternative x64 OS IDs.")

            for current_os_id in candidate_oses:
                logger.info(f"Attempting creation with alternative OS ID: {current_os_id}...")
                # Use method chaining here as well
                create_data = CreateInstanceData(region=region, plan=cheapest_plan_id)\
                    .os_id(current_os_id)\
                    .label(f"pytest-managed-vps-{current_os_id}")

                create_response = await create_instance(data=create_data)
                status = create_response.get("status")
                data = create_response.get("data", {})

                if status == 202:
                    instance_info = data.get("instance", {})
                    instance_id = instance_info.get("id")
                    if not instance_id:
                         pytest.fail(f"Created instance with OS {current_os_id} but could not get ID.")
                    os_id_to_use = current_os_id
                    compatible_os_found = True
                    logger.info(f"Successfully requested creation with alternative OS ID: {os_id_to_use}. Instance ID: {instance_id}")
                    break
                elif status == 400 and ("Invalid operating system" in data.get("error", "") or "Invalid plan" in data.get("error", "") or "Invalid region" in data.get("error", "")):
                    logger.warning(f"Alternative OS ID {current_os_id} is not compatible with plan {cheapest_plan_id}. Trying next OS.")
                    continue
                else:
                    pytest.fail(f"Failed to create instance with alternative OS {current_os_id}. Status: {status}, Data: {data}")

            if not compatible_os_found:
                pytest.skip(f"Could not find any compatible OS for plan {cheapest_plan_id} after trying candidates.")

        # 4. Wait for the instance to become active
        logger.info(f"Waiting for instance {instance_id} to become active...")
        max_wait_seconds = 600 # 10 minutes
        wait_interval = 20
        elapsed_wait = 0
        instance_status = "pending"
        while instance_status != "active" and elapsed_wait < max_wait_seconds:
             logger.info(f"Waiting for instance {instance_id} to become active (current: {instance_status})... ({elapsed_wait}/{max_wait_seconds}s)")
             await asyncio.sleep(wait_interval)
             elapsed_wait += wait_interval
             try:
                 get_resp = await get_instance(instance_id=instance_id)
                 if get_resp.get("status") == 200:
                     instance_status = get_resp.get("data", {}).get("instance", {}).get("status", "unknown")
                 else:
                     logger.warning(f"Could not get instance status for {instance_id} during setup wait. Status: {get_resp.get('status')}")
                     break
             except Exception as get_e:
                 logger.error(f"Exception getting instance status for {instance_id} during setup wait: {get_e}")
                 break

        if instance_status != "active":
             pytest.fail(f"Instance {instance_id} did not become active within {max_wait_seconds}s.")
        logger.info(f"Instance {instance_id} is active.")


        # 5. Yield the ID to the tests
        yield instance_id

    finally:
        # 6. Teardown: Delete the instance and wait for deletion
        if instance_id:
            logger.info(f"Tearing down: Deleting instance {instance_id}...")
            delete_failed = False
            try:
                # Wait loop for instance to become active before deleting
                max_wait_seconds_active = 300
                wait_interval_active = 15
                elapsed_wait_active = 0
                instance_status = "pending"
                while instance_status != "active" and elapsed_wait_active < max_wait_seconds_active:
                    logger.info(f"Waiting for instance {instance_id} to become active (current: {instance_status})... ({elapsed_wait_active}/{max_wait_seconds_active}s)")
                    await asyncio.sleep(wait_interval_active)
                    elapsed_wait_active += wait_interval_active
                    try:
                        get_resp = await get_instance(instance_id=instance_id)
                        if get_resp.get("status") == 200:
                            instance_status = get_resp.get("data", {}).get("instance", {}).get("status", "unknown")
                        else:
                            logger.warning(f"Could not get instance status for {instance_id} during teardown wait. Status: {get_resp.get('status')}")
                            break
                    except Exception as get_e:
                        logger.error(f"Exception getting instance status for {instance_id} during teardown wait: {get_e}")
                        break

                if instance_status != "active":
                    logger.warning(f"Instance {instance_id} did not become active within {max_wait_seconds_active}s. Attempting deletion anyway.")

                delete_response = await delete_instance(instance_id=instance_id)
                if delete_response.get("status") == 204:
                    logger.info(f"Instance {instance_id} deletion request successful. Waiting for confirmation...")
                else:
                    logger.error(f"Failed to initiate deletion for instance {instance_id}. Status: {delete_response.get('status')}, Data: {delete_response.get('data')}")
                    delete_failed = True

                # Wait for the instance to be actually deleted (status 404)
                max_wait_seconds_delete = 180
                wait_interval_delete = 10
                elapsed_wait_delete = 0
                instance_exists = True

                while instance_exists and elapsed_wait_delete < max_wait_seconds_delete:
                    logger.info(f"Waiting for instance {instance_id} to be deleted... ({elapsed_wait_delete}/{max_wait_seconds_delete}s)")
                    await asyncio.sleep(wait_interval_delete)
                    elapsed_wait_delete += wait_interval_delete
                    try:
                        get_resp = await get_instance(instance_id=instance_id)
                        if get_resp.get("status") == 404:
                            instance_exists = False
                            logger.info(f"Instance {instance_id} successfully deleted (confirmed by 404).")
                        elif get_resp.get("status") == 200:
                            current_status = get_resp.get("data", {}).get("instance", {}).get("status", "unknown")
                            logger.info(f"Instance {instance_id} still exists with status: {current_status}")
                        else:
                            logger.warning(f"Unexpected status {get_resp.get('status')} while checking deletion for {instance_id}.")
                    except Exception as get_e:
                        logger.error(f"Exception checking instance status during deletion wait for {instance_id}: {get_e}")
                        break

                if instance_exists:
                    logger.error(f"Instance {instance_id} was not confirmed deleted within {max_wait_seconds_delete}s.")

            except Exception as e:
                logger.error(f"Exception during instance deletion process ({instance_id}): {e}", exc_info=True)
        else:
            logger.info("No instance ID to delete in teardown.")

# No custom event_loop fixture needed