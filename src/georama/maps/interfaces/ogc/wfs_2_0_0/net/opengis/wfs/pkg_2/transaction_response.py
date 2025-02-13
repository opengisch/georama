from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.transaction_response_type import (
    TransactionResponseType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionResponse(TransactionResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
