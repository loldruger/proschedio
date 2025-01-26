from .apis import _const

API_KEY: str = ""

def set_key(key: str):
	global API_KEY
	API_KEY = key

def get_key() -> str:
	return API_KEY

__all__ = ['set_key', 'get_key', '_const']