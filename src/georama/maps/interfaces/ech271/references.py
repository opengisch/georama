from dataclasses import dataclass, field


@dataclass
class Ref:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    ref: str | None = field(
        default=None,
        metadata={"type": "Attribute", "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS"},
    )


class BinBlBoxType(bytes):
    pass


class XmlBlBoxType(str):
    pass
