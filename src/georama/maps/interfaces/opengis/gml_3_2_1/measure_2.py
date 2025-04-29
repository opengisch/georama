from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Measure2:
    """
    The value of a physical quantity, together with its unit.
    """

    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml/3.2"
