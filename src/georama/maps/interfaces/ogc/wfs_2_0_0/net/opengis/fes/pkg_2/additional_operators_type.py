from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.fes.pkg_2.extension_operator_type import (
    ExtensionOperatorType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AdditionalOperatorsType:
    operator: list[ExtensionOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
