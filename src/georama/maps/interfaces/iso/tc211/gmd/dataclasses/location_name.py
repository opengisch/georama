from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LocationName(CodeType):
    """The gml:locationName property element is a convenience property where the
    text value describes the location of the feature.

    If the location names are selected from a controlled list, then the
    list shall be identified in the codeSpace attribute.
    """

    class Meta:
        name = "locationName"
        namespace = "http://www.opengis.net/gml"
