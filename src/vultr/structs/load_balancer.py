from typing import Optional, List, Literal, Dict


class HealthCheck:
    def __init__(self, protocol: Literal["HTTPS", "HTTP", "TCP"], port: int):
        """
        Data structure representing the health check configuration for a Vultr Load Balancer.

        Args:
            protocol (Literal["HTTPS", "HTTP", "TCP"]): The protocol to use for health checks.
            port (int): The port to use for health checks.
        """
        self.protocol: Literal["HTTPS", "HTTP", "TCP"] = protocol
        self.port: int = port
        self.path: Optional[str] = None
        self.check_interval: Optional[int] = None
        self.response_timeout: Optional[int] = None
        self.unhealthy_threshold: Optional[int] = None
        self.healthy_threshold: Optional[int] = None

    def path(self, path: str) -> "HealthCheck":
        """
        Set the HTTP Path to check. Only applies if protocol is HTTP, or HTTPS.

        Args:
            path (str): HTTP Path to check.

        Returns:
            HealthCheck: The current object with the path set.
        """
        self.path = path
        return self

    def check_interval(self, check_interval: int) -> "HealthCheck":
        """
        Set the interval between health checks.

        Args:
            check_interval (int): Interval between health checks.

        Returns:
            HealthCheck: The current object with the check interval set.
        """
        self.check_interval = check_interval
        return self

    def response_timeout(self, response_timeout: int) -> "HealthCheck":
        """
        Set the timeout before health check fails.

        Args:
            response_timeout (int): Timeout before health check fails.

        Returns:
            HealthCheck: The current object with the response timeout set.
        """
        self.response_timeout = response_timeout
        return self

    def unhealthy_threshold(self, unhealthy_threshold: int) -> "HealthCheck":
        """
        Set the number of times a check must fail before becoming unhealthy.

        Args:
            unhealthy_threshold (int): Number of times a check must fail.

        Returns:
            HealthCheck: The current object with the unhealthy threshold set.
        """
        self.unhealthy_threshold = unhealthy_threshold
        return self

    def healthy_threshold(self, healthy_threshold: int) -> "HealthCheck":
        """
        Set the number of times a check must succeed before returning to healthy status.

        Args:
            healthy_threshold (int): Number of times a check must succeed.

        Returns:
            HealthCheck: The current object with the healthy threshold set.
        """
        self.healthy_threshold = healthy_threshold
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "protocol": self.protocol,
            "port": self.port,
            "path": self.path,
            "check_interval": self.check_interval,
            "response_timeout": self.response_timeout,
            "unhealthy_threshold": self.unhealthy_threshold,
            "healthy_threshold": self.healthy_threshold,
        }
        return {k: v for k, v in data.items() if v is not None}


class ForwardingRule:
    def __init__(
        self,
        frontend_protocol: Literal["HTTP", "HTTPS", "TCP"],
        frontend_port: int,
        backend_protocol: Literal["HTTP", "HTTPS", "TCP"],
        backend_port: int,
    ):
        """
        Data structure representing a forwarding rule for a Vultr Load Balancer.

        Args:
            frontend_protocol (Literal["HTTP", "HTTPS", "TCP"]): The protocol on the Load Balancer to forward to the backend.
            frontend_port (int): The port number on the Load Balancer to forward to the backend.
            backend_protocol (Literal["HTTP", "HTTPS", "TCP"]): The protocol destination on the backend server.
            backend_port (int): The port number destination on the backend server.
        """
        self.frontend_protocol: Literal["HTTP", "HTTPS", "TCP"] = frontend_protocol
        self.frontend_port: int = frontend_port
        self.backend_protocol: Literal["HTTP", "HTTPS", "TCP"] = backend_protocol
        self.backend_port: int = backend_port

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "frontend_protocol": self.frontend_protocol,
            "frontend_port": self.frontend_port,
            "backend_protocol": self.backend_protocol,
            "backend_port": self.backend_port,
        }


