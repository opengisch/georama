from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import AssociationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Association(AssociationType):
    class Meta:
        name = "_association"
        namespace = "http://www.opengis.net/gml"
