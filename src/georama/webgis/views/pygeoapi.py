from dataclasses import dataclass

from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from georama.features.models import FeatureLayer
from georama.features.views.pygeoapi import PygeoapiServer
from georama.integration.models import Vector
from georama.integration.models.datasource import VectorField
from georama.maps.services.wfs_2_0_0 import WfsOperation
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
    perm_create = "webgis.create_objects_theme_vector_layer"
    perm_update = "webgis.update_objects_theme_vector_layer"
    perm_delete = "webgis.delete_objects_theme_vector_layer"

    def refine_accessible_layers(self, feature_layers: QuerySet) -> QuerySet:
        # only WMS layers on a vector datasource can be served as collection
        return feature_layers.filter(datasource__vector__isnull=False).prefetch_related(
            "datasource__vector__fields"
        )

    def get_reference_target_layers(self, project) -> QuerySet[WmsLayer]:
        # the collection is the WMS layer itself, served from its vector datasource
        return (
            self.model.objects.filter(datasource__project=project, datasource__vector__isnull=False)
            .select_related("datasource__vector")
            .prefetch_related("datasource__vector__fields")
        )

    def collection_identifier(self, collection_id: str) -> str:
        return WfsOperation.decode_layer_name(collection_id)

    def collection_key(self, feature_layer: WmsLayer) -> str:
        # the GeoGirafe layer id, the editable check compares against it
        return WfsOperation.encode_layer_name(feature_layer.identifier)

    def is_editable(self, feature_layer: WmsLayer, permission_checker) -> bool:
        # write permissions are granted on the theme, not on its layers
        return any(
            permission_checker.has_perm(perm, feature_layer.theme)
            for perm in (self.perm_create, self.perm_update, self.perm_delete)
        )

    def get_vector(self, feature_layer: WmsLayer) -> Vector:
        return feature_layer.datasource.vector

    def get_visible_fields(self, feature_layer: WmsLayer) -> list[PublishedField]:
        return [
            PublishedField(name=field.name, datasource_field=field)
            for field in feature_layer.datasource.vector.fields.all()
        ]

    def get_limits(self, feature_layer: WmsLayer) -> dict:
        # WmsLayer has no limits yet, the defaults of a FeatureLayer apply
        return {
            name: FeatureLayer._meta.get_field(name).default
            for name in ("on_exceed", "max_items", "default_items")
        }
