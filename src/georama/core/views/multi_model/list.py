from abc import ABC

from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from georama.core.menu import BreadCrumb, MenuItem
from georama.core.services.multi_model.base import Service


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
    breadcrumb_action_icon: str = None
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
                int(request.GET.get("count", settings.LIST_PAGE_SIZE_DEFAULT)),
            ),
            "absolute_count": service.count(),
            "current_offset": int(request.GET.get("offset", 0)),
            "default_count": settings.LIST_PAGE_SIZE_DEFAULT,
            "current_count": int(request.GET.get("count", settings.LIST_PAGE_SIZE_DEFAULT)),
            "available_counts": settings.LIST_PAGE_SIZES,
            "pages": service.pages_list(
                int(request.GET.get("count", settings.LIST_PAGE_SIZE_DEFAULT))
            ),
            "current_page": int(request.GET.get("page", 1)),
            "next_page": int(request.GET.get("page", 1)) + 1,
            "next_page_offset": (int(request.GET.get("page", 1)) + 1)
            * int(request.GET.get("count", settings.LIST_PAGE_SIZE_DEFAULT))
            - 1,
            "prev_page": int(request.GET.get("page", 1)) - 1,
            "prev_page_offset": (int(request.GET.get("page", 1)) - 1)
            * int(request.GET.get("count", settings.LIST_PAGE_SIZE_DEFAULT))
            - 1,
            "breadcrumb_action_url": self.breadcrumb_action_url,
            "breadcrumb_action_icon": self.breadcrumb_action_icon,
            "breadcrumb_action_title": self.breadcrumb_action_title,
        }
        context.update(self.extra_context(context, service))
        return render(request, self.template, context)
