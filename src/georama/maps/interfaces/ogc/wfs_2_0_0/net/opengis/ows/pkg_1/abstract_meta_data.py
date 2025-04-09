from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AbstractMetaData:
    """Abstract element containing more metadata about the element that includes
    the containing "metadata" element.

    A specific server implementation, or an Implementation
    Specification, can define concrete elements in the AbstractMetaData
    substitution group.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
