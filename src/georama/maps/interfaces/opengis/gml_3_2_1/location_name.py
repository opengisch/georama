from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LocationName(CodeType):
    """The gml:locationName property element is a convenience property where the
    text value describes the location of the feature.

    If the location names are selected from a controlled list, then the
    list shall be identified in the codeSpace attribute.
    """

    class Meta:
        name = "locationName"
        namespace = "http://www.opengis.net/gml/3.2"
