from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, StrEnum
from typing import Any, TypeAlias

from pydantic.dataclasses import dataclass as pydantic_dataclass


@pydantic_dataclass
@dataclass
class Link:
    href: str = field()
    type: str | None = field(default=None)
    rel: str | None = field(default=None)
    title: str | None = field(default=None)
    href_lang: str | None = field(default=None, metadata={"name": "hreflang"})


@pydantic_dataclass
@dataclass
class Base:
    links: list[Link] = field()


class Response(Enum):
    raw = "raw"
    document = "document"


class JobControlOptions(StrEnum):
    SYNC = "sync-execute"
    ASYNC = "async-execute"
    DISMISS = "dismiss"


class TransmissionMode(StrEnum):
    VALUE = "value"
    REFERENCE = "reference"


class Crs(Enum):
    http___www_opengis_net_def_crs_OGC_1_3_CRS84 = (
        "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    )
    http___www_opengis_net_def_crs_OGC_0_CRS84h = "http://www.opengis.net/def/crs/OGC/0/CRS84h"


@pydantic_dataclass
@dataclass
class Input:
    pass


@pydantic_dataclass
@dataclass
class Bbox:
    bbox: list[float] = field()
    crs: str | None = field(default=Crs.http___www_opengis_net_def_crs_OGC_1_3_CRS84)


BinaryInputValue: TypeAlias = str


@pydantic_dataclass
@dataclass
class InputNoObject(Input):
    value: str | float | int | bool | list[Any] | BinaryInputValue | Bbox | dict[str, Any] = (
        field()
    )


@pydantic_dataclass
@dataclass
class Format:
    media_type: str | None = field(default=None, metadata={"name": "mediaType"})
    encoding: str | None = field(default=None)
    schema: str | dict[str, Any] | None = field(default=None)


@pydantic_dataclass
@dataclass
class Output:
    format: Format | None = field(default=None)
    transmission_mode: TransmissionMode = field(
        default=TransmissionMode.VALUE, metadata={"name": "transmissionMode"}
    )


@pydantic_dataclass
@dataclass
class Subscriber:
    success_uri: str | None = field(metadata={"name": "successUri"})
    in_progress_uri: str | None = field(metadata={"name": "inProgressUri"})
    failed_uri: str | None = field(metadata={"name": "failedUri"})


@pydantic_dataclass
@dataclass
class ProcessBase(Base):
    description: str = field()
    id: str = field()
    job_control_options: list[JobControlOptions] = field(
        metadata={"name": "jobControlOptions"}
    )
    output_transmission: list[TransmissionMode] = field(
        metadata={"name": "outputTransmission"}
    )
    title: str = field()
    version: str = field()


@pydantic_dataclass
@dataclass
class Process(ProcessBase):
    inputs: list[Input] | Input = field()
    outputs: list[Output] = field()
    subscriber: Subscriber | None = field(default=None)
    response: str = field(default=Response.raw)


@pydantic_dataclass
@dataclass
class Processes(Base):
    processes: list[ProcessBase] = field()


@pydantic_dataclass
@dataclass
class Landing(Base):
    title: str = field()
    description: str = field()


@pydantic_dataclass
@dataclass
class Conformance:
    conforms_to: list[str] = field(
        metadata={
            "name": "conformsTo",
            "type": "Attribute",
            "tokens": True,
        }
    )


@pydantic_dataclass
@dataclass
class Job(Base):
    type: str = field()
    job_id: str = field(metadata={"name": "jobId"})
    process_id: str = field(metadata={"name": "processId"})
    status: str = field()
    message: str = field()
    progress: int = field()
    created: datetime = field()
    started: datetime = field()
    finished: datetime = field()
    updated: datetime = field()


@pydantic_dataclass
@dataclass
class Jobs(Base):
    jobs: list[Job] = field()
