from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.linear_cstype import LinearCstype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearCs1(LinearCstype):
    """Gml:LinearCS is a one-dimensional coordinate system that consists of the
    points that lie on the single axis described.

    The associated coordinate is the distance – with or without offset –
    from the specified datum to the point along the axis. A LinearCS
    shall have one gml:axis property element.
    """

    class Meta:
        name = "LinearCS"
        namespace = "http://www.opengis.net/gml/3.2"