class StickySession:
    def __init__(self, cookie_name: str):
        """
        Data structure representing the sticky session configuration for a Vultr Load Balancer.

        Args:
            cookie_name (str): The cookie name to make sticky.
        """
        self.cookie_name: str = cookie_name

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {"cookie_name": self.cookie_name}

from typing import Optional

class SSL:
    def __init__(self):
        """
        Data structure representing the SSL configuration for a Vultr Load Balancer.
        """
        self._private_key: Optional[str] = None
        self._certificate: Optional[str] = None
        self._chain: Optional[str] = None
        self._private_key_b64: Optional[str] = None
        self._certificate_b64: Optional[str] = None
        self._chain_b64: Optional[str] = None

    def private_key(self, private_key: str) -> "SSL":
        """
        Set the private key.

        Args:
            private_key (str): The private key.

        Returns:
            SSL: The current object with the private key set.
        """
        self._private_key = private_key
        return self

    def certificate(self, certificate: str) -> "SSL":
        """
        Set the SSL certificate.

        Args:
            certificate (str): The SSL certificate.

        Returns:
            SSL: The current object with the SSL certificate set.
        """
        self._certificate = certificate
        return self

    def chain(self, chain: str) -> "SSL":
        """
        Set the certificate chain.

        Args:
            chain (str): The certificate chain.

        Returns:
            SSL: The current object with the certificate chain set.
        """
        self._chain = chain
        return self

    def private_key_b64(self, private_key_b64: str) -> "SSL":
        """
        Set the private key base64 encoded.

        Args:
            private_key_b64 (str): The private key base64 encoded.

        Returns:
            SSL: The current object with the private key base64 encoded set.
        """
        self._private_key_b64 = private_key_b64
        return self

    def certificate_b64(self, certificate_b64: str) -> "SSL":
        """
        Set the SSL certificate base64 encoded.

        Args:
            certificate_b64 (str): The SSL certificate base64 encoded.

        Returns:
            SSL: The current object with the SSL certificate base64 encoded set.
        """
        self._certificate_b64 = certificate_b64
        return self

    def chain_b64(self, chain_b64: str) -> "SSL":
        """
        Set the certificate chain base64 encoded.

        Args:
            chain_b64 (str): The certificate chain base64 encoded.

        Returns:
            SSL: The current object with the certificate chain base64 encoded set.
        """
        self._chain_b64 = chain_b64
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "private_key": self._private_key,
            "certificate": self._certificate,
            "chain": self._chain,
            "private_key_b64": self._private_key_b64,
            "certificate_b64": self._certificate_b64,
            "chain_b64": self._chain_b64,
        }
        return {k: v for k, v in data.items() if v is not None}


class FirewallRule:
    def __init__(self, port: int, source: str, ip_type: Literal["v4", "v6"]):
        """
        Data structure representing a firewall rule for a Vultr Load Balancer.

        Args:
            port (int): Port for this rule.
            source (str): If the source string is given a value of "cloudflare" then cloudflare IPs will be supplied. Otherwise enter a IP address with subnet size that you wish to permit through the firewall.
            ip_type (Literal["v4", "v6"]): The type of IP rule.
        """
        self.port: int = port
        self.source: str = source
        self.ip_type: Literal["v4", "v6"] = ip_type

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "port": self.port,
            "source": self.source,
            "ip_type": self.ip_type,
        }

class AutoSSL:
    def __init__(self, domain_zone: str, domain_sub: Optional[str] = None):
        """
        Data structure representing the Auto SSL configuration for a Vultr Load Balancer.

        Args:
            domain_zone (str): The domain zone. (example.com)
            domain_sub (Optional[str]): (optional) Subdomain to append to the domain zone.
        """
        self.domain_zone: str = domain_zone
        self.domain_sub: Optional[str] = domain_sub

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "domain_zone": self.domain_zone,
            "domain_sub": self.domain_sub
        }
        return {k: v for k, v in data.items() if v is not None}


