from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic.base import TemplateView
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.core.views.entities.entity_detail import GeoramaEntityDetailView
from georama.core.views.entities.published_item_index import GeoramaPublishedItemIndex
from georama.core.views.generic.mixins import (
    BreadcrumbMixin,
    PermissionRequiredMixin,
)
from georama.processes.apps import central_app_label
from georama.processes.interface.ogc_api.v_100.processes import (
    JobControlOptions,
    Link,
    ProcessBase,
    Processes,
    TransmissionMode,
)
from georama.processes.models import Job, PublishedAsProcess


class ApiLanding(BreadcrumbMixin, TemplateView):
    entity_name = "process"
    template_name = "processes/api/landing.html"

    def get(self, request: HttpRequest):
        pass


class ApiProcessDetail(PermissionRequiredMixin, GeoramaEntityDetailView):
    model = PublishedAsProcess
    entity_name = "process"
    permission_required = model.perm_view()


class ApiProcessExection(PermissionRequiredMixin, View):
    entity_name = "proces"

    def post(self, request: HttpRequest):
        pass


class ApiProcessList(PermissionRequiredMixin, GeoramaPublishedItemIndex):
    model = PublishedAsProcess
    template_name = "processes/api/process_list.html"
    entity_name = "process"
    permission_required = model.perm_view()
    limit: int
    format: str
    media_types: dict[str, str] = {"json": "application/json", "html": "text/html"}

    def get_queryset(self, request: HttpRequest):
        api_processes = []
        for process in super().get_queryset(request):
            api_processes.append(
                ProcessBase(
                    id=process.process_id,
                    description=process.qsl_algorithm.short_help_string,
                    job_control_options=[JobControlOptions.SYNC],
                    output_transmission=[TransmissionMode.VALUE],
                    title=process.qsl_algorithm.display_name,
                    version="1.0.0",
                    links=[
                        Link(
                            type=self.media_types["json"],
                            rel="execution",
                            href=request.build_absolute_uri(
                                reverse(f"{central_app_label}:api-process-execution")
                            ),
                            title=_("Process execution"),
                        )
                    ],
                )
            )
        return Processes(
            processes=api_processes,
            links=[
                Link(
                    type=self.media_types["json"],
                    rel="self",
                    href=request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-landing")
                    ),
                    href_lang="en",
                    title=_("This document as JSON"),
                ),
                Link(
                    type=self.media_types["html"],
                    rel="self",
                    href=request.build_absolute_uri(
                        reverse(f"{central_app_label}:api-landing")
                    )
                    + "?f=html",
                    href_lang="en",
                    title=_("This document as HTML"),
                ),
            ],
        )

    def get(self, request: HttpRequest):
        """Do stuff herer"""
        if request.GET.get("f") == "json":
            return self.as_json()
        return self.get(request)

    def post(self):
        return self.render_to_response(self.get_conte)

    def as_json(self, request: HttpRequest):
        json = JsonSerializer().render(self.get_queryset(request))
        return HttpResponse(json, content_type="application/json")


class ApiJobList(GeoramaEntityDetailView):
    entity_name = "job"
    model = Job

    def render_to_response(self, context, **response_kwargs):
        request_format = self.request.GET.get("f", "json")
        if request_format == "json":
            return HttpResponse(self.as_json(self.request), content_type="application/json")
        else:
            return super().render_to_response(context, **response_kwargs)

    def as_json(self, request: HttpRequest):
        return JsonSerializer().render({})
