from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.engineering_datum_ref_type import (
    EngineeringDatumRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesEngineeringDatum(EngineeringDatumRefType):
    """
    Association to the engineering datum used by this CRS.
    """

    class Meta:
        name = "usesEngineeringDatum"
        namespace = "http://www.opengis.net/gml"
