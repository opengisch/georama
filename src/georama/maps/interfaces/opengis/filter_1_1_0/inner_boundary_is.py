from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_ring_property_type import (
    AbstractRingPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class InnerBoundaryIs(AbstractRingPropertyType):
    """Deprecated with GML 3.0, included only for backwards compatibility with GML
    2.

    Use "interior" instead.
    """

    class Meta:
        name = "innerBoundaryIs"
        namespace = "http://www.opengis.net/gml"
