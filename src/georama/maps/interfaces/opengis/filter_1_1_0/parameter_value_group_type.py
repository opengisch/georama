from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.includes_value import IncludesValue
from georama.maps.interfaces.opengis.filter_1_1_0.values_of_group import ValuesOfGroup

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValueGroupType(AbstractGeneralParameterValueType):
    """A group of related parameter values.

    The same group can be repeated more than once in a Conversion,
    Transformation, or higher level parameterValueGroup, if those
    instances contain different values of one or more parameterValues
    which suitably distinquish among those groups. This concrete
    complexType can be used for operation methods without using an
    Application Schema that defines operation-method-specialized element
    names and contents, especially for methods with only one instance.
    This complexType can be used, extended, or restricted for well-known
    operation methods, especially for methods with many instances.

    :ivar includes_value: Unordered set of composition associations to
        the parameter values and groups of values included in this
        group.
    :ivar values_of_group:
    """

    includes_value: list[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        },
    )
    values_of_group: ValuesOfGroup | None = field(
        default=None,
        metadata={
            "name": "valuesOfGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
