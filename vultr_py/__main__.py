from http import HTTPMethod
import asyncio
import os

import vultr_py as vultr_py
import vultr_py.composer as composer

async def main():
    vultr_py.set_key(os.environ["VULTR_API_KEY"])

    # await composer.Request(composer.URL_ACCOUNT)\
    #     .set_method(HTTPMethod.GET)\
    #     .add_header("Authorization", f"Bearer {vultr_py.API_KEY}")\
    #     .add_header("Content-Type", "application/json")\
    #     .set_body({
    #         "key": "value"
    #     })\
    #     .request()

    a = await composer.Request(composer.URL_ACCOUNT)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {vultr_py.API_KEY}")\
        .request()
    
    print(a)
    
asyncio.run(main())