from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    AbstractGeneralDerivedCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        namespace = "http://www.opengis.net/gml"
