from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.definition_proxy_type import (
    DefinitionProxyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionProxy(DefinitionProxyType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
