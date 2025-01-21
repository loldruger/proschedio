from http import HTTPMethod
from proschedio import composer
from vultr import const, get_key

async def get_account():
    return await composer.Request(const.URL_ACCOUNT)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_account_bandwidth_info():
    return await composer.Request(const.URL_ACCOUNT_BANDWIDTH)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bear {get_key()}")\
        .request()