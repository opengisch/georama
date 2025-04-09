from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StatusReference(ReferenceType):
    class Meta:
        name = "statusReference"
        namespace = "http://www.opengis.net/gml"
