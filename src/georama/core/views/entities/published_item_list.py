from django.apps import apps

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.views.entities.mixins import BreadCrumbAction
from georama.core.views.generic.list import GeoramaListView


class GeoramaPublishedItemList(BreadCrumbAction, GeoramaListView):
    """
    This view is the apps landing page. It shows the available published
    layers a user can access. This is also available in public and shows
    layers which are public too. However, the important part is, that we
    use the Georama inherent ObjectPermissionSystem `PublishedAs` here.
    Not the Django model permission system.
    """

    model: PublishedAs
    template_name = "core/published_item_list.html"
    entity_name: str

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model._meta.app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
        ]

    def get_queryset(self):
        permitted_items = []
        # TODO: We should prefilter here, since we know the list of permissions a user
        #   has
        items = self.model.objects.all()
        for item in items:
            if item.has_general_permission(self.request.user, self.model._meta.app_label):
                permitted_items.append(item)
        return permitted_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_breadcrumb_action_context())
        return context
