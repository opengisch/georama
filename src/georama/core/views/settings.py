from django.template.response import TemplateResponse
from django.views import View


class Settings(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request,
            context={},
            template="core/settings.html",
        )
