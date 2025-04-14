import logging
from typing import List

from georama.data_integration.models import VectorDataSet
from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WfsOperation(OgcOperation):
    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        accessible_layers = []
        if layer_names is not None:
            PublishedAsWmsObjects = PublishedAsWms.objects.all()
        else:
            PublishedAsWmsObjects = PublishedAsWms.objects.filter(name__in=layer_names)
        for published_as in PublishedAsWmsObjects:
            if published_as.has_read_permission(self.user, self.appname):
                if isinstance(published_as.vector_dataset, VectorDataSet):
                    accessible_layers.append(published_as)
                else:
                    logging.debug(
                        "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!"
                    )
            elif layer_names is not None:
                # TODO DD: raise exception when asking for specific layers?
                logging.debug(
                    f"User {self.user.username} does not have read permission for layer {published_as.name}."
                )

        return accessible_layers
