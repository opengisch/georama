from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_group_property_type import (
    OperationParameterGroupPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Group(OperationParameterGroupPropertyType):
    """
    Gml:group is an association role to the operation parameter group for which
    this element provides parameter values.
    """

    class Meta:
        name = "group"
        namespace = "http://www.opengis.net/gml/3.2"
