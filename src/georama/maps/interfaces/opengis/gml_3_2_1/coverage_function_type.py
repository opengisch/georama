from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.coverage_mapping_rule import (
    CoverageMappingRule,
)
from georama.maps.interfaces.opengis.gml_3_2_1.grid_function import GridFunction
from georama.maps.interfaces.opengis.gml_3_2_1.mapping_rule import MappingRule

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoverageFunctionType:
    mapping_rule: MappingRule | None = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coverage_mapping_rule: CoverageMappingRule | None = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_function: GridFunction | None = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
