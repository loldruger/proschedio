import pytest
import logging

from vultr.apis.marketplace import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_get_marketplace_app_variables(api_key):
    """
    Test get_marketplace_app_variables function.
    """
    try:
        # Test case: Get marketplace app variables (replace 'your_image_id' with a real image ID)
        result = await get_marketplace_app_variables(image_id="your_image_id")  # Replace 'your_image_id' with a real image ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")