import logging
from datetime import datetime
from decimal import Decimal

from pygeoapi.provider.postgresql import PostgreSQLProvider

LOGGER = logging.getLogger(__name__)


class GeoramaSqlProvider(PostgreSQLProvider):
    
    def __init__(self, provider_def):
        super().__init__(provider_def)
    
    def get_fields(self):
        """
        Return fields (columns) from PostgreSQL table

        :returns: dict of fields
        """
        
        # sql-schema only allows these types, so we need to map from sqlalchemy
        # string, number, integer, object, array, boolean, null,
        # https://json-schema.org/understanding-json-schema/reference/type.html
        column_type_map = {
            bool: 'boolean',
            datetime: 'string',
            Decimal: 'number',
            dict: 'object',
            float: 'number',
            int: 'integer',
            str: 'string'
            }
        default_type = 'string'
        
        # https://json-schema.org/understanding-json-schema/reference/string#built-in-formats  # noqa
        column_format_map = {
            'date': 'date',
            'interval': 'duration',
            'time': 'time',
            'timestamp': 'date-time'
            }
        
        def _column_type_to_json_schema_type(column_type):
            try:
                python_type = column_type.python_type
            except NotImplementedError:
                LOGGER.warning(f'Unsupported column type {column_type}')
                return default_type
            else:
                try:
                    return column_type_map[python_type]
                except KeyError:
                    LOGGER.warning(f'Unsupported column type {column_type}')
                    return default_type
        
        def _column_format_to_json_schema_format(column_type):
            try:
                ct = str(column_type).lower()
                return column_format_map[ct]
            except KeyError:
                LOGGER.debug('No string format detected')
                return None
        
        if not self._fields:
            for column in self.table_model.__table__.columns:
                LOGGER.debug(f'Testing {column.name}')
                if column.name == self.geom:
                    continue
                
                self._fields[str(column.name)] = {
                    'type': _column_type_to_json_schema_type(column.type),
                    'format': _column_format_to_json_schema_format(column.type)
                    }
        
        return self._fields
