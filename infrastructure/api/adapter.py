from typing import List

from domain.asset.entity import Asset


def to_asset_entity(data: List[dict]) -> Asset:
    return [Asset(**asset_data) for asset_data in data]