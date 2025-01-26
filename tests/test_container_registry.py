import pytest
import logging

from vultr.apis.container_registry import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_container_registries(api_key):
    """
    Test list_container_registries function with different parameter combinations.
    """
    try:
        # Test case 1: List all container registries
        result = await list_container_registries()
        if result.get("status") != 200:
            raise Exception(f"list_container_registries (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_container_registries - no params) - Response Data:\n%s", result)

        # Test case 2: List container registries with per_page
        result = await list_container_registries(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_container_registries(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_container_registries - per_page) - Response Data:\n%s", result)

        # Test case 3: List container registries with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_container_registries(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_container_registries(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_container_registries - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_container_registry(api_key):
    """
    Test create_container_registry function.
    """
    try:
        # Test case: Create a container registry (replace with your desired parameters)
        create_data = container.CreateContainerRegistryData(name="your_registry_name", public=False, region="ewr", plan="starter")  # Replace with your desired parameters
        result = await create_container_registry(data=create_data)

        if result.get("status") != 201 and result.get("status") != 409:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_container_registry(api_key):
    """
    Test get_container_registry function.
    """
    try:
        # Test case: Get container registry information (replace 'your_registry_id' with a real registry ID)
        result = await get_container_registry(registry_id="your_registry_id")  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_container_registry(api_key):
    """
    Test update_container_registry function.
    """
    try:
        # Test case: Update container registry information (replace 'your_registry_id' with a real registry ID)
        update_data = container.UpdateContainerRegistryData(public=True)
        result = await update_container_registry(registry_id="your_registry_id", data=update_data)  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_container_registry(api_key):
    """
    Test delete_container_registry function.
    """
    try:
        # Test case: Delete container registry (replace 'your_registry_id' with a real registry ID)
        result = await delete_container_registry(registry_id="your_registry_id")  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_container_repositories(api_key):
    """
    Test list_container_repositories function.
    """
    try:
        # Test case: List container repositories (replace 'your_registry_id' with a real registry ID)
        result = await list_container_repositories(registry_id="your_registry_id")  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_container_repository(api_key):
    """
    Test get_container_repository function.
    """
    try:
        # Test case: Get container repository information (replace with your desired parameters)
        result = await get_container_repository(registry_id="your_registry_id", repository_image="your_repository_image")  # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_container_repository(api_key):
    """
    Test update_container_repository function.
    """
    try:
        # Test case: Update container repository information (replace with your desired parameters)
        update_data = container.UpdateContainerRepositoryData(description="Updated description")
        result = await update_container_repository(registry_id="your_registry_id", repository_image="your_repository_image", data=update_data)  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_container_repository(api_key):
    """
    Test delete_container_repository function.
    """
    try:
        # Test case: Delete container repository (replace with your desired parameters)
        result = await delete_container_repository(registry_id="your_registry_id", repository_image="your_repository_image")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_docker_credentials(api_key):
    """
    Test get_docker_credentials function.
    """
    try:
        # Test case: Get Docker credentials (replace 'your_registry_id' with a real registry ID)
        result = await get_docker_credentials(registry_id="your_registry_id")  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_kubernetes_docker_credentials(api_key):
    """
    Test get_kubernetes_docker_credentials function.
    """
    try:
        # Test case: Get Kubernetes Docker credentials (replace 'your_registry_id' with a real registry ID)
        result = await get_kubernetes_docker_credentials(registry_id="your_registry_id")  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_robots(api_key):
    """
    Test list_robots function.
    """
    try:
        # Test case: List robots (replace 'your_registry_id' with a real registry ID)
        result = await list_robots(registry_id="your_registry_id")  # Replace 'your_registry_id' with a real registry ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_robot(api_key):
    """
    Test get_robot function.
    """
    try:
        # Test case: Get robot information (replace with your desired parameters)
        result = await get_robot(registry_id="your_registry_id", robot_name="your_robot_name")  # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_robot(api_key):
    """
    Test update_robot function.
    """
    try:
        # Test case: Update robot information (replace with your desired parameters)
        update_data = container.UpdateContainerRobotData()
        update_data.description = "Updated robot description"
        result = await update_robot(registry_id="your_registry_id", robot_name="your_robot_name", data=update_data)  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_robot(api_key):
    """
    Test delete_robot function.
    """
    try:
        # Test case: Delete robot (replace with your desired parameters)
        result = await delete_robot(registry_id="your_registry_id", robot_name="your_robot_name")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_artifacts(api_key):
    """
    Test list_artifacts function.
    """
    try:
        # Test case: List artifacts (replace with your desired parameters)
        result = await list_artifacts(registry_id="your_registry_id", repository_image="your_repository_image")  # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_artifact(api_key):
    """
    Test get_artifact function.
    """
    try:
        # Test case: Get artifact information (replace with your desired parameters)
        result = await get_artifact(registry_id="your_registry_id", repository_image="your_repository_image", artifact_digest="your_artifact_digest")  # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_delete_artifact(api_key):
    """
    Test delete_artifact function.
    """
    try:
        # Test case: Delete artifact (replace with your desired parameters)
        result = await delete_artifact(registry_id="your_registry_id", repository_image="your_repository_image", artifact_digest="your_artifact_digest")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_regions(api_key):
    """
    Test list_regions function.
    """
    try:
        # Test case: List regions
        result = await list_regions()

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")