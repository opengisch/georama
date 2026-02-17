from django.contrib.admin.utils import NestedObjects
from django.db import router
from django.views.generic.edit import DeleteView

from georama.core.views.generic.mixins import BreadcrumbMixin


class GeoramaDeleteView(BreadcrumbMixin, DeleteView):
    template_name = "core/delete_preview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        using = router.db_for_write(self.object.__class__)
        collector = NestedObjects(using=using)
        collector.collect([self.object])
        context["related_objects"] = collector.nested()
        context["protected"] = collector.protected
        return context
