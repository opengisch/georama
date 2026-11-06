from dataclasses import dataclass

from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from georama.features.views.pygeoapi import PygeoapiServer
from georama.integration.models.datasource import VectorField
from georama.webgis.models import WmsLayer


@dataclass
class PublishedField:
    """Interim field of a published WmsLayer until the webgis twin exists,
    all fields visible.
    """

    name: str
    datasource_field: VectorField


@method_decorator(csrf_exempt, name="dispatch")
class PygeoapiServerWebGIS(PygeoapiServer):
    action = None
    model = WmsLayer
    perm_view = "webgis.view_published_theme"

    def accessible_feature_layers(
        self, request: HttpRequest, collection_id: str | None = None
    ) -> list[WmsLayer]:
        feature_layers = (
            self.model.objects.accessible_layers(
                self.request.georama_organisation,
                request.user,
                [self.perm_view],
                include_public=True,
            )
            .filter(datasource__vector__isnull=False)
            .prefetch_related("datasource__vector__fields__datasource_field")
        )
        if collection_id is not None:
            try:
                feature_layers = feature_layers.filter(id=collection_id)
            except ValidationError:
                # not a valid identifier, pygeoapi answers with 404
                return []
        return list(feature_layers)

    def get_visible_fields(self, feature_layer: WmsLayer) -> list[PublishedField]:
        return [
            PublishedField(name=field.name, datasource_field=field)
            for field in feature_layer.datasource.vector.fields.all()
        ]

    def get_limits(self, feature_layer: WmsLayer) -> dict:
        # defaults of features.FeatureLayer, WmsLayer has no limits yet
        return {"on_exceed": "error", "max_items": 500, "default_items": 10}
