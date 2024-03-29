import pytest

from ApiClient import ApiClient

BASE_URL = 'https://petstore.swagger.io/v2/pet'


@pytest.fixture
def create_api_client():
    api_client = ApiClient(BASE_URL)
    return api_client
