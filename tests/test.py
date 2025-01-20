import unittest
import os
from unittest.mock import patch, AsyncMock
from http import HTTPMethod

from vultr_py import set_key
from vultr_py import composer

class TestRequest(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        set_key(os.environ.get("VULTR_API_KEY"))
        print("Setup")
        