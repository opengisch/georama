import inspect
import logging
from dataclasses import dataclass, field
from typing import List, Tuple

from georama.rasteroctopus.rasteroctopus_config import Config

log = logging.getLogger(__name__)


@dataclass
class QslMapJob:
    """Base class with common information for other map jobs"""

    BBOX: str = field(
        metadata={
            "name": "BBOX",
            "type": "Element",
            "required": True
        }
    )
    CRS: str = field(
        metadata={
            "name": "CRS",
            "type": "Element",
            "required": True
        }
    )
    WIDTH: str = field(
        metadata={
            "name": "WIDTH",
            "type": "Element",
            "required": True
        }
    )
    HEIGHT: str = field(
        metadata={
            "name": "HEIGHT",
            "type": "Element",
            "required": True
        }
    )
    # optional parameters
    DPI: str = field(
        default=None,
        metadata={
            "name": "DPI",
            "type": "Element",
            "required": False
        }
    )
    FORMAT_OPTIONS: str = field(
        default=None,
        metadata={
            "name": "FORMAT_OPTIONS",
            "type": "Element",
            "required": False
        }
    )
    STYLES: str = field(
        default_factory=list,
        metadata={
            "name": "STYLES",
            "type": "Element",
            "required": False
        }
    )

    @property
    def dpi(self) -> int | None:
        if self.DPI is not None:
            return int(self.DPI)
        elif self.FORMAT_OPTIONS is not None:
            return int(self.FORMAT_OPTIONS.split(":")[-1])
        else:
            return None

    @property
    def bbox(self) -> List[str]:
        return self.BBOX.split(',')

    @classmethod
    def from_overloaded_dict(cls, params: dict):
        return cls(**{
            k: v for k, v in params.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass(kw_only=True)
class QslRenderJob(QslMapJob):
    """A job to be rendered"""

    LAYERS: str = field(
        metadata={
            "name": "LAYERS",
            "type": "Element",
            "required": True
        }
    )

    # mime type of the requested image
    FORMAT: str = field(
        default="image/png",
        metadata={
            "name": "FORMAT",
            "type": "Element",
            "required": True
        }
    )

    @property
    def layers(self) -> List[str]:
        return self.LAYERS.split(',')


@dataclass(kw_only=True)
class QslFeatureInfoJob(QslMapJob):
    """Get feature info"""

    X: str = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "required": True
        }
    )
    Y: str = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "required": True
        }
    )
    I: str = field(
        default=None,
        metadata={
            "name": "I",
            "type": "Element",
            "required": True
        }
    )
    J: str = field(
        default=None,
        metadata={
            "name": "J",
            "type": "Element",
            "required": True
        }
    )
    INFO_FORMAT: str = field(
        metadata={
            "name": "INFO_FORMAT",
            "type": "Element",
            "required": True
        }
    )

    # mime type, only application/json supported
    QUERY_LAYERS: str = field(
        metadata={
            "name": "QUERY_LAYERS",
            "type": "Element",
            "required": True
        }
    )

    def __post_init__(self):
        x = int(self.I or self.X)
        y = int(self.J or self.Y)
        if x is None or y is None:
            raise KeyError(
                "Parameter `I` or `X` and `J` or `Y`  are mandatory for GetFeatureInfo"
            )
        if self.QUERY_LAYERS is None:
            raise KeyError("QUERY_LAYERS is mandatory in this request")

    @property
    def x(self) -> int:
        return int(self.I or self.X)

    @property
    def y(self) -> int:
        return int(self.J or self.Y)

    @property
    def query_layers(self):
        return self.QUERY_LAYERS.split(",")


@dataclass
class QslLegendJob(QslMapJob):
    """Render legend"""


def job_from_json(definition: dict):
    print(repr(definition))
    job_type = definition["type"]
    assert job_type
    if job_type == "QslRenderJob":
        return QslRenderJob(**definition["params"])
    if job_type == "QslFeatureInfoJob":
        return QslFeatureInfoJob(**definition["params"])
    else:
        raise RuntimeError(f"Job type {job_type} not supported")


class JobResult:
    def __init__(self, data, content_type: str) -> None:
        self.data = data
        self.content_type = content_type