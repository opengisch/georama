from django.conf import settings
from django.template.response import TemplateResponse
from django.templatetags.static import static
from django.urls import reverse
from django.views import View


class GeoramaLanding(View):
    def get(self, request, *args, **kwargs):
        logo_url = static("/core/assets/images/georama.coming_soon.png")
        site_title = getattr(settings, "SITE_TITLE", None)
        if not site_title:
            site_title = request.get_host()
        return TemplateResponse(
            request,
            context={
                "logo_url": logo_url,
                "geogirafe_url": settings.WEBGISURL,
                "site_title": site_title,
                "maps_endpoint": request.build_absolute_uri(reverse("maps:maps_ogc_entry")),
                "breadcrumbs": [],
            },
            template="core/home.html",
        )
