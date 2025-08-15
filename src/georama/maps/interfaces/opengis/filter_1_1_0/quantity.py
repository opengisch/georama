from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Quantity(MeasureType):
    """A numeric value with a scale.

    The content of the element is an amount using the XML Schema type
    double which permits decimal or scientific notation.  An XML
    attribute uom (unit of measure) is required, whose value is a URI
    which identifies the definition of the scale or units by which the
    numeric value must be multiplied.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
