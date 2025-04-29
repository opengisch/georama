from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ValueList:
    """Gml:valueList is an ordered sequence of two or more numeric values of an
    operation parameter list, where each value has the same associated unit of
    measure.

    An element of this type contains a space-separated sequence of
    double values.
    """

    class Meta:
        name = "valueList"
        namespace = "http://www.opengis.net/gml/3.2"
