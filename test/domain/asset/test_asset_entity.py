import json

from domain.asset.entity import Asset


def _load_asset_mock_data(file_name):
    with open(f'test/domain/asset/mock_data/{file_name}.json', 'r') as f:
        return json.load(f)


def test_assets_with_real_data():
    """
    This test is performed on a piece of real data.

    Note:
    There is no version column in the real data.
    The version column was added by myself
        because I wanted to track the asset information
        by date in chronological order.
    """
    mock_name = 'assets_real_part'
    test_data = _load_asset_mock_data(mock_name)
    for asset in test_data:
        Asset(**asset)

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