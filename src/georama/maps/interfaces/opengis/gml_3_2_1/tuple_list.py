from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TupleList:
    """Gml:CoordinatesType consists of a list of coordinate tuples, with each
    coordinate tuple separated by the ts or tuple separator (whitespace), and each
    coordinate in the tuple by the cs or coordinate separator (comma).

    The gml:tupleList encoding is effectively "band-interleaved".
    """

    class Meta:
        name = "tupleList"
        namespace = "http://www.opengis.net/gml/3.2"
