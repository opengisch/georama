from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridLengthType(MeasureType):
    """Value of a length (or distance) quantity in a grid, where the grid spacing
    does not have any associated physical units, or does not have a constant
    physical spacing.

    This grid length will often be used in a digital image grid, where
    the base units are likely to be pixel spacings. Uses the MeasureType
    with the restriction that the unit of measure referenced by uom must
    be suitable for length along the axes of a grid, such as pixel
    spacings or grid spacings.
    """
