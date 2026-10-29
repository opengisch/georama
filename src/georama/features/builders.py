"""Content builders shared by the content commands and the test fixtures."""

from georama.features.factories import FeatureLayerFactory, MetadataFactory
from georama.features.models import FeatureLayer
from georama.integration.models import Vector

TEST_FEATURE_LAYER_ID = "c42684cc-9731-453e-8faa-e9b400e69c1d"


def create_test_feature_layer(vector: Vector) -> FeatureLayer:
    """The public feature layer of the TestMandant point vector."""
    return FeatureLayerFactory.create(
        id=TEST_FEATURE_LAYER_ID,
        datasource=vector,
        public=True,
        metadata=MetadataFactory(title="TestFeatureLayer"),
    )
