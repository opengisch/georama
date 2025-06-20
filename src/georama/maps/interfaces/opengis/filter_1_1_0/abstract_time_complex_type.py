from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_object_type import (
    AbstractTimeObjectType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    """
    The abstract supertype for temporal complexes.
    """
