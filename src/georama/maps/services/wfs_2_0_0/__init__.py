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

        if layer_names is None:
            published_as_wms_objects = PublishedAsWms.objects.all()
        else:
            # TODO: ?distinguish between different publications of the same layer? (published_as names with uuid?)
            published_as_wms_objects = PublishedAsWms.objects.filter(name__in=layer_names)
            if len(published_as_wms_objects) < len(layer_names):
                published_names = set([pa.name for pa in published_as_wms_objects])
                non_existing_layers = [ln for ln in layer_names if ln not in published_names]
                raise Exception(f"Querying non-existing WFS layers: {", ".join(non_existing_layers)}")

        for published_as in published_as_wms_objects:
            if published_as.has_read_permission(self.user, self.appname):
                if isinstance(published_as.vector_dataset, VectorDataSet):
                    accessible_layers.append(published_as)
                else:
                    logging.debug(
                        "linked dataset has to be VectorDataSet for WFS 2.0.0, all others are ignored!"
                    )
            elif layer_names is not None:
                raise Exception(f"User {self.user.username} does not have read permission for layer {published_as.name}.")

        return accessible_layers
