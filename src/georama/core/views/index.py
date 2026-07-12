from django.template.response import TemplateResponse
from django.views import generic


class Index(generic.TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request,
            context={
                "breadcrumbs": [],
            },
            template="core/index.html",
        )
