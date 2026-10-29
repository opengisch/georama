"""Content builders shared by the content commands and the test fixtures."""

from georama.integration.models import Vector
from georama.maps.factories import MetadataFactory, WmsLayerFactory
from georama.maps.models.wms_layer import WmsLayer

TEST_WMS_LAYER_ID = "09b56f4c-e0b7-432d-b99e-48a692d12ea4"


def create_test_wms_layer(vector: Vector) -> WmsLayer:
    """The public and queryable WMS layer of the TestMandant point vector."""
    return WmsLayerFactory.create(
        id=TEST_WMS_LAYER_ID,
        datasource=vector,
        public=True,
        queryable=True,
        metadata=MetadataFactory(title="TestWmsLayer"),
    )
