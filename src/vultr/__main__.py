from http import HTTPMethod
import asyncio
import os

from proschedio import composer
from vultr import set_key, get_key
from vultr.apis import _const

async def main():
    set_key(os.environ.get("VULTR_API_KEY"))

    # await composer.Request(composer.URL_ACCOUNT)\
    #     .set_method(HTTPMethod.GET)\
    #     .add_header("Authorization", f"Bearer {API_KEY}")\
    #     .add_header("Content-Type", "application/json")\
    #     .set_body({
    #         "key": "value"
    #     })\
    #     .request()

    a = await composer.Request(_const.URL_ACCOUNT)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()
    
    print(a)
    
asyncio.run(main())