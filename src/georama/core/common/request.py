from django.http import HttpRequest
from rest_framework.request import Request

from georama.core.models import Organisation


class GeoramaHttpRequest(HttpRequest):
    georama_organisation: Organisation | None
    georama_header_authenticated: bool


class GeoramaDrfRequest(Request):
    georama_organisation: Organisation | None
