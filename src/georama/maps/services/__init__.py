from typing import List

from django.contrib.auth.models import User
from xsdata.formats.dataclass.serializers import XmlSerializer

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.exception import (
    Exception,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.exception_report import (
    ExceptionReport,
)


class OgcOperation:
    def __init__(self, appname: str, url: str, user):
        self.appname: str = appname
        self.url: str = url
        self.user: User = user

    @property
    def allowed_formats(self) -> List[str]:
        return []

    @staticmethod
    def create_operation_parsing_failed(message: str) -> ExceptionReport:
        """
        Generic method to create a valid error response XML.
        """
        return ExceptionReport(exception=[Exception(exception_text=[message])])

    def render_operation_parsing_failed(self, message: str) -> str:
        """Renders the WFS OperationParsigFailed error
        
        Should return HTTP status code 400
        """
        serializer = XmlSerializer()
        return serializer.render(
            self.create_operation_parsing_failed(
                f"Operation parsing failed:  {message}"
            ),
            ns_map={
                None: "http://www.opengis.net/wms",
                "xlink": "http://www.w3.org/1999/xlink",
            },
        )
    
    def render_operation_processing_failed(self, message: str) -> str:
        """Renders the WFS OperationParsigFailed error
        
        Should return HTTP status code 403
        """
        serializer = XmlSerializer()
        return serializer.render(
            self.create_operation_parsing_failed(
                f"Operation processing failed: {message}"
            ),
            ns_map={
                None: "http://www.opengis.net/wms",
                "xlink": "http://www.w3.org/1999/xlink",
            },
        )