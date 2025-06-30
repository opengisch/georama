from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.value_type import ValueType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DefaultValue(ValueType):
    """
    The default value for a quantity for which multiple values are allowed.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
