from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.line_string_type import (
    LineStringType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineString(LineStringType):
    """A LineString is a special curve that consists of a single segment with
    linear interpolation.

    It is defined by two or more coordinate tuples, with linear
    interpolation between them. The number of direct positions in the
    list shall be at least two.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
