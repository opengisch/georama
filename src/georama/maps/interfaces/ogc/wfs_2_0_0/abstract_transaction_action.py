from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class AbstractTransactionAction(AbstractTransactionActionType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
