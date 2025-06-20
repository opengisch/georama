from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IncludesValue(AbstractGeneralParameterValueType):
    """
    A composition association to a parameter value or group of values included in
    this group.
    """

    class Meta:
        name = "includesValue"
        namespace = "http://www.opengis.net/gml"
