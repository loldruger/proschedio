import asyncio
from typing import Optional
import pytest
import logging

from src.proschedio.resources.instance import Resource

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_instance_create_wait_delete():
    server_instance = await Resource.instance(
        provider="vultr",
        region = "ewr",
        plan = "vc2-1c-1gb",
        config={
            "os_id": 270,
            "hostname": "test-instance",
            "label": "Test Instance",
            "tags": ["test", "vultr"],
            "backups": "disabled",
            "ddos_protection": False,
            "wait_for_ready": True,
            "wait_timeout": 300,
            "wait_interval": 10
        }
    ).create()