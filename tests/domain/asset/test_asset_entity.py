from typing import List

from domain.asset.entity import Asset
from tests.domain.asset.mock_data.loader import (load_assets_real_part,
                                                 load_assets_valid_generated)


def _try_set_data_to_asset(test_data: List[dict]):
    for asset in test_data:
        assert Asset(**asset)



def test_assets_with_real_data():
    """
    This test is performed on a piece of real data.

    Note:
    There is no version column in the real data.
    The version column was added by myself
        because I wanted to track the asset information
        by date in chronological order.
    """
    d = load_assets_real_part()
    _try_set_data_to_asset(d)

def test_assets_with_generated_data():
    """
    Tested using mock data generated
        within the range that theoretically conforms to Asset.
    """
    d = load_assets_valid_generated()
    _try_set_data_to_asset(d)
