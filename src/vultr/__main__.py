import os
import asyncio

from http import HTTPMethod

from dotenv import load_dotenv
from proschedio import composer
from vultr import set_key, get_key
from vultr.apis import _const

load_dotenv()

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

if __name__ == "__main__":
    asyncio.run(main())
