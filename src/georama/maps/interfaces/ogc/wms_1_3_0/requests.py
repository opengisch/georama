from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ServiceType(Enum):
    wms = "WMS"


class RequestType(Enum):
    get_map = "GETMAP"
    get_feature_info = "GETFEATUREINFO"
    get_legend = "GETLEGEND"


class Version(Enum):
    v_1_0_0 = "1.0.0"
    v_1_1_0 = "1.1.0"
    v_1_3_0 = "1.3.0"


@dataclass
class AbstractRequest:
    service: "ServiceType"
    request: "RequestType"
    version: "Version"


@dataclass
class AbstractGetMapRequest(AbstractRequest):
    layers: list[str]
    bbox: list[float]
    crs: str
    width: int
    height: int
    format: str
    transparent: Optional[bool] = True
    styles: Optional[str] = ""
    dpi: Optional[int] = None


@dataclass
class QslGetMapRequest(AbstractGetMapRequest):
    map_resolution: Optional[int] = None
    format_options: Optional[str] = None
