from http import HTTPMethod
from typing import Optional, List

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts
from vultr.structs import container

async def list_container_registries(per_page: Optional[int], cursor: Optional[str]):
    """
    List All Container Registry Subscriptions for this account

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and max is 500.
        cursor (Optional[str]): Cursor for paging. See Meta and pagination.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_CONTAINER_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_container_registry(data: container.CreateContainerRegistryData):
    """
    Create a new Container Registry Subscription

    Args:
        data (CreateContainerRegistryData): The data to create the registry subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_container_registry(registry_id: str):
    """
    Get a single Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ID.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_container_registry(registry_id: str, data: container.UpdateContainerRegistryData):
    """
    Update a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        data (UpdateContainerRegistryData): The data to update the registry subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ID.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_container_registry(registry_id: str):
    """
    Delete a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ID.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_container_repositories(registry_id: str):
    """
    List All Repositories in a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_REPOSITORY.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_container_repository(registry_id: str, repository_image: str):
    """
    Get a single Repository in a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        repository_image (str): Target repository name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_REPOSITORY_IMAGE.assign("registry-id", registry_id).assign("repository-image", repository_image)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_container_repository(registry_id: str, repository_image: str, data: container.UpdateContainerRepositoryData):
    """
    Update a Repository in a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        repository_image (str): Target repository name.
        data (UpdateContainerRepositoryData): The data to update the repository.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_REPOSITORY_IMAGE.assign("registry-id", registry_id).assign("repository-image", repository_image)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_container_repository(registry_id: str, repository_image: str):
    """
    Delete a Repository from a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        repository_image (str): Target repository name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_REPOSITORY_IMAGE.assign("registry-id", registry_id).assign("repository-image", repository_image)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_docker_credentials(registry_id: str, expiry_seconds: Optional[int], read_write: Optional[bool]):
    """
    Create a fresh set of Docker Credentials for this Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        expiry_seconds (Optional[int]): The duration in seconds for which the credentials are valid (default: 0).
        read_write (Optional[bool]): If false, credentials will be read-only (default: false).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_CONTAINER_DOCKER_CREDENTIALS.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.OPTIONS) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if expiry_seconds is not None:
        request.add_param("expiry_seconds", expiry_seconds)
    if read_write is not None:
        request.add_param("read_write", read_write)

    return await request.request()
    
async def get_kubernetes_docker_credentials(registry_id: str, expiry_seconds: Optional[int], read_write: Optional[bool], base64_encode: Optional[bool]):
    """
    Create a fresh set of Docker Credentials for this Container Registry Subscription and return them in a Kubernetes friendly YAML format

    Args:
        registry_id (str): The Container Registry Subscription ID.
        expiry_seconds (Optional[int]): The duration in seconds for which the credentials are valid (default: 0).
        read_write (Optional[bool]): If false, credentials will be read-only (default: false).
        base64_encode (Optional[bool]): If true, encodes the output in base64 (default: false).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(Consts.URL_CONTAINER_KUBERNETES_DOCKER_CREDENTIALS.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.OPTIONS) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if expiry_seconds is not None:
        request.add_param("expiry_seconds", expiry_seconds)
    if read_write is not None:
        request.add_param("read_write", read_write)
    if base64_encode is not None:
        request.add_param("base64_encode", base64_encode)

    return await request.request()

async def list_robots(registry_id: str):
    """
    List All Robots in a Conainer Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ROBOTS.assign("registry-id", registry_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_robot(registry_id: str, robot_name: str):
    """
    Get a single Robot in a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        robot_name (str): The Robot name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ROBOT.assign("registry-id", registry_id).assign("robot-name", robot_name)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_robot(registry_id: str, robot_name: str, data: container.UpdateContainerRobotData):
    """
    Update the description, disable, duration, and add or remove access, in a Container Registry Subscription Robot

    Args:
        registry_id (str): The Container Registry Subscription ID.
        robot_name (str): The Robot name.
        data (UpdateContainerRobotData): The data to update the robot.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ROBOT.assign("registry-id", registry_id).assign("robot-name", robot_name)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_robot(registry_id: str, robot_name: str):
    """
    Deletes a Robot from a Container Registry Subscription

    Args:
        registry_id (str): The Container Registry Subscription ID.
        robot_name (str): The Robot name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ROBOT.assign("registry-id", registry_id).assign("robot-name", robot_name)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_artifacts(registry_id: str, repository_image: str):
    """
    List All Artifacts in a Container Registry Repository

    Args:
        registry_id (str): The Container Registry Subscription ID.
        repository_image (str): The Repository Name.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ARTIFACTS.assign("registry-id", registry_id).assign("repository-image", repository_image)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_artifact(registry_id: str, repository_image: str, artifact_digest: str):
    """
    Get a single Artifact in a Container Registry Repository

    Args:
        registry_id (str): The Container Registry Subscription ID.
        repository_image (str): The Repository Name.
        artifact_digest (str): The Artifact Digest.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ARTIFACT.assign("registry-id", registry_id).assign("repository-image", repository_image).assign("artifact-digest", artifact_digest)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def delete_artifact(registry_id: str, repository_image: str, artifact_digest: str):
    """
    Deletes an Artifact from a Container Registry Repository

    Args:
        registry_id (str): The Container Registry Subscription ID.
        repository_image (str): The Repository Name.
        artifact_digest (str): The Artifact Digest.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_ARTIFACT.assign("registry-id", registry_id).assign("repository-image", repository_image).assign("artifact-digest", artifact_digest)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_regions():
    """
    List All Regions where a Container Registry can be deployed

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_CONTAINER_LIST_REGIONS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()