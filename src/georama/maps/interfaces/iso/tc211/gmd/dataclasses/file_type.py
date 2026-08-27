from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.file_value_model_type import (
    FileValueModelType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.range_parameters import (
    RangeParameters,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FileType:
    range_parameters: RangeParameters | None = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    file_name: str | None = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    file_reference: str | None = field(
        default=None,
        metadata={
            "name": "fileReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    file_structure: FileValueModelType | None = field(
        default=None,
        metadata={
            "name": "fileStructure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    mime_type: str | None = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compression: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
