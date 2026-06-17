from django.conf import settings
from django.template.response import TemplateResponse
from django.views import generic


class Index(generic.TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        site_title = getattr(settings, "SITE_TITLE", None)
        if not site_title:
            site_title = request.get_host()
        return TemplateResponse(
            request,
            context={
                "site_title": site_title,
                "breadcrumbs": [],
            },
            template="core/index.html",
        )
