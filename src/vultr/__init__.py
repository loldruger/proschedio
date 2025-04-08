from ..apiV2 import const
from .structs import *

API_KEY: str = ""

def set_key(key: str):
	global API_KEY
	API_KEY = key

def get_key() -> str:
	return API_KEY

__all__ = ['set_key', 'get_key', 'const']