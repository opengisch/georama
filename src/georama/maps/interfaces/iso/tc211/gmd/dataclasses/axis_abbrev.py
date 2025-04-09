from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AxisAbbrev(CodeType):
    """Gml:axisAbbrev is the abbreviation used for this coordinate system axis;
    this abbreviation is also used to identify the coordinates in the coordinate
    tuple.

    The codeSpace attribute may reference a source of more information
    on a set of standardized abbreviations, or on this abbreviation.
    """

    class Meta:
        name = "axisAbbrev"
        namespace = "http://www.opengis.net/gml"
