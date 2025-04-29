from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Value:
    """
    Gml:value is a numeric value of an operation parameter, with its associated
    unit of measure.
    """

    class Meta:
        name = "value"
        namespace = "http://www.opengis.net/gml/3.2"
