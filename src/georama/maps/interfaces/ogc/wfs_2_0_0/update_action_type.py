from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


class UpdateActionType(Enum):
    REPLACE = "replace"
    INSERT_BEFORE = "insertBefore"
    INSERT_AFTER = "insertAfter"
    REMOVE = "remove"
