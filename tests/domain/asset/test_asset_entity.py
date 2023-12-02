import json
from datetime import datetime
from typing import List, Optional

import pytest

from domain.asset.entity import Asset
from tests.helper import generate_invalid_values


def _load_asset_mock_data(file_name) -> List[dict]:
    with open(f'tests/domain/asset/mock_data/{file_name}.json', 'r') as f:
        return json.load(f)


def _load_valid_data() -> dict:
    d = _load_asset_mock_data('real_part')
    return d[0]


def _set_data_to_asset(file_name):
    test_data = _load_asset_mock_data(file_name)
    for asset in test_data:
        Asset(**asset)



def test_assets_with_real_data():
    """
    This test is performed on a piece of real data.

    Note:
    There is no version column in the real data.
    The version column was added by myself
        because I wanted to track the asset information
        by date in chronological order.
    """
    mock_name = 'real_part'
    _set_data_to_asset(mock_name)

def test_assets_with_generated_data():
    """
    Tested using mock data generated
        within the range that theoretically conforms to Asset.
    """
    mock_name = 'valid_generated'
    _set_data_to_asset(mock_name)


@pytest.mark.parametrize("invalid_id", generate_invalid_values(str))
def test_invalid_id(invalid_id):
    """
    This method tests the following on the ID.
        1. ID is Null.
        2. ID is not str.
    """
    data = _load_valid_data()
    data['id'] = invalid_id
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_version", generate_invalid_values(Optional[datetime]))
def test_invalid_version(invalid_version):
    """
    This method tests the following on the version.
        1. version is not datetime.
    """
    data = _load_valid_data()
    data['version'] = invalid_version
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_asset_class", generate_invalid_values(str))
def test_invalid_asset_class(invalid_asset_class):
    """
    This method tests the following on the asset_class.
        1. asset_class is Null.
        2. asset_class is not str.
    """
    data = _load_valid_data()
    data['asset_class'] = invalid_asset_class
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_exchange", generate_invalid_values(str))
def test_invalid_exchange(invalid_exchange):
    """
    This method tests the following on the exchange.
        1. exchange is Null.
        2. exchange is not str.
    """
    data = _load_valid_data()
    data['exchange'] = invalid_exchange
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_symbol", generate_invalid_values(str))
def test_invalid_symbol(invalid_symbol):
    """
    This method tests the following on the symbol.
        1. symbol is Null.
        2. symbol is not str.
    """
    data = _load_valid_data()
    data['symbol'] = invalid_symbol
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_name", generate_invalid_values(str))
def test_invalid_name(invalid_name):
    """
    This method tests the following on the name.
        1. name is Null.
        2. name is not str.
    """
    data = _load_valid_data()
    data['name'] = invalid_name
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_status", generate_invalid_values(str))
def test_invalid_status(invalid_status):
    """
    This method tests the following on the status.
        1. status is Null.
        2. status is not str.
    """
    data = _load_valid_data()
    data['status'] = invalid_status
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_tradable", generate_invalid_values(bool))
def test_invalid_tradable(invalid_tradable):
    """
    This method tests the following on the tradable.
        1. tradable is not bool.
    """
    data = _load_valid_data()
    data['tradable'] = invalid_tradable
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_marginable", generate_invalid_values(bool))
def test_invalid_marginable(invalid_marginable):
    """
    This method tests the following on the marginable.
        1. marginable is not bool.
    """
    data = _load_valid_data()
    data['marginable'] = invalid_marginable
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_shortable", generate_invalid_values(bool))
def test_invalid_shortable(invalid_shortable):
    """
    This method tests the following on the shortable.
        1. shortable is not bool.
    """
    data = _load_valid_data()
    data['shortable'] = invalid_shortable
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_easy_to_borrow", generate_invalid_values(bool))
def test_invalid_easy_to_borrow(invalid_easy_to_borrow):
    """
    This method tests the following on the easy_to_borrow.
        1. easy_to_borrow is not bool.
    """
    data = _load_valid_data()
    data['easy_to_borrow'] = invalid_easy_to_borrow
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_fractionable", generate_invalid_values(bool))
def test_invalid_fractionable(invalid_fractionable):
    """
    This method tests the following on the fractionable.
        1. fractionable is not bool.
    """
    data = _load_valid_data()
    data['fractionable'] = invalid_fractionable
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_maintenance_margin_requirement", generate_invalid_values(Optional[float]))
def test_invalid_maintenance_margin_requirement(invalid_maintenance_margin_requirement):
    """
    This method tests the following on the maintenance_margin_requirement.
        1. maintenance_margin_requirement is not float.
    """
    data = _load_valid_data()
    data['maintenance_margin_requirement'] = invalid_maintenance_margin_requirement
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_attributes", generate_invalid_values(Optional[List[str]]))
def test_invalid_attributes(invalid_attributes):
    """
    This method tests the following on the attributes.
        1. attributes is not list of str.
    """
    data = _load_valid_data()
    data['attributes'] = invalid_attributes
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_min_order_size", generate_invalid_values(Optional[float]))
def test_invalid_min_order_size(invalid_min_order_size):
    """
    This method tests the following on the min_order_size.
        1. min_order_size is not float.
    """
    data = _load_valid_data()
    data['min_order_size'] = invalid_min_order_size
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_min_trade_increment", generate_invalid_values(Optional[float]))
def test_invalid_min_trade_increment(invalid_min_trade_increment):
    """
    This method tests the following on the min_trade_increment.
        1. min_trade_increment is not float.
    """
    data = _load_valid_data()
    data['min_trade_increment'] = invalid_min_trade_increment
    with pytest.raises(ValueError):
        Asset(**data)

@pytest.mark.parametrize("invalid_price_increment", generate_invalid_values(Optional[float]))
def test_invalid_price_increment(invalid_price_increment):
    """
    This method tests the following on the price_increment.
        1. price_increment is not float.
    """
    data = _load_valid_data()
    data['price_increment'] = invalid_price_increment
    with pytest.raises(ValueError):
        Asset(**data)
