from pygeoapi.provider.ogr import OGRProvider
from copy import deepcopy


class GeoramaOgcProvider(OGRProvider):
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

    def _ogr_feature_to_json(
        self,
        ogr_feature,
        skip_geometry=False,
        crs_transform_out=None,
    ):
        """
        Overwrite to filter out non-defined properties. Can be removed in
        pygeoapi 0.21.
        """
        json_feature = super()._ogr_feature_to_json(
            ogr_feature, skip_geometry, crs_transform_out
        )

        # Drop non-defined properties
        if self.properties:
            props = json_feature["properties"]
            dropping_keys = deepcopy(props).keys()
            for item in dropping_keys:
                if item not in self.properties:
                    props.pop(item)

        return json_feature
