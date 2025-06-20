from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.absolute_external_positional_accuracy_type import (
    AbsoluteExternalPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbsoluteExternalPositionalAccuracy(AbsoluteExternalPositionalAccuracyType):
    class Meta:
        name = "absoluteExternalPositionalAccuracy"
        namespace = "http://www.opengis.net/gml"
