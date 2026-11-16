from uuid import UUID

import pytest

from georama.webgis.models import WmsLayer
from georama.webgis.views.pygeoapi import PygeoapiServerWebGIS


class TestCollectionIds:
    """The webgis mount serves a WMS layer under the name GeoGirafe knows it from the WMS,
    the layer identifier prefixed so it is a valid NCName.
    """

    def test_collection_key(self):
        layer = WmsLayer(id=UUID("1ddbab8a-3a1f-4c3e-9d7e-6f1d2c3b4a59"))
        key = PygeoapiServerWebGIS().collection_key(layer)
        assert key == "_1ddbab8a-3a1f-4c3e-9d7e-6f1d2c3b4a59"

    @pytest.mark.parametrize(
        "collection_id",
        [
            # the name the mount serves the collection with
            "_1ddbab8a-3a1f-4c3e-9d7e-6f1d2c3b4a59",
            # the plain identifier is understood as well
            "1ddbab8a-3a1f-4c3e-9d7e-6f1d2c3b4a59",
        ],
    )
    def test_collection_identifier(self, collection_id):
        identifier = PygeoapiServerWebGIS().collection_identifier(collection_id)
        assert identifier == "1ddbab8a-3a1f-4c3e-9d7e-6f1d2c3b4a59"
