from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_address_property_type import (
    CiAddressPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_online_resource_property_type import (
    CiOnlineResourcePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_telephone_property_type import (
    CiTelephonePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiContactType(AbstractObjectType):
    """
    Information required enabling contact with the  responsible person and/or
    organisation.
    """

    class Meta:
        name = "CI_Contact_Type"

    phone: CiTelephonePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    address: CiAddressPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    online_resource: CiOnlineResourcePropertyType | None = field(
        default=None,
        metadata={
            "name": "onlineResource",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    hours_of_service: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "hoursOfService",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    contact_instructions: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
