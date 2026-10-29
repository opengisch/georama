from uuid import uuid4

import pytest
from django.contrib.auth.models import AnonymousUser

from georama.maps.models import WmsLayer


class TestLayerManager:
    """common logic is tested against the WmsLayer model of the maps app."""

    @pytest.mark.django_db
    def test_get_permitted_with_anonymous_has_no_access(self, global_wms_layer_public_queryable):
        assert (
            WmsLayer.objects.get_permitted(
                None, AnonymousUser, ["view_published_wms_layer"]
            ).count()
            == 0
        )

    @pytest.mark.django_db
    def test_get_permitted_with_permitted_user_has_access(
        self,
        global_wms_layer_non_public_queryable,
        user_with_membership_global_wms_layer_permission,
    ):
        assert (
            WmsLayer.objects.get_permitted(
                None, user_with_membership_global_wms_layer_permission, ["view_published_wms_layer"]
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_get_permitted_with_permitted_user_but_wrong_org_has_no_access(
        self,
        global_wms_layer_non_public_queryable,
        user_with_membership_global_wms_layer_permission,
        organisation_non_public_access,
    ):
        assert (
            WmsLayer.objects.get_permitted(
                organisation_non_public_access,
                user_with_membership_global_wms_layer_permission,
                ["view_published_wms_layer"],
            ).count()
            == 0
        )

    @pytest.mark.django_db
    def test_get_public_or_permitted_with_anonymous_has_access_on_public(
        self, global_wms_layer_public_queryable
    ):
        assert (
            WmsLayer.objects.get_public_or_permitted(
                None, AnonymousUser, ["view_published_wms_layer"]
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_get_public_or_permitted_with_anonymous_has_no_access_on_nonpublic(
        self, global_wms_layer_non_public_queryable
    ):
        assert (
            WmsLayer.objects.get_public_or_permitted(
                None, AnonymousUser, ["view_published_wms_layer"]
            ).count()
            == 0
        )

    @pytest.mark.django_db
    def test_get_public_or_permitted_with_permitted_user_but_wrong_org_has_no_access(
        self,
        global_wms_layer_non_public_queryable,
        user_with_membership_global_wms_layer_permission,
        organisation_non_public_access,
    ):
        assert (
            WmsLayer.objects.get_public_or_permitted(
                organisation_non_public_access,
                user_with_membership_global_wms_layer_permission,
                ["view_published_wms_layer"],
            ).count()
            == 0
        )

    @pytest.mark.django_db
    def test_get_public_or_permitted_with_permitted_user_has_access(
        self,
        global_wms_layer_non_public_queryable,
        user_with_membership_global_wms_layer_permission,
    ):
        assert (
            WmsLayer.objects.get_public_or_permitted(
                None, user_with_membership_global_wms_layer_permission, ["view_published_wms_layer"]
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_accessible_layers_does_not_evaluate_public(self, global_wms_layer_public_queryable):
        assert (
            WmsLayer.objects.accessible_layers(
                None, AnonymousUser, ["view_published_wms_layer"], include_public=False
            ).count()
            == 0
        )

    @pytest.mark.django_db
    def test_accessible_layers_evaluate_public(self, global_wms_layer_public_queryable):
        assert (
            WmsLayer.objects.accessible_layers(
                None, AnonymousUser, ["view_published_wms_layer"], include_public=True
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_accessible_layers_return_all_if_no_layer_ids(
        self, global_wms_layer_public_queryable, global_wms_layer_public_non_queryable
    ):
        assert (
            WmsLayer.objects.accessible_layers(
                None, AnonymousUser, ["view_published_wms_layer"], include_public=True
            ).count()
            == 2
        )

    @pytest.mark.django_db
    def test_accessible_layers_raises_not_found_on_wrong_id(
        self, global_wms_layer_public_queryable, global_wms_layer_public_non_queryable
    ):
        with pytest.raises(WmsLayer.DoesNotExist) as _:
            assert WmsLayer.objects.accessible_layers(
                None,
                AnonymousUser,
                ["view_published_wms_layer"],
                layer_ids=[str(uuid4())],
                include_public=True,
            )

    @pytest.mark.django_db
    def test_accessible_layers_raises_not_found_on_partially_matching_id_list(
        self, global_wms_layer_public_queryable, global_wms_layer_public_non_queryable
    ):
        with pytest.raises(WmsLayer.DoesNotExist) as _:
            WmsLayer.objects.accessible_layers(
                None,
                AnonymousUser,
                ["view_published_wms_layer"],
                layer_ids=[str(uuid4()), global_wms_layer_public_queryable.id],
                include_public=True,
            )

    @pytest.mark.django_db
    def test_accessible_layers_returns_the_layer_matched_by_id(
        self, global_wms_layer_public_queryable, global_wms_layer_non_public_queryable
    ):
        assert WmsLayer.objects.count() == 2
        assert (
            WmsLayer.objects.accessible_layers(
                None,
                AnonymousUser,
                ["view_published_wms_layer"],
                layer_ids=[str(global_wms_layer_public_queryable.id)],
                include_public=True,
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_accessible_layers_raises_permission_error_on_not_permitted_layer(
        self, global_wms_layer_public_queryable, global_wms_layer_non_public_queryable
    ):
        with pytest.raises(PermissionError):
            WmsLayer.objects.accessible_layers(
                None,
                AnonymousUser,
                ["view_published_wms_layer"],
                layer_ids=[str(global_wms_layer_non_public_queryable.id)],
                include_public=True,
            )

    @pytest.mark.django_db
    def test_accessible_layers_permitted_user_gets_requested(
        self,
        global_wms_layer_non_public_queryable,
        global_wms_layer_public_queryable,
        global_wms_layer_public_non_queryable,
        user_with_membership_global_wms_layer_permission,
    ):
        assert (
            WmsLayer.objects.accessible_layers(
                None,
                user_with_membership_global_wms_layer_permission,
                ["view_published_wms_layer"],
                layer_ids=[
                    str(global_wms_layer_non_public_queryable.id),
                    str(global_wms_layer_public_queryable.id),
                    str(global_wms_layer_public_non_queryable.id),
                ],
                include_public=True,
            ).count()
            == 3
        )
        assert (
            WmsLayer.objects.accessible_layers(
                None,
                user_with_membership_global_wms_layer_permission,
                ["view_published_wms_layer"],
                layer_ids=[
                    str(global_wms_layer_non_public_queryable.id),
                    str(global_wms_layer_public_non_queryable.id),
                ],
                include_public=True,
            ).count()
            == 2
        )
        assert (
            WmsLayer.objects.accessible_layers(
                None,
                user_with_membership_global_wms_layer_permission,
                ["view_published_wms_layer"],
                layer_ids=[
                    str(global_wms_layer_public_non_queryable.id),
                ],
                include_public=True,
            ).count()
            == 1
        )

    @pytest.mark.django_db
    def test_accessible_layers_raises_for_permitted_user_on_unknown_layer_id(
        self,
        global_wms_layer_non_public_queryable,
        global_wms_layer_public_queryable,
        global_wms_layer_public_non_queryable,
        user_with_membership_global_wms_layer_permission,
    ):
        with pytest.raises(WmsLayer.DoesNotExist):
            WmsLayer.objects.accessible_layers(
                None,
                user_with_membership_global_wms_layer_permission,
                ["view_published_wms_layer"],
                layer_ids=[
                    str(uuid4()),
                ],
                include_public=True,
            )
