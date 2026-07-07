from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Measure2(MeasureType):
    """
    The value of a physical quantity, together with its unit.
    """

    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml"
