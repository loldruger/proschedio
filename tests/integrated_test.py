import asyncio
from typing import List, Optional, Dict, Any
import pytest
import logging
import time
import os

# Import the new Proschedio facade and BaseInstance
from proschedio.facade import Proschedio
from proschedio.resources.instance import BaseInstance

logger = logging.getLogger(__name__)

# Fixture to configure the provider (optional, can be done in test directly)
@pytest.fixture(scope="module", autouse=True)
def configure_proschedio_provider():
    # Ensure VULTR_API_KEY is set in the environment for this example
    vultr_api_key = os.environ.get("VULTR_API_KEY")
    if not vultr_api_key:
        pytest.skip("Skipping integration tests: VULTR_API_KEY environment variable not set.")
    
    # Configure the Vultr provider once for the module
    Proschedio.configure_provider(
        provider_name="vultr",
        config={"api_key": vultr_api_key}
    )

@pytest.mark.asyncio
async def test_create_wait_delete_instance_proschedio_facade(): # Renamed test function
    """Tests the basic flow using the new Proschedio facade API."""
    instance_object: Optional[BaseInstance] = None
    instance_id: Optional[str] = None
    instance_type = "vultr.instance"

    try:
        # 1. Create Instance using Proschedio facade with explicit parameters
        # Logging is handled within Proschedio/Provider/Resource methods
        instance_object = await Proschedio.create_instance(
            type=instance_type,
            # Pass parameters directly as keyword arguments
            region="ewr",
            plan="vc2-1c-1gb",
            os_id=2136,
            hostname="test-proschedio-facade",
            label="test-proschedio-facade",
            tags=["proschedio-facade-test"],
            backups="disabled",
            ddos_protection=False,
            wait_for_ready=True, # Control parameter
            wait_timeout=400,    # Control parameter
            wait_interval=15     # Control parameter
        )

        # 2. Assertions on the returned BaseInstance object
        assert instance_object is not None, "create_instance should return a BaseInstance object"
        assert instance_object.id is not None, "Instance object should have an ID after creation"
        instance_id = instance_object.id # Store ID for cleanup

        # Assert common properties defined in BaseInstance
        assert instance_object.status == "active", f"Instance status should be active, but was {instance_object.status}"
        assert instance_object.region == "ewr"
        assert instance_object.hostname == "test-proschedio-facade"
        assert instance_object.label == "test-proschedio-facade"
        assert instance_object.plan == "vc2-1c-1gb"
        assert "proschedio-facade-test" in (instance_object.tags or [])

        # Access provider-specific data if needed (example)
        provider_data = instance_object.provider_specific_data
        assert provider_data.get("server_status") == "ok", \
               f"Vultr server_status should be ok, but was {provider_data.get('server_status')}"

        logger.info(f"Instance {instance_id} created and verified via Proschedio facade.")

        # 3. (Optional) Do something with the instance here if needed
        await asyncio.sleep(5) # Simulate doing work

    except TimeoutError as e:
        logger.error(f"Timeout occurred: {e}")
        pytest.fail(f"Timeout occurred: {e}")
    except Exception as e:
        logger.error(f"Error during instance test flow: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")
    finally:
        # 4. Delete Instance using Proschedio facade
        if instance_id:
            try:
                logger.warning(f"Cleaning up instance {instance_id} via Proschedio facade...")
                # Use Proschedio facade to delete
                await Proschedio.delete_instance(type=instance_type, id=instance_id)
                logger.info(f"Successfully initiated deletion of instance {instance_id}.")
                
                # Optional: Verify deletion by trying to get the instance again
                await asyncio.sleep(10) # Give time for deletion to process
                deleted_instance = await Proschedio.get_instance(type=instance_type, id=instance_id)
                assert deleted_instance is None, f"Instance {instance_id} should be deleted, but get returned an object."
                logger.info(f"Verified instance {instance_id} is deleted.")

            except Exception as cleanup_e:
                # Log error but don't fail the test during cleanup
                logger.error(f"Error during instance cleanup ({instance_id}): {cleanup_e}", exc_info=True)
        elif instance_object and hasattr(instance_object, 'delete'): # Fallback if ID was not stored but object exists
             try:
                logger.warning(f"Cleaning up instance {instance_object.id} via instance object delete method...")
                # Direct deletion via object might be removed if facade is the only entry point
                await instance_object.delete()
                logger.info(f"Successfully initiated deletion of instance {instance_object.id}.")
             except Exception as cleanup_e:
                 logger.error(f"Error during instance cleanup ({instance_object.id}): {cleanup_e}", exc_info=True)