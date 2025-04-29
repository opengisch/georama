from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AxisAbbrev:
    """Gml:axisAbbrev is the abbreviation used for this coordinate system axis;
    this abbreviation is also used to identify the coordinates in the coordinate
    tuple.

    The codeSpace attribute may reference a source of more information
    on a set of standardized abbreviations, or on this abbreviation.
    """

    class Meta:
        name = "axisAbbrev"
        namespace = "http://www.opengis.net/gml/3.2"
