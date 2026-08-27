from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.grid_function import GridFunction
from georama.maps.interfaces.opengis.filter_1_1_0.index_map import IndexMap
from georama.maps.interfaces.opengis.filter_1_1_0.mapping_rule import MappingRule

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageFunctionType:
    """The function or rule which defines the map from members of the domainSet to
    the range.

    More functions will be added to this list
    """

    mapping_rule_or_index_map_or_grid_function: (
        MappingRule | IndexMap | GridFunction | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MappingRule",
                    "type": MappingRule,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "IndexMap",
                    "type": IndexMap,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridFunction",
                    "type": GridFunction,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
