from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum_type_1 import (
    VerticalDatumType1,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatum(VerticalDatumType1):
    class Meta:
        namespace = "http://www.opengis.net/gml"
