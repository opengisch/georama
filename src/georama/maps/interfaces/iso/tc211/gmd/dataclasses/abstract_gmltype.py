from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.description import Description
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.description_reference import (
    DescriptionReference,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identifier import Identifier
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.meta_data_property import (
    MetaDataProperty,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.name import Name

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"

    meta_data_property: list[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    description_reference: DescriptionReference | None = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    identifier: Identifier | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    name: list[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
