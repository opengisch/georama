from typing import List

from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        print(layer_names)
        accessible_layers = []
        if layer_names:
            query = self.model.objects.filter(name__in=layer_names)
        else:
            query = self.model.objects.filter()
        for published_as in query.all():
            print(type(published_as))
            # its WMS, we only check for read permission!
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers.append(published_as)
        return accessible_layers
