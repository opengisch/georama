from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coverage_mapping_rule import (
    CoverageMappingRule,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_function import GridFunction
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.mapping_rule import MappingRule

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageFunctionType:
    mapping_rule: MappingRule | None = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_mapping_rule: CoverageMappingRule | None = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_function: GridFunction | None = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
