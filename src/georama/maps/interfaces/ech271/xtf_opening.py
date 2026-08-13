from dataclasses import dataclass, field

from georama.maps.interfaces.ech271.Dictionaries_V2.Dictionaries import (
    DictionariesTOPIC as Dictionaries_V2_Dictionaries_DictionariesTOPIC,
)
from georama.maps.interfaces.ech271.DictionariesCH_V2.Dictionaries import (
    DictionariesTOPIC as DictionariesCH_V2_Dictionaries_DictionariesTOPIC,
)
from georama.maps.interfaces.ech271.eCH0271_1.eCH0271 import (
    eCH0271TOPIC as eCH0271_1_eCH0271_eCH0271TOPIC,
)
from georama.maps.interfaces.ech271.INTERLIS.TIMESYSTEMS import (
    TIMESYSTEMSTOPIC as INTERLIS_TIMESYSTEMS_TIMESYSTEMSTOPIC,
)


@dataclass
class DataSection:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    baskets: list[
        INTERLIS_TIMESYSTEMS_TIMESYSTEMSTOPIC
        | Dictionaries_V2_Dictionaries_DictionariesTOPIC
        | DictionariesCH_V2_Dictionaries_DictionariesTOPIC
        | eCH0271_1_eCH0271_eCH0271TOPIC
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TIMESYSTEMS",
                    "type": INTERLIS_TIMESYSTEMS_TIMESYSTEMSTOPIC,
                    "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                },
                {
                    "name": "Dictionaries",
                    "type": Dictionaries_V2_Dictionaries_DictionariesTOPIC,
                    "namespace": "http://www.interlis.ch/xtf/2.4/Dictionaries_V2",
                },
                {
                    "name": "Dictionaries",
                    "type": DictionariesCH_V2_Dictionaries_DictionariesTOPIC,
                    "namespace": "http://www.interlis.ch/xtf/2.4/DictionariesCH_V2",
                },
                {
                    "name": "eCH0271",
                    "type": eCH0271_1_eCH0271_eCH0271TOPIC,
                    "namespace": "http://www.interlis.ch/xtf/2.4/eCH0271_1",
                },
            ),
        },
    )

    @property
    def metadata(self) -> dict:
        return {"interlis": {"oid": "datasection", "kind": None, "meta_attributes": {}}}


@dataclass
class Model:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    name: str | None = field(default=None, metadata={"type": "Text"})

    @property
    def metadata(self) -> dict:
        return {"interlis": {"oid": "model", "kind": None, "meta_attributes": {}}}


@dataclass
class ModelsType:
    choice: list[Model] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "model",
                    "type": Model,
                    "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                },
            ),
        },
    )


@dataclass
class HeaderSection:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    models: ModelsType = field(
        metadata={
            "name": "models",
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        }
    )
    sender: str | None = field(
        default=None,
        metadata={"type": "Element", "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS"},
    )
    version: str | None = field(
        default=None,
        metadata={"type": "Element", "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS"},
    )
    comment: str | None = field(
        default=None,
        metadata={"type": "Element", "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS"},
    )

    @property
    def metadata(self) -> dict:
        return {"interlis": {"oid": "headersection", "kind": None, "meta_attributes": {}}}


@dataclass
class Transfer:
    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"
        name = "transfer"

    headersection: HeaderSection = field(
        metadata={"type": "Element", "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS"}
    )
    datasection: DataSection = field(
        metadata={"type": "Element", "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS"}
    )

    @property
    def metadata(self) -> dict:
        return {"interlis": {"oid": "transfer", "kind": None, "meta_attributes": {}}}
