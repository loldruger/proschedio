import pytest
import logging

from vultr.apis.account import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_get_account_info(api_key):
    try:
        result = await get_account_info()

        if result.get("status") != 200:
            raise Exception(result)
        
        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_account_bandwidth(api_key):
    try:
        result = await get_account_bandwidth()

        if result.get("status") != 200:
            raise Exception(result)
        
        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")