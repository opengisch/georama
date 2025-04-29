from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.description import Description
from georama.maps.interfaces.opengis.gml_3_2_1.description_reference import (
    DescriptionReference,
)
from georama.maps.interfaces.opengis.gml_3_2_1.identifier import Identifier
from georama.maps.interfaces.opengis.gml_3_2_1.meta_data_property import (
    MetaDataProperty,
)
from georama.maps.interfaces.opengis.gml_3_2_1.name import Name

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"

    meta_data_property: list[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    description_reference: Optional[DescriptionReference] = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    name: list[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
