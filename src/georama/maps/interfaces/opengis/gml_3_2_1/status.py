from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Status(StringOrRefType):
    class Meta:
        name = "status"
        namespace = "http://www.opengis.net/gml/3.2"
