from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ExceptionType:
    """
    An Exception element describes one detected error that a server chooses to
    convey to the client.

    :ivar exception_text: Ordered sequence of text strings that describe
        this specific exception or error. The contents of these strings
        are left open to definition by each server implementation. A
        server is strongly encouraged to include at least one
        ExceptionText value, to provide more information about the
        detected error than provided by the exceptionCode. When
        included, multiple ExceptionText values shall provide
        hierarchical information about one detected error, with the most
        significant information listed first.
    :ivar exception_code: A code representing the type of this
        exception, which shall be selected from a set of exceptionCode
        values specified for the specific service operation and server.
    :ivar locator: When included, this locator shall indicate to the
        client where an exception was encountered in servicing the
        client's operation request. This locator should be included
        whenever meaningful information can be provided by the server.
        The contents of this locator will depend on the specific
        exceptionCode and OWS service, and shall be specified in the OWS
        Implementation Specification.
    """

    exception_text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ExceptionText",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    exception_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "exceptionCode",
            "type": "Attribute",
            "required": True,
        },
    )
    locator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
