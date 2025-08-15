from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
    AbstractGeneralDerivedCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralDerivedCrs(AbstractGeneralDerivedCrstype):
    """Gml:AbstractGeneralDerivedCRS is a coordinate reference system that is
    defined by its coordinate conversion from another coordinate reference system.

    This abstract complex type shall not be used, extended, or
    restricted, in a GML Application Schema, to define a concrete
    subtype with a meaning equivalent to a concrete subtype specified in
    this document.
    """

    class Meta:
        name = "AbstractGeneralDerivedCRS"
        namespace = "http://www.opengis.net/gml/3.2"
