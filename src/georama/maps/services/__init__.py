from django.contrib.auth.models import User
from django.db.models import Model
from xsdata.formats.dataclass.serializers import XmlSerializer

from georama.core.models import Organisation
from georama.maps.interfaces.ogc.wfs_2_0_0 import Exception, ExceptionReport


class OgcOperation:
    crs_84 = "CRS:84"
    crs_4326 = "EPSG:4326"

    def __init__(
        self, appname: str, url: str, user, model: Model, organisation: Organisation
    ):
        self.appname: str = appname
        self.url: str = url
        self.user: User = user
        self.model = model
        self.organisation = organisation

    @property
    def allowed_formats(self) -> list[str]:
        return []

    @staticmethod
    def create_operation_parsing_failed(message: str) -> ExceptionReport:
        """
        Generic method to create a valid error response XML.
        """
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
