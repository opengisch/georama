from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_type import (
    AbstractDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatumType(AbstractDatumType):
    """An engineering datum defines the origin of an engineering coordinate
    reference system, and is used in a region around that origin.

    This origin can be fixed with respect to the earth (such as a
    defined point at a construction site), or be a defined point on a
    moving vehicle (such as on a ship or satellite).
    """
