import os
import pytest

import logging
import colorlog

from vultr import get_key, set_key

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    }
))

logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@pytest.fixture(scope="session")
def api_key():
    set_key(os.environ.get("VULTR_API_KEY"))
    
    if not get_key():
        pytest.skip("VULTR_API_KEY environment variable not set")

    return get_key()