from infrastructure.client.db.data_model import TableMetaData


class AssetTableMetaData(TableMetaData):
    TABLE_NAME = 'asset'
    PRIMARY_KEYS = ['id', 'version']