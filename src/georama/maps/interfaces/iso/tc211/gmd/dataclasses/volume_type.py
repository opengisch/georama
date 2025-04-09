from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VolumeType(MeasureType):
    pass
