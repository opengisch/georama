from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum_type_type import (
    VerticalDatumTypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumType(VerticalDatumTypeType):
    class Meta:
        name = "verticalDatumType"
        namespace = "http://www.opengis.net/gml"
