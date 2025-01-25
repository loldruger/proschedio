from typing import Optional, List, Dict


class NodePoolData:
    def __init__(self, node_quantity: int, label: str, plan: str):
        """
        Data structure used for creating/updating a Vultr Kubernetes NodePool.

        Args:
            node_quantity (int): Number of instances to deploy in this nodepool.
            label (str): Label for this nodepool.
            plan (str): Plan you want this nodepool to use.
        """
        self._node_quantity: int = node_quantity
        self._label: str = label
        self._plan: str = plan
        self._tag: Optional[str] = None
        self._auto_scaler: Optional[bool] = None
        self._min_nodes: Optional[int] = None
        self._max_nodes: Optional[int] = None
        self._labels: Optional[Dict[str, str]] = None

    def tag(self, tag: str) -> "NodePoolData":
        """
        Set the tag for the node pool.

        Args:
            tag (str): Tag for node pool.

        Returns:
            NodePoolData: The current object with the tag set.
        """
        self._tag = tag
        return self

    def auto_scaler(self, auto_scaler: bool) -> "NodePoolData":
        """
        Set the option to use the auto scaler.

        Args:
            auto_scaler (bool): Option to use the auto scaler.

        Returns:
            NodePoolData: The current object with the auto scaler option set.
        """
        self._auto_scaler = auto_scaler
        return self

    def min_nodes(self, min_nodes: int) -> "NodePoolData":
        """
        Set the auto scaler minimum nodes.

        Args:
            min_nodes (int): Auto scaler minimum nodes.

        Returns:
            NodePoolData: The current object with the minimum nodes set.
        """
        self._min_nodes = min_nodes
        return self

    def max_nodes(self, max_nodes: int) -> "NodePoolData":
        """
        Set the auto scaler maximum nodes.

        Args:
            max_nodes (int): Auto scaler maximum nodes.

        Returns:
            NodePoolData: The current object with the maximum nodes set.
        """
        self._max_nodes = max_nodes
        return self

    def labels(self, labels: Dict[str, str]) -> "NodePoolData":
        """
        Set the map of key/value pairs defining labels.

        Args:
            labels (Dict[str, str]): Map of key/value pairs defining labels.

        Returns:
            NodePoolData: The current object with the labels set.
        """
        self._labels = labels
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "node_quantity": self._node_quantity,
            "label": self._label,
            "plan": self._plan,
            "tag": self._tag,
            "auto_scaler": self._auto_scaler,
            "min_nodes": self._min_nodes,
            "max_nodes": self._max_nodes,
            "labels": self._labels,
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateKubernetesData:
    def __init__(self, label: str, region: str, version: str, node_pools: List[NodePoolData]):
        """
        Data structure used for creating a Vultr Kubernetes Engine (VKE) cluster.

        Args:
            label (str): The label for your Kubernetes cluster.
            region (str): Region you want to deploy VKE in.
            version (str): Version of Kubernetes you want to deploy.
            node_pools (List[NodePoolData]): Array of node pool objects.
        """
        self._label: str = label
        self._region: str = region
        self._version: str = version
        self._ha_controlplanes: Optional[bool] = None
        self._enable_firewall: Optional[bool] = None
        self._node_pools: List[NodePoolData] = node_pools

    def ha_controlplanes(self, ha_controlplanes: bool) -> "CreateKubernetesData":
        """
        Set whether a highly available control planes configuration should be deployed.

        Args:
            ha_controlplanes (bool): Whether a highly available control planes configuration should be deployed.

        Returns:
            CreateKubernetesData: The current object with the HA control planes setting set.
        """
        self._ha_controlplanes = ha_controlplanes
        return self

    def enable_firewall(self, enable_firewall: bool) -> "CreateKubernetesData":
        """
        Set whether a [Firewall Group](#tag/firewall) should be deployed and managed by this cluster.

        Args:
            enable_firewall (bool): Whether a Firewall Group should be deployed.

        Returns:
            CreateKubernetesData: The current object with the firewall setting set.
        """
        self._enable_firewall = enable_firewall
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "label": self._label,
            "region": self._region,
            "version": self._version,
            "ha_controlplanes": self._ha_controlplanes,
            "enable_firewall": self._enable_firewall,
            "node_pools": [node_pool.to_json() for node_pool in self._node_pools],
        }
		
        return {k: v for k, v in data.items() if v is not None}
    
class UpdateKubernetesData:
    def __init__(self, label: Optional[str]):
        """
        Data structure used for updating a Vultr Kubernetes Engine (VKE) cluster.

        Args:
            label (Optional[str]): Label for the Kubernetes cluster.
        """
        self._label: Optional[str] = label

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {"label": self._label}
        return {k: v for k, v in data.items() if v is not None}
    
class UpdateNodePoolData:
    def __init__(self, node_quantity: Optional[int]):
        """
        Data structure used for updating a NodePool on a Vultr Kubernetes Engine (VKE) cluster.

        Args:
            node_quantity (Optional[int]): Number of instances in the NodePool.
        """
        self._node_quantity: Optional[int] = node_quantity
        self._tag: Optional[str] = None
        self._auto_scaler: Optional[bool] = None
        self._min_nodes: Optional[int] = None
        self._max_nodes: Optional[int] = None
        self._labels: Optional[Dict[str, str]] = None

    def node_quantity(self, node_quantity: int) -> "UpdateNodePoolData":
        """
        Set the number of instances in the NodePool.

        Args:
            node_quantity (int): Number of instances in the NodePool.

        Returns:
            UpdateNodePoolData: The current object with the node quantity set.
        """
        self._node_quantity = node_quantity
        return self

    def tag(self, tag: str) -> "UpdateNodePoolData":
        """
        Set the tag for the node pool.

        Args:
            tag (str): Tag for node pool.

        Returns:
            UpdateNodePoolData: The current object with the tag set.
        """
        self._tag = tag
        return self

    def auto_scaler(self, auto_scaler: bool) -> "UpdateNodePoolData":
        """
        Set the option to use the auto scaler.

        Args:
            auto_scaler (bool): Option to use the auto scaler.

        Returns:
            UpdateNodePoolData: The current object with the auto scaler option set.
        """
        self._auto_scaler = auto_scaler
        return self

    def min_nodes(self, min_nodes: int) -> "UpdateNodePoolData":
        """
        Set the auto scaler minimum nodes.

        Args:
            min_nodes (int): Auto scaler minimum nodes.

        Returns:
            UpdateNodePoolData: The current object with the minimum nodes set.
        """
        self._min_nodes = min_nodes
        return self

    def max_nodes(self, max_nodes: int) -> "UpdateNodePoolData":
        """
        Set the auto scaler maximum nodes.

        Args:
            max_nodes (int): Auto scaler maximum nodes.

        Returns:
            UpdateNodePoolData: The current object with the maximum nodes set.
        """
        self._max_nodes = max_nodes
        return self
    
    def labels(self, labels: Dict[str, str]) -> "UpdateNodePoolData":
        """
        Set the map of key/value pairs defining labels.

        Args:
            labels (Dict[str, str]): Map of key/value pairs defining labels.

        Returns:
            UpdateNodePoolData: The current object with the labels set.
        """
        self._labels = labels
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "node_quantity": self._node_quantity,
            "tag": self._tag,
            "auto_scaler": self._auto_scaler,
            "min_nodes": self._min_nodes,
            "max_nodes": self._max_nodes,
            "labels": self._labels,
        }
        return {k: v for k, v in data.items() if v is not None}