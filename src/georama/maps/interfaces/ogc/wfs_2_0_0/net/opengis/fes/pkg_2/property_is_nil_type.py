from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.comparison_ops_type import (
    ComparisonOpsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.function_type import (
    Function,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.literal import Literal
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.value_reference import (
    ValueReference,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsNilType(ComparisonOpsType):
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    value_reference: Optional[ValueReference] = field(
        default=None,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
        },
    )
