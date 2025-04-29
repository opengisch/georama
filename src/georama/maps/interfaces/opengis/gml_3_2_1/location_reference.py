from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LocationReference(ReferenceType):
    """
    The gml:locationReference property element is a convenience property where the
    text value referenced by the xlink:href attribute describes the location of the
    feature.
    """

    class Meta:
        name = "locationReference"
        namespace = "http://www.opengis.net/gml/3.2"
