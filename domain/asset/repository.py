from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class AssetRepository(ABC):
    @abstractmethod
    def stage_assets(self, data: List[dict], version: datetime):
        pass