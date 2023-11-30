from .base import TableMetaData


class AssetMetaData(TableMetaData):
    TABLE_NAME = 'asset'
    PRIMARY_KEYS = ['id', 'version']