from dataclasses import dataclass, field

from mypy.nodes import Enum


@dataclass
class Link:
    type: str = field()
    rel: str = field()
    title: str = field()
    href: str = field()
    href_lang: str | None = field(default=None, metadata={"name": "hreflang"})


@dataclass
class Base:
    links: list[Link] = field()


class Input:
    pass


class Output:
    pass


class Subscriber:
    pass


class JobControlOptions(str, Enum):
    SYNC = "sync-execute"
    ASYNC = "async-execute"
    DISMISS = "dismiss"


class TransmissionMode(str, Enum):
    VALUE = "value"
    REFERENCE = "reference"


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


@dataclass
class Process(ProcessBase):
    inputs: list[Input] | Input = field()

    outputs: list[Output] = field()

    response: str = field()
    subscriber: Subscriber = field()


@dataclass
class Landing(Base):
    processes: list[ProcessBase] = field()
