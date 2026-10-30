from georama.maps.models import WmsLayer
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(self, layer_ids: list[str] | None = None) -> list[WmsLayer]:
        if layer_ids is not None:
            # GeoGirafe requests filtered layers by their WFS feature type name
            layer_ids = [self.decode_layer_name(layer_id) for layer_id in layer_ids]
        layers = self.model.objects.accessible_objects(
            self.organisation, self.user, self.perms, layer_ids, include_public=True
        ).all()
        if layer_ids is None:
            return list(layers)
        layers_revmap = {layer.identifier: layer for layer in layers}
        return [layers_revmap[layer_id] for layer_id in layer_ids]
