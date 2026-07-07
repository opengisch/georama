from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregate(AbstractGeometricAggregateType):
    """
    Gml:AbstractGeometricAggregate is the abstract head of the substitution group
    for all geometric aggregates.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
