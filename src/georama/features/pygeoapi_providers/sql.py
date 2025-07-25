import logging
from pygeoapi.provider.postgresql import PostgreSQLProvider

LOGGER = logging.getLogger(__name__)


class GeoramaSqlProvider(PostgreSQLProvider):

    def __init__(self, provider_def):
        self.properties = provider_def.get("properties", {})

        super().__init__(provider_def)

        self._fields = provider_def.get("field_constraints", {})

    def get_fields(self):
        """
        Return fields (columns) from PostgreSQL table

        :returns: dict of fields
        """
        return self._fields
