from typing import Final

from _core.composer import Provider, Url

URL_ACCOUNT: Final[Url] = Url(Provider.VULTR).uri("account")
URL_ACCOUNT_BANDWIDTH: Final[Url] = Url(Provider.VULTR).uri("account/bandwidth")

URL_APPLICATIONS: Final[Url] = Url(Provider.VULTR).uri("applications")

URL_BACKUPS: Final[Url] = Url(Provider.VULTR).uri("backups")
URL_BACKUPS_ID: Final[Url] = Url(Provider.VULTR).uri("backups/{backup-id}")

URL_BARE_METAL: Final[Url] = Url(Provider.VULTR).uri("bare-metal")
URL_BARE_METAL_IP4: Final[Url] = Url(Provider.VULTR).uri("bare-metal/{baremetal-id}/ipv4")
URL_BARE_METAL_IP6: Final[Url] = Url(Provider.VULTR).uri("bare-metal/{baremetal-id}/ipv6")

# async def list_baremetal_instance(req_method: HTTPMethod.GET|HTTPMethod.POST):
# 	return await Request(URL_BARE_METAL)\
# 		.set_method(req_method)\
# 		.add_header("Authorization", f"Bearer {get_key()}")\
# 		.request()


# list_baremetal_instance