from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum_ref_type import (
    VerticalDatumRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalDatum(VerticalDatumRefType):
    """
    Association to the vertical datum used by this CRS.
    """

    class Meta:
        name = "usesVerticalDatum"
        namespace = "http://www.opengis.net/gml"
