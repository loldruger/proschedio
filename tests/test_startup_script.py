import pytest
import logging

from vultr.apis.startup_script import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_startup_scripts(api_key):
    """
    Test list_startup_scripts function with different parameter combinations.
    """
    try:
        # Test case 1: List all startup scripts
        result = await list_startup_scripts()
        if result.get("status") != 200:
            raise Exception(f"list_startup_scripts (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_startup_scripts - no params) - Response Data:\n%s", result)

        # Test case 2: List startup scripts with per_page
        result = await list_startup_scripts(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_startup_scripts(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_startup_scripts - per_page) - Response Data:\n%s", result)

        # Test case 3: List startup scripts with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_startup_scripts(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_startup_scripts(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_startup_scripts - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_startup_script(api_key):
    """
    Test create_startup_script function.
    """
    try:
        # Test case: Create a startup script (replace with your desired parameters)
        result = await create_startup_script(name="test-startup-script", script="#!/bin/bash\necho 'Hello from startup script!'", type="boot")

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_startup_script(api_key):
    """
    Test get_startup_script function.
    """
    try:
        # Test case: Get startup script information (replace 'your_startup_script_id' with a real startup script ID)
        result = await get_startup_script(startup_id="your_startup_script_id")  # Replace 'your_startup_script_id' with a real startup script ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_startup_script(api_key):
    """
    Test update_startup_script function.
    """
    try:
        # Test case: Update startup script information (replace 'your_startup_script_id' with a real startup script ID)
        update_data = startup_script.UpdateStartupScriptData().name("updated-startup-script").script("#!/bin/bash\necho 'Updated startup script!'")
        result = await update_startup_script(startup_id="your_startup_script_id", data=update_data)  # Replace 'your_startup_script_id' with a real startup script ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_startup_script(api_key):
#     """
#     Test delete_startup_script function.
#     """
#     try:
#         # Test case: Delete startup script (replace 'your_startup_script_id' with a real startup script ID)
#         result = await delete_startup_script(startup_id="your_startup_script_id")  # Replace 'your_startup_script_id' with a real startup script ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")