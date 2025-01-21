from http import HTTPMethod
from proschedio import composer
from vultr import const, get_key

async def get_applications():
	return await composer.Request(const.URL_APPLICATIONS)\
		.set_method(HTTPMethod.GET)\
		.add_header("Authorization", f"Bearer {get_key()}")\
		.request()