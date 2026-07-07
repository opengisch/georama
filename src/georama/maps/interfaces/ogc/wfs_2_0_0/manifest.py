from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.manifest_type import ManifestType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
