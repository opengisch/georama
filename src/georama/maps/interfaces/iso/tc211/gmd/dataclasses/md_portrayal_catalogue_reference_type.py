from dataclasses import dataclass, field
from typing import List

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
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

    portrayal_catalogue_citation: List[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
