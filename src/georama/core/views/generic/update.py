from django.views.generic.edit import UpdateView

from georama.core.views.generic.mixins import BreadcrumbMixin


class GeoramaUpdateView(BreadcrumbMixin, UpdateView):
    template_name = "core/form.html"
