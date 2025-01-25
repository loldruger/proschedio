from http import HTTPMethod
from typing import Optional, List, Literal

from proschedio import composer
from vultr import const, get_key
from vultr.structs import load_balancer


async def list_load_balancers(per_page: Optional[int] = None, cursor: Optional[str] = None):
    """
    List the Load Balancers in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_LOAD_BALANCER_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_load_balancer(data: load_balancer.CreateLoadBalancerData):
    """
    Create a new Load Balancer in a particular `region`.

    Args:
        data (CreateLoadBalancerData): The data to create the Load Balancer.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_CREATE) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_load_balancer(load_balancer_id: str):
    """
    Get information for a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_ID.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_load_balancer(load_balancer_id: str, data: load_balancer.UpdateLoadBalancerData):
    """
    Update information for a Load Balancer. All attributes are optional. If not set, the attributes will retain their original values.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        data (UpdateLoadBalancerData): The data to update the Load Balancer.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_ID.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def delete_load_balancer(load_balancer_id: str):
    """
    Delete a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_ID.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def delete_load_balancer_ssl(load_balancer_id: str):
    """
    Delete a Load Balancer SSL.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_SSL.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def delete_load_balancer_auto_ssl(load_balancer_id: str):
    """
    Remove a Load Balancer Auto SSL. This will not remove an ssl certificate from the load balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_AUTO_SSL.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_load_balancer_forwarding_rules(load_balancer_id: str, per_page: Optional[int] = None, cursor: Optional[str] = None):
    """
    List the fowarding rules for a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_LOAD_BALANCER_FORWARDING_RULES.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def create_load_balancer_forwarding_rule(load_balancer_id: str, data: load_balancer.ForwardingRule):
    """
    Create a new forwarding rule for a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        data (ForwardingRule): The data to create the forwarding rule.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_FORWARDING_RULES.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()


async def get_load_balancer_forwarding_rule(load_balancer_id: str, forwarding_rule_id: str):
    """
    Get information for a Forwarding Rule on a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        forwarding_rule_id (str): The [Forwarding Rule id](#operation/list-load-balancer-forwarding-rules).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_FORWARDING_RULE.assign("load-balancer-id", load_balancer_id).assign("forwarding-rule-id", forwarding_rule_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def delete_load_balancer_forwarding_rule(load_balancer_id: str, forwarding_rule_id: str):
    """
    Delete a Forwarding Rule on a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        forwarding_rule_id (str): The [Forwarding Rule id](#operation/list-load-balancer-forwarding-rules).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_FORWARDING_RULE.assign("load-balancer-id", load_balancer_id).assign("forwarding-rule-id", forwarding_rule_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def list_load_balancer_firewall_rules(load_balancer_id: str, per_page: Optional[int] = None, cursor: Optional[str] = None):
    """
    List the firewall rules for a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_LOAD_BALANCER_FIREWALL_RULES.assign("load-balancer-id", load_balancer_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()


async def get_load_balancer_firewall_rule(load_balancer_id: str, firewall_rule_id: str):
    """
    Get a firewall rule for a Load Balancer.

    Args:
        load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
        firewall_rule_id (str): The [Firewall Rule id](#operation/list-loadbalancer-firewall-rules).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_LOAD_BALANCER_FIREWALL_RULE.assign("load-balancer-id", load_balancer_id).assign("firewall-rule-id", firewall_rule_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()