from http import HTTPMethod
from typing import Optional

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts


async def list_inferences():
    """
    List all Serverless Inference subscriptions in your account.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_INFERENCE_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def create_inference(label: str):
    """
    Create a new Serverless Inference subscription.

    Args:
        label (str): A user-supplied label for this Serverless Inference subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_INFERENCE_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"label": label}) \
        .request()


async def get_inference(inference_id: str):
    """
    Get information about a Serverless Inference subscription.

    Args:
        inference_id (str): The [Inference ID](#operation/list-inference).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_INFERENCE_ID.assign("inference-id", inference_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_inference(inference_id: str, label: str):
    """
    Update information for a Serverless Inference subscription.

    Args:
        inference_id (str): The [Inference ID](#operation/list-inference).
        label (str): A user-supplied label for this Serverless Inference subscription.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_INFERENCE_ID.assign("inference-id", inference_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({"label": label}) \
        .request()


async def delete_inference(inference_id: str):
    """
    Delete a Serverless Inference subscription.

    Args:
        inference_id (str): The [Inference ID](#operation/list-inference).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_INFERENCE_ID.assign("inference-id", inference_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def get_inference_usage(inference_id: str):
    """
    Get usage information for a Serverless Inference subscription.

    Args:
        inference_id (str): The [Inference ID](#operation/list-inference).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_INFERENCE_USAGE.assign("inference-id", inference_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()