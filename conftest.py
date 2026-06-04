import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: quick critical tests")
    config.addinivalue_line("markers", "regression: deeper regression tests")