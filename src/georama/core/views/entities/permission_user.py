from django.contrib.auth.models import User

from georama.core.views.entities.permission_principal import GeoramaPrincipalListView


class GeoramaUserListView(GeoramaPrincipalListView):
    model = User
    template_name = "core/user.html"

    def get_queryset(self):
        return (
            self.model.objects.exclude(
                user_permissions__codename__icontains=str(self.kwargs.get("pk"))
            )
            .exclude(pk=None)
            .filter(is_superuser=False)
        )
