from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_topology_level_code import (
    MdTopologyLevelCode,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopologyLevelCodePropertyType:
    class Meta:
        name = "MD_TopologyLevelCode_PropertyType"

    md_topology_level_code: Optional[MdTopologyLevelCode] = field(
        default=None,
        metadata={
            "name": "MD_TopologyLevelCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
