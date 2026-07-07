from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeReferenceSystem(TimeReferenceSystemType):
    """A reference system is characterized in terms of its domain of validity: the spatial and temporal extent over which it is applicable. The basic GML element for temporal reference systems is gml:TimeReferenceSystem.  Its content model extends gml:DefinitionType with one additional property, gml:domainOfValidity."""

    class Meta:
        namespace = "http://www.opengis.net/gml"
