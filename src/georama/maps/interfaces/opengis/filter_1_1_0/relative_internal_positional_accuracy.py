from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.relative_internal_positional_accuracy_type import (
    RelativeInternalPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RelativeInternalPositionalAccuracy(RelativeInternalPositionalAccuracyType):
    class Meta:
        name = "relativeInternalPositionalAccuracy"
        namespace = "http://www.opengis.net/gml"
