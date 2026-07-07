from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.parameter_value_group_type import (
    ParameterValueGroupType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValueGroup(ParameterValueGroupType):
    class Meta:
        name = "parameterValueGroup"
        namespace = "http://www.opengis.net/gml"
