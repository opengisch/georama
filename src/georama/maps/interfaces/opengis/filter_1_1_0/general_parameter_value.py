from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralParameterValue(AbstractGeneralParameterValueType):
    class Meta:
        name = "_generalParameterValue"
        namespace = "http://www.opengis.net/gml"
