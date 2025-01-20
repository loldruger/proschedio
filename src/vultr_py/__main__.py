import asyncio
from http import HTTPMethod

import src.vultr_py as vultr_py
import src.vultr_py.composer as composer

async def main():
    await composer.Request(composer.URL_ACCOUNT)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", "Bearer {token}")\
        .add_header("Content-Type", "application/json")\
        .set_body({
            "key": "value"
        })\
        .request()

asyncio.run(main())