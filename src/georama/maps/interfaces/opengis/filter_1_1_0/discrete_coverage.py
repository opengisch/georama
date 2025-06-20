from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import (
    AbstractDiscreteCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DiscreteCoverage(AbstractDiscreteCoverageType):
    class Meta:
        name = "_DiscreteCoverage"
        namespace = "http://www.opengis.net/gml"
