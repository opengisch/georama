from georama.maps.models import WmsLayer
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(self, layer_names: list[str] | None = None) -> list[WmsLayer]:
        return self.model.objects.accessible_layers(
            self.organisation, self.user, self.perms, layer_names
        ).all()
