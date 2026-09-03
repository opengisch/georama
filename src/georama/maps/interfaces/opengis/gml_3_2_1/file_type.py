from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.code_type import CodeType
from georama.maps.interfaces.opengis.gml_3_2_1.range_parameters import RangeParameters

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class FileType:
    range_parameters: RangeParameters | None = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    file_name: str | None = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    file_reference: str | None = field(
        default=None,
        metadata={
            "name": "fileReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    file_structure: CodeType | None = field(
        default=None,
        metadata={
            "name": "fileStructure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    mime_type: str | None = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    compression: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
