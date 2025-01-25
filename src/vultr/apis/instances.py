from http import HTTPMethod
from typing import Optional, List, Literal

from proschedio import composer
from vultr import const, get_key
from vultr.structs import instance

async def list_instances(filters: Optional[instance.ListInstancesData] = None):
    """
    List all VPS instances in your account.

    Args:
        filters (Optional[ListInstancesData]): Filters to apply to the list of instances.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if filters is not None:
        if filters._per_page is not None:
            request.add_param("per_page", filters._per_page)
        if filters._cursor is not None:
            request.add_param("cursor", filters._cursor)
        if filters._tag is not None:
            request.add_param("tag", filters._tag)
        if filters._label is not None:
            request.add_param("label", filters._label)
        if filters._main_ip is not None:
            request.add_param("main_ip", filters._main_ip)
        if filters._region is not None:
            request.add_param("region", filters._region)
        if filters._firewall_group_id is not None:
            request.add_param("firewall_group_id", filters._firewall_group_id)
        if filters._hostname is not None:
            request.add_param("hostname", filters._hostname)
        if filters._show_pending_charges is not None:
            request.add_param("show_pending_charges", filters._show_pending_charges)

    return await request.request()

async def create_instance(data: instance.CreateInstanceData):
    """
    Create a new VPS Instance in a `region` with the desired `plan`. Choose one of the following to deploy the instance:
    - `os_id`
    - `iso_id`
    - `snapshot_id`
    - `app_id`
    - `image_id`

    Args:
        data (CreateInstanceData): The data to create the VPS Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_CREATE) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_instance(instance_id: str):
    """
    Get information about an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_ID.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_instance(instance_id: str, data: instance.UpdateInstanceData):
    """
    Update information for an Instance. All attributes are optional. If not set, the attributes will retain their original values.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        data (UpdateInstanceData): The data to update the VPS Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_ID.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_instance(instance_id: str):
    """
    Delete an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_ID.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def reinstall_instance(instance_id: str, hostname: Optional[str]):
    """
    Reinstall an Instance using an optional `hostname`.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        hostname (Optional[str]): The hostname to use when reinstalling this instance.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_REINSTALL.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json")

    if hostname is not None:
        request.set_body({"hostname": hostname})
    
    return await request.request()

async def get_instance_bandwidth(instance_id: str, date_range: Optional[int]):
    """
    Get bandwidth information about an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        date_range (Optional[int]): The range of days to include (1-180). Default 30.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_BANDWIDTH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if date_range is not None:
        request.add_param("date_range", date_range)
    
    return await request.request()

async def get_instance_neighbors(instance_id: str):
    """
    Get a list of other instances in the same location as this Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_NEIGHBORS.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_instance_private_networks(instance_id: str, per_page: Optional[int], cursor: Optional[str]):
    """
    **Deprecated**: use [List Instance VPCs](#operation/list-instance-vpcs) instead. List the private networks for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_PRIVATE_NETWORKS.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def list_instance_vpcs(instance_id: str, per_page: Optional[int], cursor: Optional[str]):
    """
    List the VPCs for an Instance.

    Args:
