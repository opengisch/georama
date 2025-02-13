from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.ows.pkg_1.reference_type import ReferenceType

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

    :ivar request_message: The XML-encoded operation request message to
        be sent to request this input data from another web server using
        HTTP Post.
    :ivar request_message_reference: Reference to the XML-encoded
        operation request message to be sent to request this input data
        from another web server using HTTP Post. The referenced message
        shall be attached to the same message (using the cid scheme), or
        be accessible using a URL.
    """

    request_message: Optional[object] = field(
        default=None,
        metadata={
            "name": "RequestMessage",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    request_message_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
