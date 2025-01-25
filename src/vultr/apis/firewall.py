from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import const, get_key
from vultr.structs import firewall

async def list_firewall_groups(per_page: Optional[int], cursor: Optional[str]):
    """
    Get a list of all Firewall Groups.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_FIREWALL_GROUP_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_firewall_group(data: firewall.CreateFirewallGroupData):
    """
    Create a new Firewall Group.

    Args:
        data (CreateFirewallGroupData): The data to create the Firewall Group.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_firewall_group(firewall_group_id: str):
    """
    Get information for a Firewall Group.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_ID.assign("firewall-group-id", firewall_group_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_firewall_group(firewall_group_id: str, data: firewall.UpdateFirewallGroupData):
    """
    Update information for a Firewall Group.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
        data (UpdateFirewallGroupData): The data to update the Firewall Group.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_ID.assign("firewall-group-id", firewall_group_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_firewall_group(firewall_group_id: str):
    """
    Delete a Firewall Group.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_ID.assign("firewall-group-id", firewall_group_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_firewall_group_rules(firewall_group_id: str, per_page: Optional[int], cursor: Optional[str]):
    """
    Get the Firewall Rules for a Firewall Group.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_FIREWALL_GROUP_RULES.assign("firewall-group-id", firewall_group_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_firewall_group_rule(firewall_group_id: str, data: firewall.CreateFirewallRuleData):
    """
    Create a Firewall Rule for a Firewall Group. The attributes `ip_type`, `protocol`, `subnet`, and `subnet_size` are required.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
        data (CreateFirewallRuleData): The data to create the Firewall Rule.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_RULES.assign("firewall-group-id", firewall_group_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_firewall_group_rule(firewall_group_id: str, firewall_rule_id: str):
    """
    Get a Firewall Rule.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
        firewall_rule_id (str): The [Firewall Rule id](#operation/list-firewall-group-rules).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_RULE.assign("firewall-group-id", firewall_group_id).assign("firewall-rule-id", firewall_rule_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def delete_firewall_group_rule(firewall_group_id: str, firewall_rule_id: str):
    """
    Delete a Firewall Rule.

    Args:
        firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
        firewall_rule_id (str): The [Firewall Rule id](#operation/list-firewall-group-rules).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_FIREWALL_GROUP_RULE.assign("firewall-group-id", firewall_group_id).assign("firewall-rule-id", firewall_rule_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()