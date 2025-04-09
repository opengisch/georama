from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LengthType(MeasureType):
    """This is a prototypical definition for a specific measure type defined as a
    vacuous extension (i.e. aliases) of gml:MeasureType.

    In this case, the content model supports the description of a length
    (or distance) quantity, with its units. The unit of measure
    referenced by uom shall be suitable for a length, such as metres or
    feet.
    """
