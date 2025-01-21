from http import HTTPMethod
from proschedio import composer
from vultr import const, get_key

async def get_backups():
    return await composer.Request(const.URL_BACKUPS)\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()

async def get_backup(backup_id: int):
    return await composer.Request(const.URL_BACKUPS.assign("backup_id", str(backup_id)))\
        .set_method(HTTPMethod.GET)\
        .add_header("Authorization", f"Bearer {get_key()}")\
        .request()