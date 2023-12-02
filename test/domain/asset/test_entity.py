import pytest
from domain.model.asset import Asset


def test_asset_model_conversion_valid_data():
    valid_data = {
        "id": "f1c42f1f-2444-4714-b866-3144d3548ccd",
        'version': '2022-01-01T00:00:00',
        "asset_class": "us_equity",
        "exchange": "OTC",
        "symbol": "RPCCF",
        "name": "RPCG PCL Ordinary Shares (Thailand)",
        "status": "inactive",
        "tradable": False,
        "marginable": False,
        "shortable": False,
        "easy_to_borrow": False,
        "fractionable": False,
        "min_order_size": None,
        "min_trade_increment": None,
        "price_increment": None,
        "maintenance_margin_requirement": 100.0,
        "attributes": []
    }
    asset = Asset(**valid_data)
    for key, value in valid_data.items():
        assert getattr(asset, key) == value

# def test_asset_model_conversion_insufficient_data():
#     insufficient_data = {
#         "id": "f1c42f1f-2444-4714-b866-3144d3548ccd",
#         'version': '2022-01-01T00:00:00'
#     }
#     with pytest.raises(TypeError):
#         Asset(**insufficient_data)

# def test_asset_model_conversion_excessive_data():
#     excessive_data = {
#         'id': '1',
#         'version': 'v1',
#         'asset_class': 'class1',
#         'exchange': 'exchange1',
#         'symbol': 'symbol1',
#         'name': 'name1',
#         'status': 'active',
#         'tradable': True,
#         'marginable': True,
#         'shortable': True,
#         'easy_to_borrow': True,
#         'fractionable': True,
#         'maintenance_margin_requirement': 'requirement1',
#         'attributes': 'attributes1',
#         'min_order_size': 1.0,
#         'min_trade_increment': 0.1,
#         'price_increment': 0.01,
#         'extra': 'extra'
#     }
#     with pytest.raises(TypeError):
#         Asset(**excessive_data)