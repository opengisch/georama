from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.arc_string_type import ArcStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcString(ArcStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
