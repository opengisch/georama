import pytest
from django.contrib.auth.models import AnonymousUser

from georama.maps.models import WmsLayer
from georama.maps.services.wms_1_3_0 import WmsOperation


class TestWmsOperationGeometryless:
    """Geometryless layers have no map, the WMS does not know them."""

    @pytest.fixture
    def wms_operation(self):
        yield WmsOperation(
            appname="maps",
            url="http://localhost/maps/ows",
            user=AnonymousUser(),
            model=WmsLayer,
            organisation=None,
            perms=["view_published_wms_layer"],
        )

    @pytest.mark.django_db
    def test_capabilities_leave_geometryless_layers_out(
        self,
        wms_operation,
        global_wms_layer_public_queryable,
        global_wms_layer_public_queryable_geometryless,
    ):
        assert wms_operation.obtain_accessible_layers() == [global_wms_layer_public_queryable]

    @pytest.mark.django_db
    def test_requesting_a_geometryless_layer_is_unknown(
        self, wms_operation, global_wms_layer_public_queryable_geometryless
    ):
        layer_name = WmsOperation.encode_layer_name(
            global_wms_layer_public_queryable_geometryless.identifier
        )
        with pytest.raises(WmsLayer.DoesNotExist):
            wms_operation.obtain_accessible_layers([layer_name])
