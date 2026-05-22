from django.urls import reverse
from django.utils.translation import gettext as _


class BreadCrumbAction:
    def get_breadcrumb_action_context(self) -> dict:
        action_context = {}
        if (
            self.request.user.has_perm(self.model.perm_view())
            or self.request.user.has_perm(self.model.perm_change())
            or self.request.user.has_perm(self.model.perm_delete())
            or self.request.user.has_perm(self.model.perm_add())
            or self.request.user.has_perm(self.model.perm_manage_permissions())
        ):
            action_context["breadcrumb_action_url"] = reverse(
                f"{self.model._meta.app_label}:{self.entity_name}-list"
            )
            action_context["breadcrumb_action_icon"] = "fa fa-wrench"
            action_context["breadcrumb_action_title"] = _("Manage")
            action_context["breadcrumb_action_tooltip"] = _("Manage and publish items")
        return action_context
