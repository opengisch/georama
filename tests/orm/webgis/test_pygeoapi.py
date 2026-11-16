import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from guardian.core import ObjectPermissionChecker
from guardian.shortcuts import assign_perm

from georama.webgis.factories import MetadataFactory, WmsLayerFactory
from georama.webgis.models import WmsLayer
from georama.webgis.views.pygeoapi import PygeoapiServerWebGIS


class TestWritePermissions:
    """Writing to a collection of the webgis mount is granted on the theme the layer
    belongs to, never by the theme being public.
    """

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "permission",
        [
            "webgis.create_objects_theme_vector_layer",
            "webgis.update_objects_theme_vector_layer",
            "webgis.delete_objects_theme_vector_layer",
        ],
    )
    def test_write_permission_on_the_theme(
        self, user_with_membership_global, global_webgis_wms_layer_non_public_theme, permission
    ):
        theme = global_webgis_wms_layer_non_public_theme.theme
        assign_perm("webgis.view_published_theme", user_with_membership_global, theme)
        assign_perm(permission, user_with_membership_global, theme)
        # the layer of the theme is writable for the user
        assert list(
            WmsLayer.objects.get_permitted(None, user_with_membership_global, [permission])
        ) == [global_webgis_wms_layer_non_public_theme]
        # and the collection is announced as editable
        permission_checker = ObjectPermissionChecker(user_with_membership_global)
        assert PygeoapiServerWebGIS().is_editable(
            global_webgis_wms_layer_non_public_theme, permission_checker
        )

    @pytest.mark.django_db
    def test_view_permission_does_not_allow_writing(
        self, user_with_membership_global, global_webgis_wms_layer_non_public_theme
    ):
        theme = global_webgis_wms_layer_non_public_theme.theme
        assign_perm("webgis.view_published_theme", user_with_membership_global, theme)
        assert not WmsLayer.objects.get_permitted(
            None, user_with_membership_global, ["webgis.create_objects_theme_vector_layer"]
        ).exists()
        permission_checker = ObjectPermissionChecker(user_with_membership_global)
        assert not PygeoapiServerWebGIS().is_editable(
            global_webgis_wms_layer_non_public_theme, permission_checker
        )

    @pytest.mark.django_db
    def test_public_theme_does_not_allow_writing(self, global_webgis_wms_layer_public_theme):
        # everybody sees the layer of a public theme
        assert WmsLayer.objects.get_public_or_permitted(
            None, AnonymousUser(), ["webgis.view_published_theme"]
        ).exists()
        # but nobody writes to it without permission
        assert not WmsLayer.objects.get_permitted(
            None, AnonymousUser(), ["webgis.create_objects_theme_vector_layer"]
        ).exists()


class TestGeometrylessCollections:
    """A geometryless datasource of a theme gets a WMS layer as well. It is not part of
    the map, but its collection is served on the webgis mount, e.g. as lookup table.
    """

    @pytest.mark.django_db
    def test_geometryless_layer_is_a_collection(
        self,
        global_geometryless_vector,
        global_webgis_theme_public,
        global_webgis_wms_layer_public_theme,
    ):
        geometryless_layer = WmsLayerFactory.create(
            queryable=True,
            datasource=global_geometryless_vector,
            metadata=MetadataFactory.create(title="Land use types"),
            theme=global_webgis_theme_public,
        )
        request = RequestFactory().get("/webgis/api/collections")
        request.user = AnonymousUser()
        request.georama_organisation = None
        server = PygeoapiServerWebGIS()
        server.request = request
        feature_layers = server.accessible_feature_layers(request)
        # the spatial and the geometryless layer of the public theme are collections
        assert {layer.id for layer in feature_layers} == {
            global_webgis_wms_layer_public_theme.id,
            geometryless_layer.id,
        }
