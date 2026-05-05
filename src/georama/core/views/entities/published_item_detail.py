from django.apps import apps
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.views.generic.detail import DetailView


class GeoramaPublishedItemDetail(DetailView):
    """
    This view is the apps landing page. It shows the available published
    layers a user can access. This is also available in public and shows
    layers which are public too. However, the important part is, that we
    use the Georama inherent ObjectPermissionSystem `PublishedAs` here.
    Not the Django model permission system.
    """

    model: PublishedAs
    template_name = "core/published_item_detail.html"
    entity_name: str

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model._meta.app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
            BreadCrumb(self.object.title or self.object.name),
        ]

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.has_general_permission(self.request.user, self.model._meta.app_label):
            return obj
        raise PermissionDenied()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (
            self.request.user.has_perm(self.model.perm_view())
            or self.request.user.has_perm(self.model.perm_change())
            or self.request.user.has_perm(self.model.perm_delete())
            or self.request.user.has_perm(self.model.perm_add())
            or self.request.user.has_perm(self.model.perm_manage_permissions())
        ):
            context["breadcrumb_action_url"] = (
                f"{self.model._meta.app_label}:{self.entity_name}-list"
            )
            context["breadcrumb_action_icon"] = "fa fa-wrench"
            context["breadcrumb_action_title"] = _("Manage")
            context["breadcrumb_action_tooltip"] = _("Manage and publish items")

        return context
