from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTopologyType(AbstractGmltype):
    pass
