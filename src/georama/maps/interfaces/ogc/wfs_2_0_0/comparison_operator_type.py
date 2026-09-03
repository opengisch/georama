from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.comparison_operator_name_type_value import (
    ComparisonOperatorNameTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ComparisonOperatorType:
    name: str | ComparisonOperatorNameTypeValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"extension:\w{2,}",
        },
    )
