from django.core.exceptions import ImproperlyConfigured
from django.db import models
from guardian.shortcuts import get_objects_for_user

from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models.organisation import Organisation


class OrganisationalManager(models.Manager.from_queryset(OrganisationalQuerySet)):
    """Manager to be used in context of models bound to organisations to easy handling
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
        """Checks if a model can be considered "organisational".

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


class PublicOrProtectedManager(OrganisationalManager):
    def get_public_or_permitted(
        self, organisation: Organisation, user, perms
    ) -> OrganisationalQuerySet:
        qs = self.get_queryset().organisation_objects(organisation)
        return get_objects_for_user(user, perms, qs) | qs.filter(public=True)

    def get_permitted(self, organisation: Organisation, user, perms) -> OrganisationalQuerySet:
        qs = self.get_queryset().organisation_objects(organisation)
        return get_objects_for_user(user, perms, qs)

    def accessible_objects(
        self,
        organisation: Organisation,
        user,
        perms: list[str],
        object_ids: list[str] | None = None,
        include_public: bool = False,
    ) -> OrganisationalQuerySet:
        perm_qs = self.get_public_or_permitted if include_public else self.get_permitted
        if object_ids is None:
            # most notably this is the case on capability requests
            return perm_qs(organisation, user, perms)

        # first check is about the object names (raising if missmatch is found)
        qs = self.get_queryset().organisation_objects(organisation).filter(id__in=object_ids)
        found_difference = set(object_ids) - {obj.identifier for obj in qs}
        if len(found_difference) > 0:
            raise qs.model.DoesNotExist(
                f"{qs.model._meta.verbose_name}(s) not found: {list(found_difference)}"
            )

        # continue with the available list checking for permissions
        qs = perm_qs(organisation, user, perms).filter(id__in=object_ids)
        accessible_objects = {obj.identifier: obj for obj in qs}
        permission_difference = set(object_ids) - set(accessible_objects)
        if len(permission_difference) > 0:
            raise PermissionError(
                f"{qs.model._meta.verbose_name}(s) not permitted: {list(permission_difference)}"
            )
        return qs
