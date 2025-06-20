from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import AbstractCoverageType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Coverage(AbstractCoverageType):
    class Meta:
        name = "_Coverage"
        namespace = "http://www.opengis.net/gml"
