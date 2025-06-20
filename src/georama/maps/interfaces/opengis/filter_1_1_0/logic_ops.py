from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.logic_ops_type import LogicOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class LogicOps(LogicOpsType):
    class Meta:
        name = "logicOps"
        namespace = "http://www.opengis.net/ogc"
