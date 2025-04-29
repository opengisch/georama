from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DoubleOrNilReasonTupleList:
    """Gml:doubleOrNilReasonList consists of a list of gml:doubleOrNilReason
    values, each separated by a whitespace.

    The gml:doubleOrNilReason values are grouped into tuples where the
    dimension of each tuple in the list is equal to the number of range
    parameters.
    """

    class Meta:
        name = "doubleOrNilReasonTupleList"
        namespace = "http://www.opengis.net/gml/3.2"
