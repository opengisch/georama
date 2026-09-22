from rest_framework.viewsets import ModelViewSet

from georama.webgis.api.serializers import (
    UrlShortenerCreateSerializer,
    UrlShortenerRetrieveSerializer,
)
from georama.webgis.models import UrlShortener


class UrlShortenerViewSet(ModelViewSet):
    queryset = UrlShortener.objects.all()
    serializer_class = UrlShortenerCreateSerializer
    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.action == "create":
            return UrlShortenerCreateSerializer
        if self.action == "retrieve":
            return UrlShortenerRetrieveSerializer
        raise AssertionError(f"Unsupported action: {self.action}")
