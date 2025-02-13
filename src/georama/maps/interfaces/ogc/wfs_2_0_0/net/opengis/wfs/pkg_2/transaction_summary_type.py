from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionSummaryType:
    total_inserted: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalInserted",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    total_updated: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalUpdated",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    total_replaced: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalReplaced",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    total_deleted: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalDeleted",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
