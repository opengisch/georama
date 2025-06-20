from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_object_type import (
    AbstractTimeObjectType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeObject(AbstractTimeObjectType):
    """
    This abstract element acts as the head of the substitution group for temporal
    primitives and complexes.
    """

    class Meta:
        name = "_TimeObject"
        namespace = "http://www.opengis.net/gml"
