from dataclasses import dataclass, field

from mypy.nodes import Enum


@dataclass
class Base:
    links: list[str] = field()


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
class Process(Base):
    description: str = field()
    id: str = field()
    inputs: list[Input] | Input = field()
    jobControlOptions: JobControlOptions = field()
    outputs: list[Output] = field()
    outputTransmission: list[TransmissionMode] = field()
    response: str = field()
    subscriber: Subscriber = field()
    title: str = field()
    version: str = field()


@dataclass
class Landing(Base):
    processes: list[Process] = field()
