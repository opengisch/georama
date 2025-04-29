from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.cartesian_cstype import CartesianCstype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CartesianCs1(CartesianCstype):
    """Gml:CartesianCS is a 1-, 2-, or 3-dimensional coordinate system.

    In the 1-dimensional case, it contains a single straight coordinate
    axis. In the 2- and 3-dimensional cases gives the position of points
    relative to orthogonal straight axes. In the multi-dimensional case,
    all axes shall have the same length unit of measure. A CartesianCS
    shall have one, two, or three gml:axis property elements.
    """

    class Meta:
        name = "CartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"
