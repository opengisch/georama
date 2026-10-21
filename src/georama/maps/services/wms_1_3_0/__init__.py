from georama.maps.models import WmsLayer
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(self, layer_ids: list[str] | None = None) -> list[WmsLayer]:
        layers = self.model.objects.accessible_layers(
            self.organisation, self.user, self.perms, layer_ids, include_public=True
        ).all()
        if layer_ids is None:
            return list(layers)
        layers_revmap = {layer.identifier: layer for layer in layers}
        return [layers_revmap[layer_id] for layer_id in layer_ids]
