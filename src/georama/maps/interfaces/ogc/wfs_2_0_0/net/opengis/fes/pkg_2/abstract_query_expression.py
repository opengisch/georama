from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.abstract_query_expression_type import (
    AbstractQueryExpressionType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractQueryExpression(AbstractQueryExpressionType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
