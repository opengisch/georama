from typing import List

from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation


class WmsOperation(OgcOperation):
    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        accessible_layers = []
        if layer_names:
            query = self.model.objects.filter(name__in=layer_names)
        else:
            query = self.model.objects.filter()
        found_layers = query.all()
        if layer_names:
            found_difference = set(layer_names) - {layer.name for layer in found_layers}
            if len(found_difference) > 0:
                raise PermissionError(f"Layer(s) not found: {list(found_difference)}")
        for published_as in found_layers:
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers.append(published_as)
        if layer_names:
            permission_difference = set(layer_names) - {
                layer.name for layer in accessible_layers
            }
            if len(permission_difference) > 0:
                raise PermissionError(f"Layer(s) not permitted: {list(permission_difference)}")
        return accessible_layers

    # @staticmethod
    # def create_operation_parsing_failed(message: str) -> ExceptionReport:
    #     """
    #     Generic method to create a valid error response XML.
    #     """
    #     return ExceptionReport(exception=[Exception(exception_text=[message])])
    #
    # def render_operation_parsing_failed(self, message: str) -> str:
    #     serializer = XmlSerializer()
    #     return serializer.render(
    #         self.create_operation_parsing_failed(
    #             f"Format {message} is not allowed. Allowed is {self.allowed_formats}"
    #         ),
    #         ns_map={
    #             None: "http://www.opengis.net/wms",
    #             "xlink": "http://www.w3.org/1999/xlink",
    #         },
    #     )