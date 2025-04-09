import asyncio
from typing import Optional
import pytest
import logging
import os

from src.proschedio.request import Provider
from src.proschedio.resources.instance import Resource

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_instance_create_wait_delete():
    server_instance = await Resource.instance(
        provider=Provider("vultr"),
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
    ).create()

    await Resource.server_instance.delete()