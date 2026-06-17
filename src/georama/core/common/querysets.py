from django.db import models

from georama.core.models.organisation import Organisation


class OrganisationalQuerySet(models.QuerySet):
    def organisation_objects(self, organisation: Organisation | None):
        if organisation is None:
            return self.filter(organisation__domain__isnull=True)
        return self.filter(organisation__domain=organisation.domain)
