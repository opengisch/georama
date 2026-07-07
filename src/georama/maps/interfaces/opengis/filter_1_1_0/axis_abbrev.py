from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AxisAbbrev(CodeType):
    """The abbreviation used for this coordinate system axis.

    This abbreviation can be used to identify the ordinates in a
    coordinate tuple. Examples are X and Y. The codeSpace attribute can
    reference a source of more information on a set of standardized
    abbreviations, or on this abbreviation.
    """

    class Meta:
        name = "axisAbbrev"
        namespace = "http://www.opengis.net/gml"
