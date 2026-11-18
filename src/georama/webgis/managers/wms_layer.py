from django.db import models
from guardian.shortcuts import get_objects_for_user

from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models import Organisation
from georama.maps.managers.wms_layer import WmsLayerManager as MapsWmsLayerManager


class WmsLayerManager(MapsWmsLayerManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return (
            super()
            .get_queryset()
            .prefetch_related(
                "metadata",
                "datasource",
                "theme",
                "datasource__vector",
                "datasource__raster",
                "datasource__custom",
            )
        )

    def get_public_or_permitted(
        self,
        organisation: Organisation,
        user,
        perms: list[str],
    ) -> OrganisationalQuerySet:
        # the permitted layers plus the ones of public themes
        return self.get_permitted(organisation, user, perms) | self.organisation_objects(
            organisation
        ).filter(theme__public=True)

    def get_permitted(
        self,
        organisation: Organisation,
        user,
        perms: list[str],
    ) -> OrganisationalQuerySet:
        # this is a special form of the normal wms layers, since the permission
        # of the layer is derived by the theme it belongs to. Writes only use this
        # one, they are never public.
        from georama.webgis.models.theme import Theme

        themes_qs = get_objects_for_user(
            user, perms, Theme.objects.organisation_objects(organisation)
        )
        return self.organisation_objects(organisation).filter(theme__in=themes_qs)
