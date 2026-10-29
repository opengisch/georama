import pytest
from django.contrib.auth.models import AnonymousUser

from georama.maps.models import WmsLayer


class TestWmsLayerManager:
    @pytest.mark.django_db
    def test_accessible_layers_queryable_with_anonymous_on_queryable_layer_allowed(
        self, global_wms_layer_public_queryable
    ):
        assert (
            WmsLayer.objects.accessible_layers_queryable(
                None, AnonymousUser, ["view_published_wms_layer"]
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_accessible_layers_queryable_with_anonymous_non_queryable_layer_denied(
        self, global_wms_layer_public_non_queryable
    ):
        assert (
            WmsLayer.objects.accessible_layers_queryable(
                None, AnonymousUser, ["view_published_wms_layer"]
            ).count()
            == 0
        )
