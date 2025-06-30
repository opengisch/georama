from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ServiceReferenceType(ReferenceType):
    """Complete reference to a remote resource that needs to be retrieved from an
    OWS using an XML-encoded operation request.

    This element shall be used, within an InputData or Manifest element
    that is used for input data, when that input data needs to be
    retrieved from another web service using a XML-encoded OWS operation
    request. This element shall not be used for local payload input data
    or for requesting the resource from a web server using HTTP Get.
    """

    request_message_or_request_message_reference: Optional[Union[object, str]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RequestMessage",
                    "type": object,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
                {
                    "name": "RequestMessageReference",
                    "type": str,
                    "namespace": "http://www.opengis.net/ows/1.1",
                },
            ),
        },
    )
