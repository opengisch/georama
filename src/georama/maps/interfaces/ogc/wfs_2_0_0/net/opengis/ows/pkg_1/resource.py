from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Resource:
    """XML encoded GetResourceByID operation response.

    The complexType used by this element shall be specified by each
    specific OWS.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
