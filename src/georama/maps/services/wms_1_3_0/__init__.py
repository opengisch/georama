from typing import List

from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        accessible_layers = []
        if layer_names:
            query = PublishedAsWms.objects.filter(name__in=layer_names)
        else:
            PublishedAsWms.objects.all()
        for published_as in PublishedAsWms.objects.all():
            # its WMS, we only check for read permission!
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers.append(published_as)
        return accessible_layers
