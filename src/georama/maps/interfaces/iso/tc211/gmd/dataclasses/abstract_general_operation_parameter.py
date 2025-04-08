from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameter(AbstractGeneralOperationParameterType):
    """
    Gml:GeneralOperationParameter is the abstract definition of a parameter or
    group of parameters used by an operation method.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
