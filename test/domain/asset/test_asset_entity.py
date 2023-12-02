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

def test_assets_with_generated_data():
    """
    Tested using mock data generated
        within the range that theoretically conforms to Asset.
    """
    mock_name = 'assets_valid_generated'
    test_data = _load_asset_mock_data(mock_name)
    for asset in test_data:
        Asset(**asset)