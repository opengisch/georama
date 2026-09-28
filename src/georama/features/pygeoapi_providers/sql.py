import logging

from pygeoapi.provider.sql import GenericSQLProvider, PostgreSQLProvider

LOGGER = logging.getLogger(__name__)


class GeoramaSqlProvider(PostgreSQLProvider):
    # pygeoapi's PostgreSQLProvider hardcodes the psycopg2 driver, but only
    # psycopg 3 is installed, so we use SQLAlchemy's psycopg 3 dialect instead.
    driver_name = "postgresql+psycopg"
    extra_conn_args = {"client_encoding": "utf8", "application_name": "pygeoapi"}

    def __init__(self, provider_def):
        self.properties = provider_def.get("properties", {})

        # Bypass PostgreSQLProvider.__init__, which only exists to set the driver.
        GenericSQLProvider.__init__(self, provider_def, self.driver_name, self.extra_conn_args)

        self._fields = provider_def.get("field_constraints", {})

    def get_fields(self):
        """
        Return fields (columns) from PostgreSQL table

        :returns: dict of fields
        """
        return self._fields
