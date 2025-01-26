import pytest
import logging

from vultr.apis.kubernetes import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_kubernetes_clusters(api_key):
    """
    Test list_kubernetes_clusters function.
    """
    try:
        # Test case: List all Kubernetes clusters
        result = await list_kubernetes_clusters()
        if result.get("status") != 200:
            raise Exception(f"list_kubernetes_clusters failed: {result}")
        logger.info("\nTest Case (list_kubernetes_clusters - no params) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_kubernetes_cluster(api_key):
    """
    Test create_kubernetes_cluster function.
    """
    try:
        # Test case: Create a Kubernetes cluster (replace with your desired parameters)
        node_pool_data = kubenetes.NodePoolData(node_quantity=1, label="test-nodepool", plan="vc2-1c-2gb")
        create_data = kubenetes.CreateKubernetesData(label="test-kubernetes-cluster", region="ewr", version="v1.28.2+1", node_pools=[node_pool_data])
        result = await create_kubernetes_cluster(label=create_data.label, region=create_data.region, version=create_data.version, ha_controlplanes=create_data.ha_controlplanes, enable_firewall=create_data.enable_firewall, node_pools=create_data.node_pools)

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_kubernetes_cluster(api_key):
    """
    Test get_kubernetes_cluster function.
    """
    try:
        # Test case: Get Kubernetes cluster information (replace 'your_vke_id' with a real VKE ID)
        result = await get_kubernetes_cluster(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_kubernetes_cluster(api_key):
    """
    Test update_kubernetes_cluster function.
    """
    try:
        # Test case: Update Kubernetes cluster information (replace 'your_vke_id' with a real VKE ID)
        result = await update_kubernetes_cluster(vke_id="your_vke_id", label="updated-kubernetes-cluster")  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_kubernetes_cluster(api_key):
#     """
#     Test delete_kubernetes_cluster function.
#     """
#     try:
#         # Test case: Delete Kubernetes cluster (replace 'your_vke_id' with a real VKE ID)
#         result = await delete_kubernetes_cluster(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_kubernetes_cluster_and_resources(api_key):
#     """
#     Test delete_kubernetes_cluster_and_resources function.
#     """
#     try:
#         # Test case: Delete Kubernetes cluster and resources (replace 'your_vke_id' with a real VKE ID)
#         result = await delete_kubernetes_cluster_and_resources(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_kubernetes_resources(api_key):
    """
    Test get_kubernetes_resources function.
    """
    try:
        # Test case: Get Kubernetes resources (replace 'your_vke_id' with a real VKE ID)
        result = await get_kubernetes_resources(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_available_kubernetes_upgrades(api_key):
    """
    Test get_available_kubernetes_upgrades function.
    """
    try:
        # Test case: Get available Kubernetes upgrades (replace 'your_vke_id' with a real VKE ID)
        result = await get_available_kubernetes_upgrades(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_start_kubernetes_upgrade(api_key):
    """
    Test start_kubernetes_upgrade function.
    """
    try:
        # Test case: Start Kubernetes upgrade (replace with your desired parameters)
        result = await start_kubernetes_upgrade(vke_id="your_vke_id", upgrade_version="v1.28.2+1")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_kubernetes_nodepools(api_key):
    """
    Test list_kubernetes_nodepools function.
    """
    try:
        # Test case: List Kubernetes nodepools (replace 'your_vke_id' with a real VKE ID)
        result = await list_kubernetes_nodepools(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_kubernetes_nodepool(api_key):
    """
    Test create_kubernetes_nodepool function.
    """
    try:
        # Test case: Create a Kubernetes nodepool (replace with your desired parameters)
        create_data = kubenetes.NodePoolData(node_quantity=1, label="test-nodepool", plan="vc2-1c-2gb")
        result = await create_kubernetes_nodepool(vke_id="your_vke_id", data=create_data)  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_kubernetes_nodepool(api_key):
    """
    Test get_kubernetes_nodepool function.
    """
    try:
        # Test case: Get Kubernetes nodepool information (replace with your desired parameters)
        result = await get_kubernetes_nodepool(vke_id="your_vke_id", nodepool_id="your_nodepool_id")  # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_kubernetes_nodepool(api_key):
    """
    Test update_kubernetes_nodepool function.
    """
    try:
        # Test case: Update Kubernetes nodepool information (replace with your desired parameters)
        result = await update_kubernetes_nodepool(vke_id="your_vke_id", nodepool_id="your_nodepool_id", node_quantity=2)  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_kubernetes_nodepool(api_key):
#     """
#     Test delete_kubernetes_nodepool function.
#     """
#     try:
#         # Test case: Delete Kubernetes nodepool (replace with your desired parameters)
#         result = await delete_kubernetes_nodepool(vke_id="your_vke_id", nodepool_id="your_nodepool_id")  # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_kubernetes_nodepool_instance(api_key):
#     """
#     Test delete_kubernetes_nodepool_instance function.
#     """
#     try:
#         # Test case: Delete Kubernetes nodepool instance (replace with your desired parameters)
#         result = await delete_kubernetes_nodepool_instance(vke_id="your_vke_id", nodepool_id="your_nodepool_id", node_id="your_node_id")  # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_recycle_kubernetes_nodepool_instance(api_key):
    """
    Test recycle_kubernetes_nodepool_instance function.
    """
    try:
        # Test case: Recycle Kubernetes nodepool instance (replace with your desired parameters)
        result = await recycle_kubernetes_nodepool_instance(vke_id="your_vke_id", nodepool_id="your_nodepool_id", node_id="your_node_id")  # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_kubernetes_config(api_key):
    """
    Test get_kubernetes_config function.
    """
    try:
        # Test case: Get Kubernetes config (replace 'your_vke_id' with a real VKE ID)
        result = await get_kubernetes_config(vke_id="your_vke_id")  # Replace 'your_vke_id' with a real VKE ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_kubernetes_versions(api_key):
    """
    Test get_kubernetes_versions function.
    """
    try:
        # Test case: Get Kubernetes versions
        result = await get_kubernetes_versions()

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")