from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "ObliqueCartesianCSType"
