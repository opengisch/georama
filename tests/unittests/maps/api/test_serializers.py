import pytest
from asgiref.sync import async_to_sync

from georama.integration.factories import DatasourceFactory
from georama.maps.api.serializers import WmsLayerSerializer
from georama.maps.models import Metadata, WmsLayer


@pytest.mark.django_db
class TestWmsLayerSerializer:
    def test_aupdate_wmslayer_with_nested_metadata(self):
        wms_layer = WmsLayer.objects.create(
            datasource=DatasourceFactory(),
            metadata=Metadata.objects.create(),
        )

        async def run():
            serializer = WmsLayerSerializer(
                wms_layer,
                data={"metadata": {"title": "A New Title"}},
                partial=True,
            )
            assert serializer.is_valid(raise_exception=True)
            await serializer.asave()

        async_to_sync(run)()
        wms_layer.metadata.refresh_from_db()
        assert wms_layer.metadata.title == "A New Title"
