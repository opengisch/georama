from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.transaction_type import TransactionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Transaction(TransactionType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
