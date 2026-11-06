import logging

from pygeoapi.provider.sql import PostgreSQLProvider
from sqlalchemy import true

LOGGER = logging.getLogger(__name__)


class GeoramaSqlProvider(PostgreSQLProvider):
    def __init__(self, provider_def):
        self.properties = provider_def.get("properties", {})

        super().__init__(provider_def)

        self._fields = provider_def.get("field_constraints", {})

    def _select_properties_clause(self, select_properties, skip_geometry):
        # geometryless tables have no geometry column to select
        return super()._select_properties_clause(
            select_properties, skip_geometry or self.geom is None
        )

    def _get_bbox_filter(self, bbox: list[float]):
        # without a geometry column the bbox cannot be applied, the items are not filtered
        if self.geom is None:
            return true()
        return super()._get_bbox_filter(bbox)

    def get_fields(self):
        """Return fields (columns) from PostgreSQL table.

        :returns: dict of fields
        """
        return self._fields
