from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.metadata_type import MetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Metadata(MetadataType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
