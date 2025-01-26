import pytest
import logging

from vultr.apis.inference import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_inferences(api_key):
    """
    Test list_inferences function.
    """
    try:
        # Test case: List all inferences
        result = await list_inferences()
        if result.get("status") != 200:
            raise Exception(f"list_inferences failed: {result}")
        logger.info("\nTest Case (list_inferences - no params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_inference(api_key):
    """
    Test create_inference function.
    """
    try:
        # Test case: Create an inference (replace with your desired label)
        result = await create_inference(label="test-inference")

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_inference(api_key):
    """
    Test get_inference function.
    """
    try:
        # Test case: Get inference information (replace 'your_inference_id' with a real inference ID)
        result = await get_inference(inference_id="your_inference_id") # Replace 'your_inference_id' with a real inference ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_inference(api_key):
    """
    Test update_inference function.
    """
    try:
        # Test case: Update inference information (replace 'your_inference_id' with a real inference ID)
        result = await update_inference(inference_id="your_inference_id", label="updated-test-inference") # Replace 'your_inference_id' with a real inference ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_inference(api_key):
#     """
#     Test delete_inference function.
#     """
#     try:
#         # Test case: Delete inference (replace 'your_inference_id' with a real inference ID)
#         result = await delete_inference(inference_id="your_inference_id") # Replace 'your_inference_id' with a real inference ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_inference_usage(api_key):
    """
    Test get_inference_usage function.
    """
    try:
        # Test case: Get inference usage (replace 'your_inference_id' with a real inference ID)
        result = await get_inference_usage(inference_id="your_inference_id") # Replace 'your_inference_id' with a real inference ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")