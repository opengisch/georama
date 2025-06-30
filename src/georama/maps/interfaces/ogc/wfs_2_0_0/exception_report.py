from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.exception import Exception
from georama.maps.interfaces.ogc.wfs_2_0_0.lang_value import LangValue

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ExceptionReport:
    """
    Report message returned to the client that requested any OWS operation when the
    server detects an error while processing that operation request.

    :ivar exception: Unordered list of one or more Exception elements
        that each describes an error. These Exception elements shall be
        interpreted by clients as being independent of one another (not
        hierarchical).
    :ivar version: Specification version for OWS operation. The string
        value shall contain one x.y.z "version" value (e.g., "2.1.3"). A
        version number shall contain three non-negative integers
        separated by decimal points, in the form "x.y.z". The integers y
        and z shall not exceed 99. Each version shall be for the
        Implementation Specification (document) and the associated XML
        Schemas to which requested operations will conform. An
        Implementation Specification version normally specifies XML
        Schemas against which an XML encoded operation response must
        conform and should be validated. See Version negotiation
        subclause for more information.
    :ivar lang: Identifier of the language used by all included
        exception text values. These language identifiers shall be as
        specified in IETF RFC 4646. When this attribute is omitted, the
        language used is not identified.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    exception: list[Exception] = field(
        default_factory=list,
        metadata={
            "name": "Exception",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\d+\.\d?\d\.\d?\d",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
