import os
from typing import List

import pytest
from dotenv import load_dotenv

from infrastructure.api.client import AlpacaApiClient

load_dotenv()

client = AlpacaApiClient(
    api_key=os.getenv('API_KEY'),
    secret_key=os.getenv('SECRET_KEY')
)

@pytest.fixture
def api_client() -> AlpacaApiClient:
    return AlpacaApiClient(
        api_key=os.getenv('API_KEY'),
        secret_key=os.getenv('SECRET_KEY')
    )


@pytest.mark.api
def test_fetch_stock_assets(api_client: AlpacaApiClient):
    """
    Testing of stock asset acquisitions.
    Checking is minimal, almost only looking to see if the value is returned.
    """
    response_data: List[dict] = api_client.fetch_stock_assets()
    assert isinstance(response_data, list), "Response from fetch_stock_assets is not a list"


@pytest.mark.api
def test_fetch_crypto_assets(api_client):
    """
    Testing of crypto asset acquisitions.
    Checking is minimal, almost only looking to see if the value is returned.
    """
    response_data: List[dict] = api_client.fetch_crypto_assets()
    assert isinstance(response_data, list), "Response from fetch_crypto_assets is not a list"
