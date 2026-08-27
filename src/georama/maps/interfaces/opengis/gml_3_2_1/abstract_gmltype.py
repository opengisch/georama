from dataclasses import dataclass, field

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
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    description_reference: DescriptionReference | None = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    identifier: Identifier | None = field(
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
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
