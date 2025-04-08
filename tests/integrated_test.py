import asyncio
from typing import List, Optional
import pytest
import logging
import time

from vultr.apis import *
from vultr.apis.container_registry import list_regions
# Import only necessary functions
from vultr.apis.instances import delete_instance
# Import the Instance struct
from vultr.structs.instances import CreateInstanceData, Instance
from vultr.vultr import Vultr

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_create_wait_delete_instance(api_key):
    """Tests the basic flow: create instance, wait until ready, then delete."""
    instance_id: Optional[str] = None
    
    try:
        # 1. Create Instance using the builder and wait
        # Logging is now handled within Vultr/InstanceBuilder methods
        instance_object: Instance = await Vultr()\
            .new_instance(
                CreateInstanceData(
                    region="ewr",
                    plan="vc2-1c-1gb"
                )\
                .os_id(2136)
                .hostname("test-create-wait-del")\
                .label("test-create-wait-del")\
                .ddos_protection(False)\
                .backups("disabled")
            )\
            .apply(wait=True, timeout=400, interval=5)

        # 2. Assertions on the returned Instance object
        assert instance_object is not None, "apply(wait=True) should return an Instance object"
        assert instance_object.id is not None, "Instance object should have an ID"
        instance_id = instance_object.id # Store ID for cleanup

        assert instance_object.status == "active", f"Instance status should be active, but was {instance_object.status}"
        assert instance_object.server_status == "ok", f"Instance server_status should be ok, but was {instance_object.server_status}"
        assert instance_object.hostname == "test-create-wait-del"
        assert instance_object.label == "test-create-wait-del"

        # 3. (Optional) Do something with the instance here if needed
        await asyncio.sleep(5) # Simulate doing work

    except TimeoutError as e:
        # Keep logging for errors
        logger.error(f"Timeout waiting for instance {instance_id}: {e}")
        pytest.fail(f"Timeout waiting for instance {instance_id}")
    except Exception as e:
        # Keep logging for errors
        logger.error(f"Error during instance test flow: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")
    finally:
        # Keep logging for cleanup
        if instance_id:
            try:
                logger.warning(f"Cleaning up instance {instance_id}...")
                delete_resp = await delete_instance(instance_id=instance_id)
                if delete_resp.get("status") == 204:
                    logger.info(f"Successfully initiated deletion of instance {instance_id}.")
                else:
                    logger.error(f"Failed to delete instance {instance_id}. Status: {delete_resp.get('status')}, Response: {delete_resp.get('data')}")
            except Exception as cleanup_e:
                logger.error(f"Error during instance cleanup ({instance_id}): {cleanup_e}", exc_info=True)

# Remove or adapt previous test cases like test_construct_instance_and_wait
# and test_create_instance_and_wait_manual as they are now covered by
# test_create_wait_delete_instance