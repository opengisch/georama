from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_group_property_type import (
    OperationParameterGroupPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Group(OperationParameterGroupPropertyType):
    """
    Gml:group is an association role to the operation parameter group for which
    this element provides parameter values.
    """

    class Meta:
        name = "group"
        namespace = "http://www.opengis.net/gml"