instance_id (str): The [Instance ID](#operation/list-instances).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_VPCS.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def list_instance_vpc2s(instance_id: str, per_page: Optional[int], cursor: Optional[str]):
    """
    List the VPC 2.0 networks for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_VPC2S.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def get_instance_iso_status(instance_id: str):
    """
    Get the ISO status for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_ISO.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def attach_instance_iso(instance_id: str, iso_id: str):
    """
    Attach an ISO to an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        iso_id (str): The [ISO id](#operation/list-isos) to attach to this Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_ISO_ATTACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"iso_id": iso_id}) \
        .request()

async def detach_instance_iso(instance_id: str):
    """
    Detach the ISO from an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_ISO_DETACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def attach_instance_private_network(instance_id: str, network_id: str):
    """
    Attach Private Network to an Instance. (Deprecated)

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        network_id (str): The [Private Network id](#operation/list-networks) to attach to this Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_PRIVATE_NETWORKS_ATTACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"network_id": network_id}) \
        .request()

async def detach_instance_private_network(instance_id: str, network_id: str):
    """
    Detach Private Network from an Instance. (Deprecated)

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        network_id (str): The [Private Network id](#operation/list-networks) to detach from this Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_PRIVATE_NETWORKS_DETACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"network_id": network_id}) \
        .request()

async def attach_instance_vpc(instance_id: str, vpc_id: str):
    """
    Attach a VPC to an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        vpc_id (str): The [VPC ID](#operation/list-vpcs) to attach to this Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_VPCS_ATTACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id}) \
        .request()

async def detach_instance_vpc(instance_id: str, vpc_id: str):
    """
    Detach a VPC from an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        vpc_id (str): The [VPC ID](#operation/list-vpcs) to detach from this Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_VPCS_DETACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id}) \
        .request()

async def attach_instance_vpc2(instance_id: str, vpc_id: str, ip_address: Optional[str]):
    """
    Attach a VPC 2.0 Network to an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        vpc_id (str): The [VPC ID](#operation/list-vpc2) to attach to this Instance.
        ip_address (Optional[str]): The IP address to use for this instance on the attached VPC 2.0 network.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_VPC2_ATTACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id})

    if ip_address is not None:
        request.set_body({"vpc_id": vpc_id, "ip_address": ip_address})

    return await request.request()

async def detach_instance_vpc2(instance_id: str, vpc_id: str):
    """
    Detach a VPC 2.0 Network from an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        vpc_id (str): The [VPC ID](#operation/list-vpc2) to detach from this Instance.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_VPC2_DETACH.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"vpc_id": vpc_id}) \
        .request()

async def get_instance_backup_schedule(instance_id: str):
    """
    Get the backup schedule for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_BACKUP_SCHEDULE.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def set_instance_backup_schedule(instance_id: str, data: instance.SetInstanceBackupScheduleData):
    """
    Set the backup schedule for an Instance in UTC.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        data (SetInstanceBackupScheduleData): The data to set the backup schedule.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_BACKUP_SCHEDULE.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def restore_instance(instance_id: str, backup_id: Optional[str], snapshot_id: Optional[str]):
    """
    Restore an Instance from either `backup_id` or `snapshot_id`.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        backup_id (Optional[str]): The [Backup id](#operation/list-backups) used to restore this instance.
        snapshot_id (Optional[str]): The [Snapshot id](#operation/list-snapshots) used to restore this instance.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_RESTORE.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json")

    if backup_id is not None:
        request.set_body({"backup_id": backup_id})
    elif snapshot_id is not None:
        request.set_body({"snapshot_id": snapshot_id})

    return await request.request()

async def list_instance_ipv4(instance_id: str, public_network: Optional[bool], per_page: Optional[int], cursor: Optional[str]):
    """
    List the IPv4 information for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        public_network (Optional[bool]): If `true`, includes information about the public network adapter (such as MAC address) with the `main_ip` entry.
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_IPV4.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if public_network is not None:
        request.add_param("public_network", public_network)
    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_instance_ipv4(instance_id: str, reboot: Optional[bool]):
    """
    Create an IPv4 address for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        reboot (Optional[bool]): Set if the server is rebooted immediately after the IPv4 address is created.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_IPV4.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json")
    
    if reboot is not None:
        request.set_body({"reboot": reboot})

    return await request.request()

async def get_instance_ipv6(instance_id: str):
    """
    Get the IPv6 information for an VPS Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_IPV6.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_instance_reverse_ipv4(instance_id: str, ip: str, reverse: str):
    """
    Create a reverse IPv4 entry for an Instance. The `ip` and `reverse` attributes are required.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        ip (str): The IPv4 address.
        reverse (str): The IPv4 reverse entry.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_IPV4_REVERSE.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"ip": ip, "reverse": reverse}) \
        .request()

async def list_instance_reverse_ipv6(instance_id: str):
    """
    List the reverse IPv6 information for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_IPV6_REVERSE.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_instance_reverse_ipv6(instance_id: str, ip: str, reverse: str):
    """
    Create a reverse IPv6 entry for an Instance. The `ip` and `reverse` attributes are required. IP address must be in full, expanded format.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        ip (str): The IPv6 address in full, expanded format.
        reverse (str): The IPv6 reverse entry.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_IPV6_REVERSE.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"ip": ip, "reverse": reverse}) \
        .request()

async def set_instance_reverse_ipv4(instance_id: str, ip: str):
    """
    Set a reverse DNS entry for an IPv4 address

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        ip (str): The IPv4 address.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_IPV4_REVERSE_DEFAULT.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"ip": ip}) \
        .request()

async def delete_instance_reverse_ipv6(instance_id: str, ipv6: str):
    """
    Delete the reverse IPv6 for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        ipv6 (str): The IPv6 address.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_IPV6_REVERSE_IPV6.assign("instance-id", instance_id).assign("ipv6", ipv6)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def halt_instance(instance_id: str):
    """
    Halt an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_HALT.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_instance_user_data(instance_id: str):
    """
    Get the user-supplied, base64 encoded [user data](https://www.vultr.com/docs/manage-instance-user-data-with-the-vultr-metadata-api/) for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_INSTANCE_USER_DATA.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_instance_upgrades(instance_id: str, type: Optional[Literal["all", "applications", "os", "plans"]]):
    """
    Get available upgrades for an Instance.

    Args:
        instance_id (str): The [Instance ID](#operation/list-instances).
        type (Optional[Literal["all", "applications", "os", "plans"]]): Filter upgrade by type.

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_INSTANCE_UPGRADES.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if type is not None:
        request.add_param("type", type)

    return await request.request()