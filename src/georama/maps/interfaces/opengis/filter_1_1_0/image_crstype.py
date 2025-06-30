from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_cartesian_cs import (
    UsesCartesianCs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_image_datum import UsesImageDatum
from georama.maps.interfaces.opengis.filter_1_1_0.uses_oblique_cartesian_cs import (
    UsesObliqueCartesianCs,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrstype(AbstractReferenceSystemType):
    """An engineering coordinate reference system applied to locations in images.

    Image coordinate reference systems are treated as a separate sub-
    type because a separate user community exists for images with its
    own terms of reference.
    """

    class Meta:
        name = "ImageCRSType"

    uses_cartesian_cs_or_uses_oblique_cartesian_cs: Optional[
        Union[UsesCartesianCs, UsesObliqueCartesianCs]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "usesCartesianCS",
                    "type": UsesCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "usesObliqueCartesianCS",
                    "type": UsesObliqueCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    uses_image_datum: Optional[UsesImageDatum] = field(
        default=None,
        metadata={
            "name": "usesImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
