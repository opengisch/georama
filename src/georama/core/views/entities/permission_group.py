from django.contrib.auth.models import Group

from georama.core.views.entities.permission_principal import GeoramaPrincipalListView


class GeoramaGroupListView(GeoramaPrincipalListView):
    model = Group
    template_name = "core/group.html"

    def get_queryset(self):
        return self.model.objects.exclude(
            permissions__codename__icontains=str(self.kwargs.get("pk"))
        )
