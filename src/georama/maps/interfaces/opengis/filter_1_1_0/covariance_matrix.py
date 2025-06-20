from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.covariance_matrix_type import (
    CovarianceMatrixType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CovarianceMatrix(CovarianceMatrixType):
    class Meta:
        name = "covarianceMatrix"
        namespace = "http://www.opengis.net/gml"
