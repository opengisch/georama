from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.serializers import DictEncoder
from xsdata.formats.dataclass.serializers.dict import DictFactory


@dataclass
class OgcApiDictEncoder(DictEncoder):
    """An encoder for the OGC API - Processes documents. Optional values which are not
    set are left out instead of being written as `null`, the specification types them
    without `null`.
    """

    dict_factory: Callable = field(default=DictFactory.FILTER_NONE)


@dataclass
class OgcApiProcessDetailDictEncoder(OgcApiDictEncoder):
    """An encoder for the process description. The specification holds inputs and outputs
    as map by id, xsdata can only write them as list (see
    `qgis_server_light.interface.job.process.description.InputDescription`). The encoder
    turns these lists into maps.
    """

    mapped_fields: tuple[str, ...] = ("inputs", "outputs")

    def encode(self, value: Any, var: XmlVar | None = None, wrapped: bool = False) -> Any:
        encoded = super().encode(value, var, wrapped)
        if var is not None:
            return encoded
        for mapped_field in self.mapped_fields:
            encoded[mapped_field] = {
                description.pop("id"): description for description in encoded[mapped_field]
            }
        return encoded
