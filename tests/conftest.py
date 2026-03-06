import pytest
import requests

BASE_URL = "https://fakestoreapi.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    return s


@pytest.fixture
def payload_login():
    return {
        "username": "mor_2314",
        "password": "83r5^_"
    }
