import logging
from typing import List

from georama.data_integration.models import VectorDataSet
from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WfsOperation(OgcOperation):
    def obtain_accessible_layers(self) -> List[PublishedAsWms]:
        accessible_layers = []
        for published_as in PublishedAsWms.objects.all():
            if published_as.has_read_permission(self.user, self.appname):
                if isinstance(published_as.vector_dataset, VectorDataSet):
                    accessible_layers.append(published_as)
                else:
                    logging.debug(
                        "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!"
                    )
        return accessible_layers
