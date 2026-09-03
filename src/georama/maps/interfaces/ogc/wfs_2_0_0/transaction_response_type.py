from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.action_results_type import ActionResultsType
from georama.maps.interfaces.ogc.wfs_2_0_0.transaction_summary_type import (
    TransactionSummaryType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionResponseType:
    transaction_summary: TransactionSummaryType | None = field(
        default=None,
        metadata={
            "name": "TransactionSummary",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
        },
    )
    insert_results: ActionResultsType | None = field(
        default=None,
        metadata={
            "name": "InsertResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    update_results: ActionResultsType | None = field(
        default=None,
        metadata={
            "name": "UpdateResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    replace_results: ActionResultsType | None = field(
        default=None,
        metadata={
            "name": "ReplaceResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"2\.0\.\d+",
        },
    )
