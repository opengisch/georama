from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.extension_ops_type import ExtensionOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ExtensionOps(ExtensionOpsType):
    class Meta:
        name = "extensionOps"
        namespace = "http://www.opengis.net/fes/2.0"
