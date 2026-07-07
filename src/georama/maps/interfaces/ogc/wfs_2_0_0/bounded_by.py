from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.envelope_property_type import (
    EnvelopePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class BoundedBy(EnvelopePropertyType):
    class Meta:
        name = "boundedBy"
        namespace = "http://www.opengis.net/wfs/2.0"
