from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_identifier_type import (
    CiCitationPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPortrayalCatalogueReferenceType(AbstractObjectType):
    """
    Information identifing the portrayal catalogue used.
    """

    class Meta:
        name = "MD_PortrayalCatalogueReference_Type"

    portrayal_catalogue_citation: list[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
