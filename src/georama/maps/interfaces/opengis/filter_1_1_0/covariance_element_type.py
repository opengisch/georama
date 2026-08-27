from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.column_index import ColumnIndex
from georama.maps.interfaces.opengis.filter_1_1_0.covariance import Covariance
from georama.maps.interfaces.opengis.filter_1_1_0.row_index import RowIndex

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CovarianceElementType:
    """
    An element of a covariance matrix.
    """

    row_index: RowIndex | None = field(
        default=None,
        metadata={
            "name": "rowIndex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    column_index: ColumnIndex | None = field(
        default=None,
        metadata={
            "name": "columnIndex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    covariance: Covariance | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
