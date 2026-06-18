from unfold.admin import ModelAdmin


class OrganisationalModelAdmin(ModelAdmin):
    """
    Model admin which shows full content to admin users but content filtered by
    organisation to staff users.

    Attributes:
        prefetch_organisation_related: The name of the organisation field. `organisation`
            if there is a direct relation, if there is a tree like relation like
            `organisation=>collection=>project` then the value should be:
            `'organisation__collection__project'`
    """

    prefetch_organisation_related: str

    def get_queryset(self, request):
        qs = super().get_queryset(request).prefetch_related(self.prefetch_organisation_related)
        if request.user.is_superuser:
            return qs
        return qs.filter(**{self.prefetch_organisation_related: request.georama_organisation})
