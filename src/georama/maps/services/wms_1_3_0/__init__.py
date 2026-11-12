from georama.maps.models import WmsLayer
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(self, layer_ids: list[str] | None = None) -> list[WmsLayer]:
        if layer_ids is not None:
            # GeoGirafe requests filtered layers by their WFS feature type name
            layer_ids = [self.decode_layer_name(layer_id) for layer_id in layer_ids]
        layers = self.model.objects.accessible_layers(
            self.organisation, self.user, self.perms, layer_ids, include_public=True
        ).filter(datasource__is_spatial=True)
        if layer_ids is None:
            return list(layers)
        layers_revmap = {layer.identifier: layer for layer in layers}
        missing = [layer_id for layer_id in layer_ids if layer_id not in layers_revmap]
        if missing:
            # geometryless layers have no map, they are unknown to the WMS
            raise self.model.DoesNotExist(f"Layer(s) not found: {missing}")
        return [layers_revmap[layer_id] for layer_id in layer_ids]
