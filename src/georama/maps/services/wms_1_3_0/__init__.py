from georama.core.entities.models import PublishedAs
from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(
        self, layer_names: list[str] | None = None
    ) -> list[PublishedAsWms]:
        accessible_layers = {}
        if layer_names:
            found_layers = self.model.objects.filter(name__in=layer_names)
        else:
            found_layers = self.model.objects.all()
        if layer_names:
            found_difference = set(layer_names) - {layer.name for layer in found_layers}
            if len(found_difference) > 0:
                raise PermissionError(f"Layer(s) not found: {list(found_difference)}")
        for published_as in found_layers:
            published_as: PublishedAs
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers[published_as.name] = published_as
        if layer_names:
            permission_difference = set(layer_names) - set(accessible_layers)
            if len(permission_difference) > 0:
                raise PermissionError(f"Layer(s) not permitted: {list(permission_difference)}")
            return [accessible_layers[layer_name] for layer_name in layer_names]
        return list(accessible_layers.values())
