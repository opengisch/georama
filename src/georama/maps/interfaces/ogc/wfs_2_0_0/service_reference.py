from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.service_reference_type import (
    ServiceReferenceType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ServiceReference(ServiceReferenceType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
