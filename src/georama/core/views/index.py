from django.conf import settings
from django.template.response import TemplateResponse
from django.views import generic


class Index(generic.TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request,
            context={
                "breadcrumbs": [],
                "webgis_url": settings.WEBGISURL,
            },
            template="core/index.html",
        )
