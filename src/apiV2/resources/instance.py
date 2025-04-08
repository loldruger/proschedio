# src/proschedio/apiV2/resources/instance.py
# Functions related to CRUD and listing of Vultr instances.
# Note: Imports are adjusted assuming this file is part of the proschedio package
# and needs access to the original vultr implementation details for now.

import logging
from http import HTTPMethod
import os
from typing import Optional

# Assuming composer, get_key, Consts are accessible or refactored later
# For now, import from the original vultr locations
from ....vultr.apis import Consts
from request import Request
from ..structs import instance as instance_structs

logger = logging.getLogger(__name__)

async def list_instances(filters: Optional[instance_structs.ListInstancesData]):
    """
    List all VPS instances in your account. (Vultr specific)
    """
    request = Request(Consts.URL_INSTANCE_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}")

    if filters is not None:
        # Apply filters using the filter object's method
        filters.apply_params(request)

    return await request.request()

async def create_instance(data: instance_structs.CreateInstanceData):
    """
    Create a new Vultr VPS Instance. (Vultr specific)
    """
    return await Request(Consts.URL_INSTANCE_CREATE) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_instance(instance_id: str):
    """
    Get information about a Vultr Instance. (Vultr specific)
    """
    return await Request(Consts.URL_INSTANCE_ID.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
        .request()

async def update_instance(instance_id: str, data: instance_structs.UpdateInstanceData):
    """
    Update information for a Vultr Instance. (Vultr specific)
    """
    return await Request(Consts.URL_INSTANCE_ID.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_instance(instance_id: str):
    """
    Delete a Vultr Instance. (Vultr specific)
    """
    return await Request(Consts.URL_INSTANCE_ID.assign("instance-id", instance_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {os.environ.get("VULTR_API_KEY")}") \
        .request()

# Other potential resource-centric functions like getting bandwidth, neighbors, user_data, upgrades
# could also be placed here or kept as actions depending on interpretation.
# For now, keeping them as actions.
