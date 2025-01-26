import pytest
import logging

from vultr.apis.applications import list_applications

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_applications(api_key):
    try:
        result = await list_applications(type="all", per_page=10, cursor='bmV4dF9fMTAzNA==')

        if result.get("status") != 200:
            raise Exception(result)
        
        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")