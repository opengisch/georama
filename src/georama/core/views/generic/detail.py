from django.views.generic import DetailView

from georama.core.views.generic.mixins import BreadcrumbMixin


class GeoramaDetailView(BreadcrumbMixin, DetailView):
    template_name = "core/detail.html"
