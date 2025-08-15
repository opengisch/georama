from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_object_type import (
    AbstractTimeObjectType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    pass
