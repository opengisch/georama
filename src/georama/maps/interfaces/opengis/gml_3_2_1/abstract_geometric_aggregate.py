from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricAggregate(AbstractGeometricAggregateType):
    """
    Gml:AbstractGeometricAggregate is the abstract head of the substitution group
    for all geometric aggregates.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
