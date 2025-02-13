from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.value_type import ValueType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class MaximumValue(ValueType):
    """
    Maximum value of this numeric parameter.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
