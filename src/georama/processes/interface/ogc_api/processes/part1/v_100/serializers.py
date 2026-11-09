from collections.abc import Callable
from dataclasses import dataclass, field

from xsdata.formats.dataclass.serializers import DictEncoder
from xsdata.formats.dataclass.serializers.dict import DictFactory


@dataclass
class OgcApiDictEncoder(DictEncoder):
    """An encoder for the OGC API - Processes documents. Optional values which are not
    set are left out instead of being written as `null`, the specification types them
    without `null`.
    """

    dict_factory: Callable = field(default=DictFactory.FILTER_NONE)
