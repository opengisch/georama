from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.manifest_type import ManifestType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class InputData(ManifestType):
    """Input data in a XML-encoded OWS operation request, allowing including
    multiple data items with each data item either included or referenced.

    This InputData element, or an element using the ManifestType with a
    more-specific element name (TBR), shall be used whenever applicable
    within XML-encoded OWS operation requests.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