class CreateLoadBalancerData:
    def __init__(self, region: str):
        """
        Data structure used for creating a Vultr Load Balancer.

        Args:
            region (str): [Required] [Region id](#operation/list-regions) to create this Load Balancer.
        """
        self._region: str = region
        self._balancing_algorithm: Optional[Literal["roundrobin", "leastconn"]] = None
        self._ssl_redirect: Optional[bool] = None
        self._http2: Optional[bool] = None
        self._http3: Optional[bool] = None
        self._nodes: Optional[int] = None
        self._proxy_protocol: Optional[bool] = None
        self._timeout: Optional[int] = None
        self._health_check: Optional[HealthCheck] = None
        self._forwarding_rules: List[ForwardingRule] = []
        self._sticky_session: Optional[StickySession] = None
        self._ssl: Optional[SSL] = None
        self._label: Optional[str] = None
        self._instances: Optional[List[str]] = None
        self._firewall_rules: Optional[List[FirewallRule]] = None
        self._vpc: Optional[str] = None
        self._auto_ssl: Optional[AutoSSL] = None
        self._global_regions: Optional[List[str]] = None

    def balancing_algorithm(self, balancing_algorithm: Literal["roundrobin", "leastconn"]) -> "CreateLoadBalancerData":
        """
        Set the balancing algorithm.

        Args:
            balancing_algorithm (Literal["roundrobin", "leastconn"]): The balancing algorithm.

        Returns:
            CreateLoadBalancerData: The current object with the balancing algorithm set.
        """
        self._balancing_algorithm = balancing_algorithm
        return self

    def ssl_redirect(self, ssl_redirect: bool) -> "CreateLoadBalancerData":
        """
        Set whether to redirect all HTTP traffic to HTTPS. You must have an HTTPS rule and SSL certificate installed on the load balancer to enable this option.

        Args:
            ssl_redirect (bool): Whether to redirect HTTP traffic to HTTPS.

        Returns:
            CreateLoadBalancerData: The current object with the SSL redirect setting set.
        """
        self._ssl_redirect = ssl_redirect
        return self

    def http2(self, http2: bool) -> "CreateLoadBalancerData":
        """
        Set whether to enable HTTP2 traffic. You must have an HTTPS forwarding rule combo (HTTPS -> HTTPS) to enable this option.

        Args:
            http2 (bool): Whether to enable HTTP2 traffic.

        Returns:
            CreateLoadBalancerData: The current object with the HTTP2 setting set.
        """
        self._http2 = http2
        return self

    def http3(self, http3: bool) -> "CreateLoadBalancerData":
        """
        Set whether to enable HTTP3/QUIC traffic. You must have HTTP2 enabled.

        Args:
            http3 (bool): Whether to enable HTTP3/QUIC traffic.

        Returns:
            CreateLoadBalancerData: The current object with the HTTP3 setting set.
        """
        self._http3 = http3
        return self

    def nodes(self, nodes: int) -> "CreateLoadBalancerData":
        """
        Set the number of nodes to add to the load balancer (1-99), must be an odd number. This defaults to 1.

        Args:
            nodes (int): The number of nodes.

        Returns:
            CreateLoadBalancerData: The current object with the number of nodes set.
        """
        self._nodes = nodes
        return self

    def proxy_protocol(self, proxy_protocol: bool) -> "CreateLoadBalancerData":
        """
        Set whether to configure backend nodes to accept Proxy protocol.

        Args:
            proxy_protocol (bool): Whether to configure backend nodes to accept Proxy protocol.

        Returns:
            CreateLoadBalancerData: The current object with the proxy protocol setting set.
        """
        self._proxy_protocol = proxy_protocol
        return self

    def timeout(self, timeout: int) -> "CreateLoadBalancerData":
        """
        Set the maximum time allowed for the connection to remain inactive before timing out in seconds. This defaults to 600.

        Args:
            timeout (int): The timeout in seconds.

        Returns:
            CreateLoadBalancerData: The current object with the timeout set.
        """
        self._timeout = timeout
        return self

    def health_check(self, health_check: HealthCheck) -> "CreateLoadBalancerData":
        """
        Set the health check configuration.

        Args:
            health_check (HealthCheck): The health check configuration.

        Returns:
            CreateLoadBalancerData: The current object with the health check configuration set.
        """
        self._health_check = health_check
        return self

    def forwarding_rules(self, forwarding_rules: List[ForwardingRule]) -> "CreateLoadBalancerData":
        """
        Set the forwarding rules.

        Args:
            forwarding_rules (List[ForwardingRule]): The forwarding rules.

        Returns:
            CreateLoadBalancerData: The current object with the forwarding rules set.
        """
        self._forwarding_rules = forwarding_rules
        return self

    def sticky_session(self, sticky_session: StickySession) -> "CreateLoadBalancerData":
        """
        Set the sticky session configuration.

        Args:
            sticky_session (StickySession): The sticky session configuration.

        Returns:
            CreateLoadBalancerData: The current object with the sticky session configuration set.
        """
        self._sticky_session = sticky_session
        return self

    def ssl(self, ssl: SSL) -> "CreateLoadBalancerData":
        """
        Set the SSL configuration.

        Args:
            ssl (SSL): The SSL configuration.

        Returns:
            CreateLoadBalancerData: The current object with the SSL configuration set.
        """
        self._ssl = ssl
        return self

    def label(self, label: str) -> "CreateLoadBalancerData":
        """
        Set the label for your Load Balancer.

        Args:
            label (str): The label.

        Returns:
            CreateLoadBalancerData: The current object with the label set.
        """
        self._label = label
        return self

    def instances(self, instances: List[str]) -> "CreateLoadBalancerData":
        """
        Set an array of instances IDs that you want attached to the load balancer.

        Args:
            instances (List[str]): The instance IDs.

        Returns:
            CreateLoadBalancerData: The current object with the instance IDs set.
        """
        self._instances = instances
        return self

    def firewall_rules(self, firewall_rules: List[FirewallRule]) -> "CreateLoadBalancerData":
        """
        Set the firewall rules.

        Args:
            firewall_rules (List[FirewallRule]): The firewall rules.

        Returns:
            CreateLoadBalancerData: The current object with the firewall rules set.
        """
        self._firewall_rules = firewall_rules
        return self

    def vpc(self, vpc: str) -> "CreateLoadBalancerData":
        """
        Set the ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network.

        Args:
            vpc (str): The VPC ID.
Returns:
            CreateLoadBalancerData: The current object with the VPC ID set.
        """
        self._vpc = vpc
        return self

    def auto_ssl(self, auto_ssl: AutoSSL) -> "CreateLoadBalancerData":
        """
        Set the Auto SSL configuration.

        Args:
            auto_ssl (AutoSSL): The Auto SSL configuration.

        Returns:
            CreateLoadBalancerData: The current object with the Auto SSL configuration set.
        """
        self._auto_ssl = auto_ssl
        return self

    def global_regions(self, global_regions: List[str]) -> "CreateLoadBalancerData":
        """
        Set the array of [Region ids](#operation/list-regions) to deploy child Load Balancers to.

        Args:
            global_regions (List[str]): The region IDs.

        Returns:
            CreateLoadBalancerData: The current object with the region IDs set.
        """
        self._global_regions = global_regions
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "region": self._region,
            "balancing_algorithm": self._balancing_algorithm,
            "ssl_redirect": self._ssl_redirect,
            "http2": self._http2,
            "http3": self._http3,
            "nodes": self._nodes,
            "proxy_protocol": self._proxy_protocol,
            "timeout": self._timeout,
            "health_check": self._health_check.to_json() if self._health_check is not None else None,
            "forwarding_rules": [rule.to_json() for rule in self._forwarding_rules] if self._forwarding_rules else None,
            "sticky_session": self._sticky_session.to_json() if self._sticky_session is not None else None,
            "ssl": self._ssl.to_json() if self._ssl is not None else None,
            "label": self._label,
            "instances": self._instances,
            "firewall_rules": [rule.to_json() for rule in self._firewall_rules] if self._firewall_rules else None,
            "vpc": self._vpc,
            "auto_ssl": self._auto_ssl.to_json() if self._auto_ssl is not None else None,
            "global_regions": self._global_regions,
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateLoadBalancerData:
    def __init__(self):
        """
        Data structure used for updating a Vultr Load Balancer.
        """
        self._ssl: Optional[SSL] = None
        self._sticky_session: Optional[StickySession] = None
        self._forwarding_rules: Optional[List[ForwardingRule]] = None
        self._health_check: Optional[HealthCheck] = None
        self._proxy_protocol: Optional[bool] = None
        self._timeout: Optional[int] = None
        self._ssl_redirect: Optional[bool] = None
        self._http2: Optional[bool] = None
        self._http3: Optional[bool] = None
        self._nodes: Optional[int] = None
        self._balancing_algorithm: Optional[Literal["roundrobin", "leastconn"]] = None
        self._instances: Optional[List[str]] = None
        self._label: Optional[str] = None
        self._vpc: Optional[str] = None
        self._firewall_rules: Optional[List[FirewallRule]] = None
        self._auto_ssl: Optional[AutoSSL] = None
        self._global_regions: Optional[List[str]] = None

    def ssl(self, ssl: SSL) -> "UpdateLoadBalancerData":
        """
        Set the SSL configuration.

        Args:
            ssl (SSL): The SSL configuration.

        Returns:
            UpdateLoadBalancerData: The current object with the SSL configuration set.
        """
        self._ssl = ssl
        return self

    def sticky_session(self, sticky_session: StickySession) -> "UpdateLoadBalancerData":
        """
        Set the sticky session configuration.

        Args:
            sticky_session (StickySession): The sticky session configuration.

        Returns:
            UpdateLoadBalancerData: The current object with the sticky session configuration set.
        """
        self._sticky_session = sticky_session
        return self

    def forwarding_rules(self, forwarding_rules: List[ForwardingRule]) -> "UpdateLoadBalancerData":
        """
        Set the forwarding rules.

        Args:
            forwarding_rules (List[ForwardingRule]): The forwarding rules.

        Returns:
            UpdateLoadBalancerData: The current object with the forwarding rules set.
        """
        self._forwarding_rules = forwarding_rules
        return self

    def health_check(self, health_check: HealthCheck) -> "UpdateLoadBalancerData":
        """
        Set the health check configuration.

        Args:
            health_check (HealthCheck): The health check configuration.

        Returns:
            UpdateLoadBalancerData: The current object with the health check configuration set.
        """
        self._health_check = health_check
        return self

    def proxy_protocol(self, proxy_protocol: bool) -> "UpdateLoadBalancerData":
        """
        Set whether to configure backend nodes to accept Proxy protocol.

        Args:
            proxy_protocol (bool): Whether to configure backend nodes to accept Proxy protocol.

        Returns:
            UpdateLoadBalancerData: The current object with the proxy protocol setting set.
        """
        self._proxy_protocol = proxy_protocol
        return self

    def timeout(self, timeout: int) -> "UpdateLoadBalancerData":
        """
        Set the maximum time allowed for the connection to remain inactive before timing out in seconds. This defaults to 600.

        Args:
            timeout (int): The timeout in seconds.

        Returns:
            UpdateLoadBalancerData: The current object with the timeout set.
        """
        self._timeout = timeout
        return self

    def ssl_redirect(self, ssl_redirect: bool) -> "UpdateLoadBalancerData":
        """
        Set whether to redirect all HTTP traffic to HTTPS.

        Args:
            ssl_redirect (bool): Whether to redirect HTTP traffic to HTTPS.

        Returns:
            UpdateLoadBalancerData: The current object with the SSL redirect setting set.
        """
        self._ssl_redirect = ssl_redirect
        return self

    def http2(self, http2: bool) -> "UpdateLoadBalancerData":
        """
        Set whether to enable HTTP2 traffic.

        Args:
            http2 (bool): Whether to enable HTTP2 traffic.

        Returns:
            UpdateLoadBalancerData: The current object with the HTTP2 setting set.
        """
        self._http2 = http2
        return self

    def http3(self, http3: bool) -> "UpdateLoadBalancerData":
        """
        Set whether to enable HTTP3/QUIC traffic.

        Args:
            http3 (bool): Whether to enable HTTP3/QUIC traffic.

        Returns:
            UpdateLoadBalancerData: The current object with the HTTP3 setting set.
        """
        self._http3 = http3
        return self

    def nodes(self, nodes: int) -> "UpdateLoadBalancerData":
        """
        Set the number of nodes to add to the load balancer (1-99), must be an odd number.

        Args:
            nodes (int): The number of nodes.

        Returns:
            UpdateLoadBalancerData: The current object with the number of nodes set.
        """
        self._nodes = nodes
        return self

    def balancing_algorithm(self, balancing_algorithm: Literal["roundrobin", "leastconn"]) -> "UpdateLoadBalancerData":
        """
        Set the balancing algorithm.

        Args:
            balancing_algorithm (Literal["roundrobin", "leastconn"]): The balancing algorithm.

        Returns:
            UpdateLoadBalancerData: The current object with the balancing algorithm set.
        """
        self._balancing_algorithm = balancing_algorithm
        return self

    def instances(self, instances: List[str]) -> "UpdateLoadBalancerData":
        """
        Send the complete array of Instances IDs that should be attached to this Load Balancer.

        Args:
            instances (List[str]): The instance IDs.

        Returns:
            UpdateLoadBalancerData: The current object with the instance IDs set.
        """
        self._instances = instances
        return self

    def label(self, label: str) -> "UpdateLoadBalancerData":
        """
        Set the label for your Load Balancer.

        Args:
            label (str): The label.

        Returns:
            UpdateLoadBalancerData: The current object with the label set.
        """
        self._label = label
        return self

    def vpc(self, vpc: str) -> "UpdateLoadBalancerData":
        """
        Set the ID of the VPC you wish to use. If a VPC ID is omitted it will default to the public network.

        Args:
            vpc (str): The VPC ID.

        Returns:
            UpdateLoadBalancerData: The current object with the VPC ID set.
        """
        self._vpc = vpc
        return self

    def firewall_rules(self, firewall_rules: List[FirewallRule]) -> "UpdateLoadBalancerData":
        """
        Set the firewall rules.

        Args:
            firewall_rules (List[FirewallRule]): The firewall rules.

        Returns:
            UpdateLoadBalancerData: The current object with the firewall rules set.
        """
        self._firewall_rules = firewall_rules
        return self

    def auto_ssl(self, auto_ssl: AutoSSL) -> "UpdateLoadBalancerData":
        """
        Set the Auto SSL configuration.

        Args:
            auto_ssl (AutoSSL): The Auto SSL configuration.

        Returns:
            UpdateLoadBalancerData: The current object with the Auto SSL configuration set.
        """
        self._auto_ssl = auto_ssl
        return self

    def global_regions(self, global_regions: List[str]) -> "UpdateLoadBalancerData":
        """
        Set the array of [Region ids](#operation/list-regions) to deploy child Load Balancers to.

        Args:
            global_regions (List[str]): The region IDs.

        Returns:
            UpdateLoadBalancerData: The current object with the region IDs set.
        """
        self._global_regions = global_regions
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "ssl": self._ssl.to_json() if self._ssl is not None else None,
            "sticky_session": self._sticky_session.to_json() if self._sticky_session is not None else None,
            "forwarding_rules": [rule.to_json() for rule in self._forwarding_rules] if self._forwarding_rules else None,
            "health_check": self._health_check.to_json() if self._health_check is not None else None,
            "proxy_protocol": self._proxy_protocol,
            "timeout": self._timeout,
            "ssl_redirect": self._ssl_redirect,
            "http2": self._http2,
            "http3": self._http3,
            "nodes": self._nodes,
            "balancing_algorithm": self._balancing_algorithm,
            "instances": self._instances,
            "label": self._label,
            "vpc": self._vpc,
            "firewall_rules": [rule.to_json() for rule in self._firewall_rules] if self._firewall_rules else None,
            "auto_ssl": self._auto_ssl.to_json() if self._auto_ssl is not None else None,
            "global_regions": self._global_regions,
        }
        return {k: v for k, v in data.items() if v is not None}