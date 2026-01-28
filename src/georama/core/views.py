from abc import ABC

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission, User
from django.db import models
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.templatetags.static import static
from django.urls import reverse
from django.views import View

from georama.core.menu import BreadCrumb, MenuItem
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
                "maps_endpoint": request.build_absolute_uri(reverse("maps:maps_ogc_entry")),
                "breadcrumbs": [],
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


class ChangeListView(View, ABC):
    service: type[Service] = Service
    forms: list[ModelForm]
    title: str
    view_type_name: str = "change_list"
    name: str
    template: str = "core/change_list.html"
    app_menu: MenuItem
    breadcrumbs: list[BreadCrumb] = []
    breadcrumb_action_url: str = None
    breadcrumb_action_title: str = None
    list_actions: list[tuple[str, str]] = []

    def extra_context(self, context: dict, service: Service):
        return context

    def find_form_by_model(self, model: models.Model) -> ModelForm | None:
        for form in self.forms:
            if form._meta.model == model:
                return form
        return None

    def get(self, request: HttpRequest):
        service = self.service()
        context = {
            "view_name": f"{self.app_menu.app_label}:{self.name}",
            "app_menu": self.app_menu,
            "list_actions": self.list_actions,
            "breadcrumbs": self.breadcrumbs,
            "page_title": self.title,
            "items": service.get_list_page(
                int(request.GET.get("offset", 0)),
                int(request.GET.get("count", settings.LIST_PAGE_SIZES[0])),
            ),
            "absolute_count": service.count(),
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
            "breadcrumb_action_url": self.breadcrumb_action_url,
            "breadcrumb_action_title": self.breadcrumb_action_title,
        }
        context.update(self.extra_context(context, service))
        return render(request, self.template, context)


class Settings(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request,
            context={},
            template="core/settings.html",
        )


class FormView(View):
    service: type[Service] = Service
    forms: list[ModelForm] = []
    view_type_name: str = "form"
    name: str
    title: str
    template = "core/form.html"
    app_menu: MenuItem
    breadcrumbs: list[BreadCrumb] = []
    breadcrumb_action_url: str = None
    breadcrumb_action_title: str = None

    def extra_context(self, context: dict, service: Service):
        return context

    def get_form_by_db_object(self, instance):
        for form in self.forms:
            if form._meta.model == instance._meta.model:
                return form(instance=instance)
        return None

    def get_empty_forms(self):
        forms = []
        for form in self.forms:
            forms.append(form(instance=None))
        return forms

    def get(self, request, pk=None):
        service = self.service()
        if pk is None:
            forms = self.get_empty_forms()
            instance = None
        else:
            instance = service.get(pk=pk)[0]
            forms = [self.get_form_by_db_object(instance)]
        context = {
            "instance": instance,
            "forms": forms,
            "breadcrumbs": self.breadcrumbs,
            "breadcrumb_action_url": self.breadcrumb_action_url,
            "breadcrumb_action_title": self.breadcrumb_action_title,
        }
        context.update(self.extra_context(context, service))
        return render(request, self.template, context)


class AssignPermissionToUserOrGroup(View):

    def post(self, request: HttpRequest):
        principal_id = request.GET["principal_id"]
        permission_id = request.GET["permission_id"]
        principal_type = request.GET["principal_type"]
        permission = Permission.objects.filter(pk=permission_id).get()
        if principal_type == "user":
            user = User.objects.filter(pk=principal_id).get()
            user.user_permissions.add(permission)
            return HttpResponse("OK")
        elif principal_type == "group":
            group = Group.objects.filter(pk=principal_id).get()
            group.permissions.add(permission)
            return HttpResponse("OK")
        return HttpResponseBadRequest()


class RemovePermissionToUserOrGroup(View):

    def post(self, request: HttpRequest):
        principal_id = request.GET["principal_id"]
        permission_id = request.GET["permission_id"]
        principal_type = request.GET["principal_type"]
        permission = Permission.objects.filter(pk=permission_id).get()
        if principal_type == "user":
            user = User.objects.filter(pk=principal_id).get()
            user.user_permissions.remove(permission)
            return HttpResponse("OK")
        elif principal_type == "group":
            group = Group.objects.filter(pk=principal_id).get()
            group.permissions.remove(permission)
            return HttpResponse("OK")
        return HttpResponseBadRequest()
