import pytest
import logging

from vultr.apis.users import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_users(api_key):
    """
    Test list_users function with different parameter combinations.
    """
    try:
        # Test case 1: List all users
        result = await list_users()
        if result.get("status") != 200:
            raise Exception(f"list_users (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_users - no params) - Response Data:\n%s", result)

        # Test case 2: List users with per_page
        result = await list_users(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_users(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_users - per_page) - Response Data:\n%s", result)

        # Test case 3: List users with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_users(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_users(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_users - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_user(api_key):
    """
    Test create_user function.
    """
    try:
        # Test case: Create a user (replace with your desired parameters)
        create_data = users.CreateUserData(email="testuser@example.com", name="Test User", password="password123")
        result = await create_user(data=create_data)

        if result.get("status") != 201 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_user(api_key):
    """
    Test get_user function.
    """
    try:
        # Test case: Get user information (replace 'your_user_id' with a real user ID)
        result = await get_user(user_id="your_user_id")  # Replace 'your_user_id' with a real user ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_user(api_key):
    """
    Test update_user function.
    """
    try:
        # Test case: Update user information (replace 'your_user_id' with a real user ID)
        update_data = users.UpdateUserData().name("Updated User Name")
        result = await update_user(user_id="your_user_id", data=update_data)  # Replace 'your_user_id' with a real user ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_user(api_key):
#     """
#     Test delete_user function.
#     """
#     try:
#         # Test case: Delete user (replace 'your_user_id' with a real user ID)
#         result = await delete_user(user_id="your_user_id")  # Replace 'your_user_id' with a real user ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")