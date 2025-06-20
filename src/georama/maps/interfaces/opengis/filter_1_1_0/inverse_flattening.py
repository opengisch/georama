from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class InverseFlattening(MeasureType):
    """Inverse flattening value of the ellipsoid.

    Value is a scale factor (or ratio) that has no physical unit. Uses
    the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a scale factor, such as
    percent, permil, or parts-per-million.
    """

    class Meta:
        name = "inverseFlattening"
        namespace = "http://www.opengis.net/gml"
