from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.covariance_element_type import (
    CovarianceElementType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IncludesElement(CovarianceElementType):
    class Meta:
        name = "includesElement"
        namespace = "http://www.opengis.net/gml"
