import json
from typing import List


def load_asset_mock_data(file_name) -> List[dict]:
    with open(f'tests/domain/asset/mock_data/{file_name}.json', 'r') as f:
        return json.load(f)


def load_assets_real_part() -> List[dict]:
    mock_name = 'real_part'
    return load_asset_mock_data(mock_name)


def load_assets_valid_generated() -> List[dict]:
    mock_name = 'valid_generated'
    return load_asset_mock_data(mock_name)


def load_valid_data() -> dict:
    d = load_asset_mock_data('valid_generated')
    return d[0]