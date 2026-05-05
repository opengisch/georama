from typing import Literal

from django.apps import apps
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.core.menu import BreadCrumb
from georama.core.views.entities.published_item_detail import GeoramaPublishedItemDetail
from georama.core.views.entities.published_item_list import GeoramaPublishedItemList
from georama.core.views.generic.mixins import (
    BreadcrumbMixin,
    PermissionRequiredMixin,
)
from georama.processes.apps import central_app_label
from georama.processes.interface.ogc_api.v_100.processes import (
    Conformance,
    Landing,
    Link,
    Processes,
)
from georama.processes.models import Job, PublishedAsProcess


class TemplateOrApiView(PermissionRequiredMixin, BreadcrumbMixin, TemplateView):
    permission_required = []

    def render_to_json(self, context, **json_kwargs):
        raise NotImplementedError()

    def get_output_format(self) -> Literal["html", "json"]:
        param_preferred_type = self.request.GET.get("f")
        header_preferred_type = self.request.get_preferred_type(
            [
                "text/html",
                "application/json",
            ]
        )
        if param_preferred_type is not None:
            if param_preferred_type == "html":
                return "html"
            if param_preferred_type == "json":
                return "json"
        if header_preferred_type == "text/html":
            return "html"
        if header_preferred_type == "application/json":
            return "json"

    def render(self, context):
        output_format = self.get_output_format()
        if output_format == "html":
            return self.render_to_response(context)
        if output_format == "json":
            return self.render_to_json(context)
        return JsonResponse({"detail": "Unsupported media type"}, status=406)

    def get(self, request: HttpRequest, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render(context)


class TemplateOrApiListView(TemplateOrApiView, GeoramaPublishedItemList):
    permission_required = []

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        return self.render(context)


class TemplateOrApiDetailView(TemplateOrApiView, GeoramaPublishedItemDetail):
    permission_required = []

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, **kwargs)
        return self.render(context)


class LandingView(TemplateOrApiView):
    template_name = "processes/api/landing.html"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = Landing(
            title="Georama OGC API Processes",
            description="...",
            links=[
                Link(
                    type="application/json",
                    rel="self",
                    href=self.request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-landing")
                    )
                    + "?f=json",
                    href_lang="en",
                    title=_("This document as JSON"),
                ),
                Link(
                    type="text/html",
                    rel="self",
                    href=self.request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-landing")
                    )
                    + "?f=html",
                    href_lang="en",
                    title=_("This document as HTML"),
                ),
                Link(
                    type="application/json",
                    rel="conformance",
                    href=self.request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-conformance")
                    ),
                    href_lang="en",
                    title=_("Conformance"),
                ),
                Link(
                    type="application/json",
                    rel="http://www.opengis.net/def/rel/ogc/1.0/processes",
                    href=self.request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-process-list")
                    ),
                    href_lang="en",
                    title=_("Process list"),
                ),
                Link(
                    type="application/json",
                    rel="http://www.opengis.net/def/rel/ogc/1.0/job-list",
                    href=self.request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-job-list")
                    ),
                    href_lang="en",
                    title=_("Jobs list"),
                ),
            ],
        )
        return context

    def render_to_json(self, context, **json_kwargs):
        return HttpResponse(
            JsonSerializer().render(context["object"]), content_type="application/json"
        )


class ConformanceView(TemplateOrApiView):
    template_name = "processes/api/conformance.html"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Conformance"),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = Conformance(
            conforms_to=[
                "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core",
                "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description",
                "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json",
            ]
        )
        return context

    def render_to_json(self, context, **json_kwargs):
        return HttpResponse(
            JsonSerializer().render(context["object"]), content_type="application/json"
        )


class ProcessListView(TemplateOrApiListView):
    model = PublishedAsProcess
    template_name = "processes/api/process_list.html"
    entity_name = "process"
    permission_required = model.perm_view()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model._meta.app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Process list"),
        ]

    def render_to_json(self, context, **json_kwargs):
        processes = Processes(
            processes=[process.dataclass for process in self.object_list],
            links=[],
        )
        return HttpResponse(
            JsonSerializer().render(processes), content_type="application/json"
        )


class ProcessDetailView(TemplateOrApiDetailView):
    model = PublishedAsProcess
    entity_name = "process"
    template_name = "processes/api/process_detail.html"

    slug_url_kwarg = "process_id"
    slug_field = "process_id"

    permission_required = model.perm_view()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Process list", reverse(f"{app_menu.app_label}:api-process-list")),
            BreadCrumb(self.object.title),
        ]

    def render_to_json(self, context, **json_kwargs):
        process = self.object.dataclass
        return HttpResponse(JsonSerializer().render(process), content_type="application/json")


class ProcessExectionView(TemplateOrApiView):
    entity_name = "proces"

    def post(self, request: HttpRequest):
        pass

    def get(self, request: HttpRequest):
        pass


class JobListView(TemplateOrApiListView):
    entity_name = "job"
    model = Job

    def render_to_json(self, context, **json_kwargs):
        return HttpResponse(
            JsonSerializer().render(context["object_list"]), content_type="application/json"
        )


class JobDetailView(TemplateOrApiDetailView):
    entity_name = "job"
    model = Job

    def render_to_json(self, context, **json_kwargs):
        return HttpResponse(
            JsonSerializer().render(context["object_list"]), content_type="application/json"
        )
