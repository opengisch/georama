from dataclasses import dataclass

from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from georama.features.references import ReferenceTarget
from georama.features.views.pygeoapi import PygeoapiServer
from georama.integration.models import Vector
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
    landing_url_name = "webgis:landing"
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
            .prefetch_related("datasource__vector__fields")
        )
        if collection_id is not None:
            try:
                feature_layers = feature_layers.filter(id=collection_id)
            except ValidationError:
                # not a valid identifier, pygeoapi answers with 404
                return []
        return list(feature_layers)

    @staticmethod
    def get_reference_targets(project) -> dict[str, ReferenceTarget]:
        """The published WMS layers of the project, keyed by QGIS layer id. Their collection
        is the WMS layer itself, with the primary key of its vector datasource.
        """
        targets: dict[str, ReferenceTarget] = {}
        layers = (
            WmsLayer.objects.filter(datasource__project=project, datasource__vector__isnull=False)
            .select_related("datasource")
            .prefetch_related("datasource__vector__fields")
        )
        for layer in layers:
            key_field = next(
                (
                    f.name
                    for f in layer.datasource.vector.fields.all()
                    if f.definition and f.field_definition_qsl.is_primary_key
                ),
                None,
            )
            if key_field is not None:
                targets[layer.datasource.qgis_layer_id] = ReferenceTarget(
                    str(layer.identifier), key_field
                )
        return targets

    def get_vector(self, feature_layer: WmsLayer) -> Vector:
        return feature_layer.datasource.vector

    def get_visible_fields(self, feature_layer: WmsLayer) -> list[PublishedField]:
        return [
            PublishedField(name=field.name, datasource_field=field)
            for field in feature_layer.datasource.vector.fields.all()
        ]

    def get_limits(self, feature_layer: WmsLayer) -> dict:
        # defaults of features.FeatureLayer, WmsLayer has no limits yet
        return {"on_exceed": "error", "max_items": 500, "default_items": 10}
