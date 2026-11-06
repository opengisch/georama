from django.core.exceptions import ValidationError
from django.http import Http404, HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import PermissionDenied

from georama.features.views.pygeoapi import PygeoapiServer
from georama.webgis.models import WmsLayer


@method_decorator(csrf_exempt, name="dispatch")
class PygeoapiServerWebGIS(PygeoapiServer):
    action = None
    model = WmsLayer

    def accessible_feature_layers(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> list[WmsLayer]:
        feature_layers = (
            self.model.objects.accessible_layers(
                self.request.georama_organisation,
                request.user,
                ["webgis.view_published_theme"],
                include_public=True,
            )
            .filter(datasource__vector__isnull=False)
            .prefetch_related("fields__datasource_field")
        )
        if collection_id is not None:
            try:
                feature_layers = feature_layers.filter(id=collection_id)
            except ValidationError:
                # not a valid identifier, pygeoapi answers with 404
                return []
        return list(feature_layers)

    def get_collection_or_404_or_403(
        self, collection_id: str, perm: str, include_public: bool = False
    ):
        try:
            return self.model.objects.accessible_layers(
                self.request.georama_organisation,
                self.request.user,
                ["webgis.view_published_theme"],
                [collection_id],
                include_public,
            )
        except self.model.DoesNotExist as e:
            raise Http404(e) from e
        except PermissionError as e:
            raise PermissionDenied(e) from e
