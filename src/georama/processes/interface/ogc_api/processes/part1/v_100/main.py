from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum

from qgis_server_light.interface.job.process.description import (
    InputDescription,
    OutputDescription,
)


@dataclass
class Link:
    href: str = field()
    type: str | None = field(default=None)
    rel: str | None = field(default=None)
    title: str | None = field(default=None)
    href_lang: str | None = field(default=None, metadata={"name": "hreflang"})


@dataclass
class Base:
    links: list[Link] = field()


class JobControlOptions(StrEnum):
    SYNC = "sync-execute"
    ASYNC = "async-execute"
    DISMISS = "dismiss"


class TransmissionMode(StrEnum):
    VALUE = "value"
    REFERENCE = "reference"


@dataclass
class ProcessBase(Base):
    description: str | None = field()
    id: str = field()
    job_control_options: list[JobControlOptions] = field(metadata={"name": "jobControlOptions"})
    output_transmission: list[TransmissionMode] = field(metadata={"name": "outputTransmission"})
    title: str = field()
    version: str = field()


@dataclass
class ProcessDetail(ProcessBase):
    inputs: list[InputDescription] = field()
    outputs: list[OutputDescription] = field()


@dataclass
class Processes(Base):
    processes: list[ProcessBase] = field()


@dataclass
class Landing(Base):
    title: str = field()
    description: str = field()


@dataclass
class Conformance:
    conforms_to: list[str] = field(
        metadata={
            "name": "conformsTo",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Job(Base):
    type: str = field()
    job_id: str = field(metadata={"name": "jobId"})
    process_id: str = field(metadata={"name": "processId"})
    status: str = field()
    message: str = field()
    progress: int = field()
    created: datetime = field(metadata={"format": "%Y-%m-%dT%H:%M:%S.%f%:z"})
    started: datetime = field(metadata={"format": "%Y-%m-%dT%H:%M:%S.%f%:z"})
    finished: datetime = field(metadata={"format": "%Y-%m-%dT%H:%M:%S.%f%:z"})
    updated: datetime = field(metadata={"format": "%Y-%m-%dT%H:%M:%S.%f%:z"})


@dataclass
class Jobs(Base):
    jobs: list[Job] = field()
