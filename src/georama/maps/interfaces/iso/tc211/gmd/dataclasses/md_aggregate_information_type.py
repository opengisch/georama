from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ds_association_type_code_property_type import (
    DsAssociationTypeCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ds_initiative_type_code_property_type import (
    DsInitiativeTypeCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
    CiCitationPropertyType,
    MdIdentifierPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdAggregateInformationType(AbstractObjectType):
    """
    Encapsulates the dataset aggregation information.
    """

    class Meta:
        name = "MD_AggregateInformation_Type"

    aggregate_data_set_name: CiCitationPropertyType | None = field(
        default=None,
        metadata={
            "name": "aggregateDataSetName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    aggregate_data_set_identifier: MdIdentifierPropertyType | None = field(
        default=None,
        metadata={
            "name": "aggregateDataSetIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    association_type: DsAssociationTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "associationType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    initiative_type: DsInitiativeTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "initiativeType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
