from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.geodetic_datum_type import (
    GeodeticDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatum(GeodeticDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
