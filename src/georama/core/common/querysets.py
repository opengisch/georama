import logging

from django.db import models

from georama.core.models.organisation import Organisation


class OrganisationalQuerySet(models.QuerySet):
    def get_model_organisation_field(self):
        return self.model.ORGANISATION_FIELD_NAME

    def assemble_organisational_filter_field_name(self):
        return f"{self.get_model_organisation_field()}__domain"

    def organisation_objects(self, organisation: Organisation | None):
        filter_kwarg = self.assemble_organisational_filter_field_name()
        if organisation is None:
            filter_kwarg = f"{filter_kwarg}__isnull"
            filter_value = True
        else:
            filter_value = organisation.domain
        filter_kwargs = {filter_kwarg: filter_value}
        logging.debug(f"Applied organisational filter kwargs: {filter_kwargs}")
        return self.filter(**filter_kwargs)
