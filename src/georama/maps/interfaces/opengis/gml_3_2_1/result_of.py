from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.result_type import ResultType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ResultOf(ResultType):
    class Meta:
        name = "resultOf"
        namespace = "http://www.opengis.net/gml/3.2"
