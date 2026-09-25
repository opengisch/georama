from django.core.exceptions import ImproperlyConfigured
from django.db import models
from guardian.shortcuts import get_objects_for_user

from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models.organisation import Organisation


class OrganisationalManager(models.Manager.from_queryset(OrganisationalQuerySet)):
    """
    Manager to be used in context of models bound to organisations to easy handling
    of those.
    """

    def get_queryset(self) -> OrganisationalQuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        qs = super().get_queryset()
        self.validate_organisational(qs.model)
        return qs.prefetch_related(qs.get_model_organisation_field())

    def organisation_objects(self, organisation: Organisation | None) -> OrganisationalQuerySet:
        """Filters for objects bound to passed organisation. Organisation `None`
        means the _global_ organisation.

        Returns:
            the filtered QuerySet
        """
        return self.get_queryset().organisation_objects(organisation)

    @staticmethod
    def validate_organisational(model: models.Model):
        """
        Checks if a model can be considered "organisational"

        Args:
            model: The django orm model which must have a
                georama.core.common.managers.OrganisationalManager bound as default manager
                and the attribute ORGANISATION_FIELD_NAME defined.
        Returns:
            True if conditions are met.
        Raises:
            ImproperlyConfigured: if the model is not considered "organisational".
        """
        if isinstance(model.objects, OrganisationalManager) and hasattr(
            model, "ORGANISATION_FIELD_NAME"
        ):
            return True
        else:
            raise ImproperlyConfigured(
                "An OrganisationalModelAdmin has to be configured with models bound to"
                "an Organisational georama.core.common.managers.OrganisationalManager"
            )


class LayerManager(OrganisationalManager):
    def get_public_or_permitted(self, organisation: Organisation, user, perms):
        qs = self.get_queryset().organisation_objects(organisation)
        return get_objects_for_user(user, perms, qs) | qs.filter(public=True)

    def accessible_layers(
        self,
        organisation: Organisation,
        user,
        perms: list[str],
        layer_names: list[str] | None = None,
    ) -> OrganisationalQuerySet:
        qs = self.get_queryset().organisation_objects(organisation)
        if layer_names is None:
            # most notably this is the case on capability requests
            return self.get_public_or_permitted(organisation, user, perms)

        # first check is about the layer names (raising if missmatch is found)
        qs = qs.filter(id__in=layer_names)
        found_difference = set(layer_names) - {layer.identifier for layer in qs}
        if len(found_difference) > 0:
            raise PermissionError(f"Layer(s) not found: {list(found_difference)}")

        # continue with the available list checking for permissions
        qs = self.get_public_or_permitted(organisation, user, perms)
        accessible_layers = {}
        for layer in qs:
            accessible_layers[layer.identifier] = layer
        permission_difference = set(layer_names) - set(accessible_layers)
        if len(permission_difference) > 0:
            raise PermissionError(f"Layer(s) not permitted: {list(permission_difference)}")
        return qs
