import pytest
import logging

from http import HTTPMethod

from _core import composer
from vultr import const

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_example(capsys, api_key):
    try:
        a = await composer.Request(const.URL_ACCOUNT)\
            .set_method(HTTPMethod.GET)\
            .add_header("Authorization", f"Bearer {api_key}")\
            .request()

        if a.get("status") != 200:
            raise Exception(a)
        
        logger.info("\nResponse Data:\n%s", a)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")
