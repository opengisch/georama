from dataclasses import dataclass, field
from enum import StrEnum

from pydantic.dataclasses import dataclass as pydantic_dataclass


@pydantic_dataclass
@dataclass
class Link:
    type: str = field()
    rel: str = field()
    title: str = field()
    href: str = field()
    href_lang: str | None = field(default=None, metadata={"name": "hreflang"})


@pydantic_dataclass
@dataclass
class Base:
    links: list[Link] = field()


@pydantic_dataclass
@dataclass
class Input:
    pass


@pydantic_dataclass
@dataclass
class Output:
    pass


@pydantic_dataclass
@dataclass
class Subscriber:
    pass


class JobControlOptions(StrEnum):
    SYNC = "sync-execute"
    ASYNC = "async-execute"
    DISMISS = "dismiss"


class TransmissionMode(StrEnum):
    VALUE = "value"
    REFERENCE = "reference"


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
    response: str = field()
    subscriber: Subscriber = field()


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
