from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_proxy_type import (
    DefinitionProxyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionProxy(DefinitionProxyType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
