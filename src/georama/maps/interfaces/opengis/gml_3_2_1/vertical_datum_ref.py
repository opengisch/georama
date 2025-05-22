from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
    VerticalDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatumRef(VerticalDatumPropertyType):
    class Meta:
        name = "verticalDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"
