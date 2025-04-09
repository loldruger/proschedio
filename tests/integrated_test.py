import asyncio
from typing import Optional
import pytest
import logging
import os

from src.apiV2.resources.instance import Resource

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
async def test_instance_create_wait_delete():
    server_instance = await Resource.instance(
        provider="vultr",
        plan="vc2-1c-1gb",
        region="ewr",
        hostname="test-create-and-delete",
        properties={
            "label": "test-proschedio",
            "tags": "test-proschedio",
            "backups": "disabled",
            "ddos_protection": "disabled",
            "enable_ipv6": "disabled",
        }
    )
    .create()

    await Resource.server_instance.delete()