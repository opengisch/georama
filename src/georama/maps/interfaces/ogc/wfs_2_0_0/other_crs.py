from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class OtherCrs:
    class Meta:
        global_type = False

    value: str | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
