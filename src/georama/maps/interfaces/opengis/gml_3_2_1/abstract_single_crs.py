from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    AbstractCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSingleCrs(AbstractCrstype):
    """
    Gml:AbstractSingleCRS implements a coordinate reference system consisting of
    one coordinate system and one datum (as opposed to a Compound CRS).
    """

    class Meta:
        name = "AbstractSingleCRS"
        namespace = "http://www.opengis.net/gml/3.2"
