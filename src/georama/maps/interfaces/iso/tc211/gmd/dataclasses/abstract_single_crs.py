from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    AbstractCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSingleCrs(AbstractCrstype):
    """
    Gml:AbstractSingleCRS implements a coordinate reference system consisting of
    one coordinate system and one datum (as opposed to a Compound CRS).
    """

    class Meta:
        name = "AbstractSingleCRS"
        namespace = "http://www.opengis.net/gml"
