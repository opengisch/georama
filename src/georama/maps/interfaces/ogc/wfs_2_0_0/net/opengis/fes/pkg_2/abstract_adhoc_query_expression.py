from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.abstract_adhoc_query_expression_type import (
    AbstractAdhocQueryExpressionType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractAdhocQueryExpression(AbstractAdhocQueryExpressionType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
