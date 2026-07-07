from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.parameter_value_type import (
    ParameterValueType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValue1(ParameterValueType):
    """Gml:ParameterValue is a parameter value, an ordered sequence of values, or a
    reference to a file of parameter values.

    This concrete complex type may be used for operation methods without
    using an Application Schema that defines operation-method-
    specialized element names and contents, especially for methods with
    only one instance. This complex type may be used, extended, or
    restricted for well-known operation methods, especially for methods
    with many instances.
    """

    class Meta:
        name = "ParameterValue"
        namespace = "http://www.opengis.net/gml"
