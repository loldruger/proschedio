import http
import http.client
from . import composer

API_KEY: str = ""

def set_key(key: str):
	global API_KEY
	API_KEY = key