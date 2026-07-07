from guardian.shortcuts import get_objects_for_user, get_perms

from georama.maps.models import WmsLayer
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(self, layer_names: list[str] | None = None) -> list[WmsLayer]:
        # TODO@maps: Remember to add the organisation logic here

        if layer_names is None:
            return list(get_objects_for_user(self.user, ["view_wmslayer"], self.model))

        accessible_layers = {}

        found_layers = self.model.objects.filter(id__in=layer_names)
        found_difference = set(layer_names) - {wms_layer.name for wms_layer in found_layers}

        if len(found_difference) > 0:
            raise PermissionError(f"Layer(s) not found: {list(found_difference)}")

        for wms_layer in found_layers:
            if "view_wmslayer" in get_perms(self.user, wms_layer):
                accessible_layers[wms_layer.name] = wms_layer

        permission_difference = set(layer_names) - set(accessible_layers)
        if len(permission_difference) > 0:
            raise PermissionError(f"Layer(s) not permitted: {list(permission_difference)}")
        return [accessible_layers[layer_name] for layer_name in layer_names]
