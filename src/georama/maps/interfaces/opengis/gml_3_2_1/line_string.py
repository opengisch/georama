from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.line_string_type import LineStringType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LineString(LineStringType):
    """A LineString is a special curve that consists of a single segment with
    linear interpolation.

    It is defined by two or more coordinate tuples, with linear
    interpolation between them. The number of direct positions in the
    list shall be at least two.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
