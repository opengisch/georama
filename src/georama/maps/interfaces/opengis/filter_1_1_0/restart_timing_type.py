from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


class RestartTimingType(Enum):
    NEVER = "never"
    ALWAYS = "always"
    WHEN_NOT_ACTIVE = "whenNotActive"
    DEFAULT = "default"
