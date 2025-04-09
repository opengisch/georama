from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.action_results_type import (
    ActionResultsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.transaction_summary_type import (
    TransactionSummaryType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionResponseType:
    transaction_summary: Optional[TransactionSummaryType] = field(
        default=None,
        metadata={
            "name": "TransactionSummary",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
        },
    )
    insert_results: Optional[ActionResultsType] = field(
        default=None,
        metadata={
            "name": "InsertResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    update_results: Optional[ActionResultsType] = field(
        default=None,
        metadata={
            "name": "UpdateResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    replace_results: Optional[ActionResultsType] = field(
        default=None,
        metadata={
            "name": "ReplaceResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"2\.0\.\d+",
        },
    )
