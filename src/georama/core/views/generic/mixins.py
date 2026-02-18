from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


class BreadcrumbMixin:
    breadcrumbs = []

    def get_breadcrumbs(self):
        return self.breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = self.get_breadcrumbs()
        return context


class GeoramaLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")


class GeoramaAnyPermissionRequiredMixin(PermissionRequiredMixin):
    """
    Allows access if user has at least one of the allowed permissions.
    Implements OR check instead of the normal AND check.
    """

    def has_permission(self):
        perms = self.get_permission_required()
        return any(self.request.user.has_perm(p) for p in perms)
