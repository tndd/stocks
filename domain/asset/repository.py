from abc import ABC, abstractmethod
from typing import List

from .entity import Asset
from .value import AssetType


class AssetRepository(ABC):
    @abstractmethod
    def fetch_assets(self, asset_type: AssetType) -> List[Asset]:
        pass

    @abstractmethod
    def store_assets(self, assets: List[Asset]) -> None:
        """
        Store the given Asset list.
        The same version is assigned to each saved Asset.
        """
        pass