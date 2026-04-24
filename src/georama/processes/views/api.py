from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
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

config = SerializerConfig(indent="  ")


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
                    type=self.content_type,
                    rel="self",
                    href=request.build_absolute_uri(reverse("processes:api-landing")),
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
