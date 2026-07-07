from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    """
    This is the abstract root type of the geometric aggregates.
    """
