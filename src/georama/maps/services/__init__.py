from typing import TYPE_CHECKING

from django.db.models import Model
from xsdata.formats.dataclass.serializers import XmlSerializer

from georama.core.models import Organisation
from georama.maps.interfaces.ogc.wfs_2_0_0 import Exception, ExceptionReport
from georama.maps.models import WmsLayer

if TYPE_CHECKING:
    from django.contrib.auth.models import User


class OgcOperation:
    crs_84 = "CRS:84"
    crs_4326 = "EPSG:4326"
    # layer identifiers are uuids which may start with a digit, this is not a valid
    # NCName and breaks the XML (e.g. <georama:1ddbab8a-...> in GetFeature responses)
    layer_name_prefix = "_"

    def __init__(
        self,
        appname: str,
        url: str,
        user,
        model: Model,
        organisation: Organisation,
        perms: list[str],
    ):
        self.appname: str = appname
        self.url: str = url
        self.user: User = user
        self.model = model
        self.organisation = organisation
        self.perms = perms

    @classmethod
    def encode_layer_name(cls, identifier: str) -> str:
        """Method to bridge layer identifiers which are used in Georama and the
        layer name which is exposed by the OGC services as valid NCName.

        Args:
            identifier: The layer identifier.

        Returns:
            The layer name.
        """
        return f"{cls.layer_name_prefix}{identifier}"

    @classmethod
    def decode_layer_name(cls, layer_name: str) -> str:
        """Method to bridge the layer name which is exposed by the OGC services and the
        layer identifiers which are used in Georama. Plain identifiers pass unchanged.

        Args:
            layer_name: The layer name without namespace.

        Returns:
            The layer identifier.
        """
        return layer_name.removeprefix(cls.layer_name_prefix)

    @property
    def allowed_formats(self) -> list[str]:
        return []

    @staticmethod
    def create_operation_parsing_failed(message: str) -> ExceptionReport:
        """Generic method to create a valid error response XML."""
        return ExceptionReport(exception=[Exception(exception_text=[message])])

    def render_operation_parsing_failed(self, message: str) -> str:
        serializer = XmlSerializer()
        return serializer.render(
            self.create_operation_parsing_failed(
                f"Format {message} is not allowed. Allowed is {self.allowed_formats}"
            ),
            ns_map={
                None: "http://www.opengis.net/wms",
                "xlink": "http://www.w3.org/1999/xlink",
            },
        )

    def obtain_accessible_layers(self, layer_ids: list[str] | None = None) -> list[WmsLayer]:
        return self.model.objects.accessible_layers(
            self.organisation, self.user, self.perms, layer_ids, include_public=True
        ).all()
