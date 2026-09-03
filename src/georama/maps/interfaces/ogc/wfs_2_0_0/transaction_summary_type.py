from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionSummaryType:
    total_inserted: int | None = field(
        default=None,
        metadata={
            "name": "totalInserted",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    total_updated: int | None = field(
        default=None,
        metadata={
            "name": "totalUpdated",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    total_replaced: int | None = field(
        default=None,
        metadata={
            "name": "totalReplaced",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    total_deleted: int | None = field(
        default=None,
        metadata={
            "name": "totalDeleted",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
