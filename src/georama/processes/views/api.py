from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from ninja import NinjaAPI
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.json import JsonSerializer

from georama.processes.interface.ogc_api.v_100.processes import (
    JobControlOptions,
    Landing,
    Link,
    ProcessBase,
    TransmissionMode,
)
from georama.processes.models import PublishedAsProcess
from georama.processes.views.gui import Index

config = SerializerConfig(indent="  ")


api = NinjaAPI()


@api.get("/", response=Landing)
def landing(request, f: str | None = None, limit: int = 10):
    view = Index()
    view.request = request
    view.args = {}
    view.kwargs = {}
    qs = view.get_queryset()
    api_processes = []
    for process in qs:
        api_processes.append(
            ProcessBase(
                id=process.process_id,
                description=process.qsl_algorithm.short_help_string,
                job_control_options=[JobControlOptions.SYNC],
                output_transmission=[TransmissionMode.VALUE],
                title=process.qsl_algorithm.display_name,
                version="1.0.0",
                links=[],
            )
        )
        return Landing(
            processes=api_processes,
            links=[
                Link(
                    type=api.renderer.media_type,
                    rel="self",
                    href=reverse("processes:landing"),
                    href_lang="en",
                    title=_("This document as JSON"),
                )
            ],
        )


class OgcApiProcesses100(View):
    response_format: str
    limit: int
    action: str = None
    content_type_lookup = {"json": "application/json"}

    @property
    def content_type(self) -> str:
        return self.content_type_lookup[self.response_format]

    def dispatch(self, request, *args, **kwargs):
        self.limit = int(request.GET.get("limit", 10))
        self.response_format = request.GET.get("f", "json")
        handler = getattr(self, f"{self.action}", None)

        if callable(handler):
            return handler(request, *args, **kwargs)

        raise Http404(f"Unknown action: {self.action!r}")

    def _landing(self, request: HttpRequest) -> Landing:
        processes = PublishedAsProcess.objects.order_by("-process_id").all()[: self.limit]
        api_processes = []
        for process in processes:
            api_processes.append(
                ProcessBase(
                    id=process.process_id,
                    description=process.qsl_algorithm.short_help_string,
                    job_control_options=[JobControlOptions.SYNC],
                    output_transmission=[TransmissionMode.VALUE],
                    title=process.qsl_algorithm.display_name,
                    version="1.0.0",
                    links=[],
                )
            )
            return Landing(
                processes=api_processes,
                links=[
                    Link(
                        type=api.renderer.media_type,
                        rel="self",
                        href=reverse("processes:landing"),
                        href_lang="en",
                        title=_("This document as JSON"),
                    )
                ],
            )

    def landing(self, request: HttpRequest):
        if self.response_format == "json":
            return HttpResponse(
                JsonSerializer(config).render(self._landing(request)),
                content_type=self.content_type,
            )
