from http import HTTPMethod
from typing import Optional, List

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import kubenetes


async def list_kubernetes_clusters():
    """
    List all Kubernetes clusters currently deployed.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_kubernetes_cluster(label: str, region: str, version: str, node_pools: List[kubenetes.NodePoolData], ha_controlplanes: Optional[bool], enable_firewall: Optional[bool]):
    """
    Create Kubernetes Cluster.

    Args:
        label (str): The label for your Kubernetes cluster.
        region (str): Region you want to deploy VKE in.
        version (str): Version of Kubernetes you want to deploy.
        node_pools (List[NodePoolData]): Array of node pool objects.
        ha_controlplanes (Optional[bool]): Whether a highly available control planes configuration should be deployed.
        enable_firewall (Optional[bool]): Whether a [Firewall Group](#tag/firewall) should be deployed and managed by this cluster.

    Returns:
        requests.Response: The response from the API.
    """
    body = {
        "label": label,
        "region": region,
        "version": version,
        "ha_controlplanes": ha_controlplanes,
        "enable_firewall": enable_firewall,
        "node_pools": [node_pool.to_json() for node_pool in node_pools],
    }
    return await composer.Request(_const.URL_KUBERNETES_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({k: v for k, v in body.items() if v is not None}) \
        .request()


async def get_kubernetes_cluster(vke_id: str):
    """
    Get Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_ID.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_kubernetes_cluster(vke_id: str, label: Optional[str]):
    """
    Update Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.
        label (Optional[str]): Label for the Kubernetes cluster.

    Returns:
        requests.Response: The response from the API.
    """
    body = {"label": label}
    return await composer.Request(_const.URL_KUBERNETES_ID.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({k: v for k, v in body.items() if v is not None}) \
        .request()


async def delete_kubernetes_cluster(vke_id: str):
    """
    Delete Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_ID.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def delete_kubernetes_cluster_and_resources(vke_id: str):
    """
    Delete Kubernetes Cluster and all related resources.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_DELETE_WITH_LINKED_RESOURCES.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_kubernetes_resources(vke_id: str):
    """
    Get the block storage volumes and load balancers deployed by the specified Kubernetes cluster.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_RESOURCES.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_available_kubernetes_upgrades(vke_id: str):
    """
    Get the available upgrades for the specified Kubernetes cluster.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_AVAILABLE_UPGRADES.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def start_kubernetes_upgrade(vke_id: str, upgrade_version: str):
    """
    Start a Kubernetes cluster upgrade.

    Args:
        vke_id (str): The VKE ID.
        upgrade_version (str): The version you're upgrading to.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_UPGRADES.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"upgrade_version": upgrade_version}) \
        .request()


async def list_kubernetes_nodepools(vke_id: str):
    """
    List all available NodePools on a Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOLS.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_kubernetes_nodepool(vke_id: str, data: kubenetes.NodePoolData):
    """
    Create NodePool for a Existing Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.
        data (NodePoolData): The data to create the NodePool.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOLS.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_kubernetes_nodepool(vke_id: str, nodepool_id: str):
    """
    Get Nodepool from a Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.
        nodepool_id (str): The NodePool ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOL.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_kubernetes_nodepool(vke_id: str, nodepool_id: str, node_quantity: Optional[int], tag: Optional[str], auto_scaler: Optional[bool], min_nodes: Optional[int], max_nodes: Optional[int], labels: Optional[dict]):
    """
    Update a Nodepool on a Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.
        nodepool_id (str): The NodePool ID.
        node_quantity (Optional[int]): Number of instances in the NodePool.
        tag (Optional[str]): Tag for node pool.
        auto_scaler (Optional[bool]): Option to use the auto scaler.
        min_nodes (Optional[int]): Auto scaler minimum nodes.
        max_nodes (Optional[int]): Auto scaler maximum nodes.
        labels (Optional[dict]): Map of key/value pairs defining labels.

    Returns:
        requests.Response: The response from the API.
    """
    body = {
        "node_quantity": node_quantity,
        "tag": tag,
        "auto_scaler": auto_scaler,
        "min_nodes": min_nodes,
        "max_nodes": max_nodes,
        "labels": labels,
    }
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOL.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({k: v for k, v in body.items() if v is not None}) \
        .request()


async def delete_kubernetes_nodepool(vke_id: str, nodepool_id: str):
    """
    Delete a NodePool from a Kubernetes Cluster.

    Args:
        vke_id (str): The VKE ID.
        nodepool_id (str): The NodePool ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOL.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def delete_kubernetes_nodepool_instance(vke_id: str, nodepool_id: str, node_id: str):
    """
    Delete a single nodepool instance from a given Nodepool.

    Args:
        vke_id (str): The VKE ID.
        nodepool_id (str): The NodePool ID.
        node_id (str): The Instance ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOL_INSTANCE.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).assign("node-id", node_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def recycle_kubernetes_nodepool_instance(vke_id: str, nodepool_id: str, node_id: str):
    """
    Recycle a specific NodePool Instance.

    Args:
        vke_id (str): The VKE ID.
        nodepool_id (str): The NodePool ID.
        node_id (str): Node ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_NODEPOOL_INSTANCE_RECYCLE.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).assign("node-id", node_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_kubernetes_config(vke_id: str):
    """
    Get Kubernetes Cluster Kubeconfig.

    Args:
        vke_id (str): The VKE ID.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_CONFIG.assign("vke-id", vke_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_kubernetes_versions():
    """
    Get a list of supported Kubernetes versions.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_KUBERNETES_VERSIONS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()