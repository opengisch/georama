from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.templatetags.static import static
from django.urls import reverse
from django.views import View

from georama.core.menu import MenuItem
from georama.core.services import Service


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
                "maps_endpoint": request.build_absolute_uri(reverse("maps_ogc_entry")),
            },
            template="core/home.html",
        )


class Login(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing")
        else:
            return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


class ChangeListView(View):
    service: type[Service]
    title: str
    template: str = "core/change_list.html"
    app_menu: MenuItem

    def get(self, request: HttpRequest):
        service = self.service()
        context = {
            "app_menu": self.app_menu,
            "page_title": self.title,
            "items": service.get_list_page(
                int(request.GET.get("offset", 0)),
                int(request.GET.get("count", settings.LIST_PAGE_SIZES[0])),
            ),
            "current_offset": int(request.GET.get("offset", 0)),
            "default_count": settings.LIST_PAGE_SIZES[0],
            "current_count": int(request.GET.get("count", settings.LIST_PAGE_SIZES[0])),
            "available_counts": settings.LIST_PAGE_SIZES,
            "pages": service.pages_list(
                int(request.GET.get("count", settings.LIST_PAGE_SIZES[0]))
            ),
            "current_page": int(request.GET.get("page", 1)),
            "next_page": int(request.GET.get("page", 1)) + 1,
            "next_page_offset": (int(request.GET.get("page", 1)) + 1)
            * int(request.GET.get("count", settings.LIST_PAGE_SIZES[0]))
            - 1,
            "prev_page": int(request.GET.get("page", 1)) - 1,
            "prev_page_offset": (int(request.GET.get("page", 1)) - 1)
            * int(request.GET.get("count", settings.LIST_PAGE_SIZES[0]))
            - 1,
        }
        return render(request, self.template, context)
