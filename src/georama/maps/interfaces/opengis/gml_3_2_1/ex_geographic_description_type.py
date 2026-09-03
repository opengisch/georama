from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_ex_geographic_extent_type import (
    AbstractExGeographicExtentType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_identifier_type import (
    MdIdentifierPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicDescriptionType(AbstractExGeographicExtentType):
    class Meta:
        name = "EX_GeographicDescription_Type"

    geographic_identifier: MdIdentifierPropertyType | None = field(
        default=None,
        metadata={
            "name": "geographicIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
