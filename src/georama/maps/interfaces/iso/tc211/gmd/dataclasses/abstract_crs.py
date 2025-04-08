from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    AbstractCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCrs(AbstractCrstype):
    """Gml:AbstractCRS specifies a coordinate reference system which is usually
    single but may be compound.

    This abstract complex type shall not be used, extended, or
    restricted, in a GML Application Schema, to define a concrete
    subtype with a meaning equivalent to a concrete subtype specified in
    this document.
    """

    class Meta:
        name = "AbstractCRS"
        namespace = "http://www.opengis.net/gml"
