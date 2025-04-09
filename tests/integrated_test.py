import asyncio
from typing import Optional
import pytest
import logging
import os

from src.apiV2.request import Provider
from src.apiV2.resources.instance import Resource
from proschedio.facade import Proschedio
from proschedio.resources.base import BaseResource

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_create_wait_delete_instance_proschedio_facade():
    """Tests the basic flow using the new Proschedio.Resource API."""
    resource_object: Optional[BaseResource] = None
    resource_id: Optional[str] = None
    resource_type = "vultr.instance"

    try:
        # 1. Create Instance using Proschedio.Resource.create
        resource_object = await Proschedio.Resource.create(
            type=resource_type,
            region="ewr",
            plan="vc2-1c-1gb",
            os_id=2136,
            hostname="test-proschedio-res-facade",
            label="test-proschedio-res-facade",
            tags=["proschedio-resource-test"],
            backups="disabled",
            ddos_protection=False,
            wait_for_ready=True,
            wait_timeout=400,
            wait_interval=15
        )

        # 2. Assertions on the returned BaseResource object
        assert resource_object is not None, "Resource.create should return a BaseResource object"
        assert resource_object.id is not None, "Resource object should have an ID after creation"
        resource_id = resource_object.id

        if isinstance(resource_object, BaseInstance):
            assert resource_object.status == "active", f"Instance status should be active, but was {resource_object.status}"
            assert resource_object.region == "ewr"
            assert resource_object.hostname == "test-proschedio-res-facade"
            assert resource_object.label == "test-proschedio-res-facade"
            assert resource_object.plan == "vc2-1c-1gb"
            assert "proschedio-resource-test" in (resource_object.tags or [])

            provider_data = resource_object.provider_specific_data
            assert provider_data.get("server_status") == "ok", \
                   f"Vultr server_status should be ok, but was {provider_data.get('server_status')}"
        else:
            pytest.fail("Created resource is not an instance of BaseInstance")

        logger.info(f"Resource {resource_id} ({resource_type}) created and verified via Proschedio.Resource.")

        await asyncio.sleep(5)

    except TimeoutError as e:
        logger.error(f"Timeout occurred: {e}")
        pytest.fail(f"Timeout occurred: {e}")
    except Exception as e:
        logger.error(f"Error during resource test flow: {e}", exc_info=True)
        pytest.fail(f"Test failed with error: {e}")
    finally:
        if resource_id:
            try:
                logger.warning(f"Cleaning up resource {resource_id} ({resource_type}) via Proschedio.Resource...")
                await Proschedio.Resource.delete(type=resource_type, id=resource_id)
                logger.info(f"Successfully initiated deletion of resource {resource_id}.")
                
                await asyncio.sleep(10)
                deleted_resource = await Proschedio.Resource.get(type=resource_type, id=resource_id)
                assert deleted_resource is None, f"Resource {resource_id} should be deleted, but get returned an object."
                logger.info(f"Verified resource {resource_id} is deleted.")

            except Exception as cleanup_e:
                logger.error(f"Error during resource cleanup ({resource_id}): {cleanup_e}", exc_info=True)