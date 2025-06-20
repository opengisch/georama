from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_positional_accuracy_type import (
    AbstractPositionalAccuracyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.includes_element import (
    IncludesElement,
)
from georama.maps.interfaces.opengis.filter_1_1_0.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CovarianceMatrixType(AbstractPositionalAccuracyType):
    """
    Error estimate covariance matrix.

    :ivar unit_of_measure: Ordered sequence of units of measure,
        corresponding to the row and column index numbers of the
        covariance matrix, starting with row and column 1 and ending
        with row/column N. Each unit of measure is for the ordinate
        reflected in the relevant row and column of the covariance
        matrix.
    :ivar includes_element: Unordered set of elements in this covariance
        matrix. Because the covariance matrix is symmetrical, only the
        elements in the upper or lower diagonal part (including the main
        diagonal) of the matrix need to be specified. Any zero valued
        covariance elements can be omitted.
    """

    unit_of_measure: list[UnitOfMeasure] = field(
        default_factory=list,
        metadata={
            "name": "unitOfMeasure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    includes_element: list[IncludesElement] = field(
        default_factory=list,
        metadata={
            "name": "includesElement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
