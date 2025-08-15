from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_reference_system_type import (
    AbstractTimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeReferenceSystem(AbstractTimeReferenceSystemType):
    """
    Abstract element serves primarily as the head of a substitution group for
    temporal reference systems.
    """

    class Meta:
        name = "_TimeReferenceSystem"
        namespace = "http://www.opengis.net/gml"
