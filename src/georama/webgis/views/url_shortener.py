from django.conf import settings
from django.db import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.utils.crypto import get_random_string
from django.views import View

from georama.webgis.models import UrlShortener


class UrlShortenerCreate(View):
    def post(self, request: HttpRequest):
        url = request.POST.get("url", "").strip()
        if not url:
            return JsonResponse({"error": "Missing URL."}, status=400)

        if not url.startswith(settings.WEBGISURL):
            return JsonResponse({"error": "Invalid URL."}, status=400)

        while True:
            try:
                short = UrlShortener.objects.create(id=get_random_string(length=6), url=url)
                break
            except IntegrityError:
                continue

        short_url = request.build_absolute_uri(f"/webgis/short/get/{short.id}")
        return JsonResponse({"short_url": short_url}, status=201)


class UrlShortenerRetrieve(View):
    def get(self, _request: HttpRequest, id: str):
        try:
            short = UrlShortener.objects.get(id=id)
        except UrlShortener.DoesNotExist:
            return JsonResponse({"error": "Not found."}, status=404)

        return JsonResponse({"long_url": short.url}, status=200)
