import os
import pytest
import asyncio
import pytest_asyncio  # Import pytest_asyncio

import logging
import colorlog

# Adjust the import path to reflect the src layout
from vultr.vultr import Vultr
from vultr import set_key  # Assuming set_key is available here

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

logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@pytest.fixture(scope="session")
def api_key():
    """Fixture to get the API key from environment variable."""
    key = os.environ.get("VULTR_API_KEY")
    if not key:
        pytest.skip("VULTR_API_KEY environment variable not set")
    set_key(key)  # Uncomment this line to set the key globally
    return key

@pytest_asyncio.fixture  # No scope specified, defaults to "function"
async def vultr_client(api_key):
    """Fixture to provide an initialized Vultr API client for each test function."""
    client = Vultr()
    yield client
    # No cleanup needed here as Vultr class doesn't manage sessions directly