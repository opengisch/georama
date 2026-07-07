from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.base_request_type import BaseRequestType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeFeatureTypeType(BaseRequestType):
    type_name: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "TypeName",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    output_format: str = field(
        default="application/gml+xml; version=3.2",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        },
    )
