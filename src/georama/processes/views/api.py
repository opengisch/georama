from django.apps import apps
from django.conf import settings
from django.core.paginator import Page
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
    Jobs,
    Landing,
    Link,
    Processes,
)
from georama.processes.models import Job, PublishedAsProcess


class TemplateOrApiView(PermissionRequiredMixin, BreadcrumbMixin, TemplateView):
    permission_required = []

    def render_to_json(self, context, **json_kwargs):
        raise NotImplementedError()

    def render(self, context):
        preferred_type = self.request.GET.get("f") or self.request.get_preferred_type(
            [
                "application/json",
                "text/html",
            ]
        )
        if preferred_type in {"html", "text/html"}:
            return self.render_to_response(context)
        if preferred_type in {"json", "application/json"}:
            return self.render_to_json(context)
        return JsonResponse({"detail": "Unsupported media type"}, status=406)

    def get(self, request: HttpRequest, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render(context)


class TemplateOrApiListView(TemplateOrApiView, GeoramaPublishedItemList):
    permission_required = []

    def setup(self, request, *args, **kwargs):
        # This is a hack: the templates and django pagination works with
        # `per_page` and `page` parameters but the OGC API requires `limit`
        # and `offset`. We convert the latter into the former here so that
        # we can keep using the pagination features without additional changes
        # TODO: catch errors
        limit = request.GET.get("limit")
        offset = request.GET.get("offset")
        if limit is not None:
            limit = int(limit)
            if limit not in settings.LIST_PAGE_SIZES:
                limit = settings.LIST_PAGE_SIZE_DEFAULT
            kwargs["per_page"] = limit
        if offset is not None:
            offset = int(offset)
            page = 1 if limit in (None, 0) else (offset // limit) + 1
            kwargs["page"] = page
        super().setup(request, *args, **kwargs)

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
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb("OGC API Processes"),
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
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb("OGC API Processes", reverse(f"{app_menu.app_label}:api-landing")),
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
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb("OGC API Processes", reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Process list"),
        ]

    def render_to_json(self, context, **json_kwargs):
        page: Page = context["page_obj"]
        per_page = context["per_page"]
        offset = (page.number - 1) * per_page
        links = [
            Link(
                rel="self",
                title="Processes (current page)",
                href=reverse(f"{central_app_label}:api-process-list")
                + f"?f=json&limit={per_page}&offset={offset}",
                type="application/json",
            ),
        ]
        if page.has_previous():
            offset = (page.previous_page_number() - 1) * per_page
            links.append(
                Link(
                    rel="prev",
                    title="Processes (previous page)",
                    href=reverse(f"{central_app_label}:api-process-list")
                    + f"?f=json&limit={per_page}&offset={offset}",
                    type="application/json",
                )
            )
        if page.has_next():
            offset = (page.next_page_number() - 1) * per_page
            links.append(
                Link(
                    rel="next",
                    title="Processes (next page)",
                    href=reverse(f"{central_app_label}:api-process-list")
                    + f"?f=json&limit={per_page}&offset={offset}",
                    type="application/json",
                )
            )
        processes = Processes(
            processes=[process.dataclass for process in self.object_list],
            links=links,
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
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb("OGC API Processes", reverse(f"{app_menu.app_label}:api-landing")),
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
    template_name = "processes/api/job_list.html"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb("OGC API Processes", reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Job list"),
        ]

    def render_to_json(self, context, **json_kwargs):
        jobs = Jobs(
            jobs=[job.dataclass for job in self.object_list],
            links=[],
        )
        return HttpResponse(JsonSerializer().render(jobs), content_type="application/json")


class JobDetailView(TemplateOrApiDetailView):
    entity_name = "job"
    model = Job
    template_name = "processes/api/job_detail.html"

    slug_url_kwarg = "job_id"
    slug_field = "job_id"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb("OGC API Processes", reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Job list", reverse(f"{app_menu.app_label}:api-job-list")),
            BreadCrumb(self.object.title),
        ]

    def render_to_json(self, context, **json_kwargs):
        job = self.object.dataclass
        return HttpResponse(JsonSerializer().render(job), content_type="application/json")


class JobResultView(TemplateOrApiDetailView):
    entity_name = "job"
    model = Job
    template_name = "processes/api/job_result.html"

    slug_url_kwarg = "job_id"
    slug_field = "job_id"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{self.model._meta.app_label}:index")),
            BreadCrumb("OGC API Processes", reverse(f"{app_menu.app_label}:api-landing")),
            BreadCrumb("Job list", reverse(f"{app_menu.app_label}:api-job-list")),
            BreadCrumb(
                self.object.title,
                reverse(
                    f"{app_menu.app_label}:api-job-detail",
                    kwargs={"job_id": self.object.job_id},
                ),
            ),
            BreadCrumb("Results"),
        ]

    def render_to_json(self, context, **json_kwargs):
        return HttpResponse(
            JsonSerializer().render(context["object"]), content_type="application/json"
        )
