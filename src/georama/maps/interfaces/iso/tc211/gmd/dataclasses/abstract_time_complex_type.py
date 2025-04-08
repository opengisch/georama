from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_object_type import (
    AbstractTimeObjectType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    pass
