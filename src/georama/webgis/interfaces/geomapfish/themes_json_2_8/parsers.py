from collections.abc import Iterable
from contextlib import suppress
from dataclasses import replace

from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.types import T

from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    WmsLayer,
    WmtsLayer,
)


class CustomDictDecoder(DictDecoder):
    def bind_best_dataclass(self, data: dict, classes: Iterable[type[T]]) -> T:
        """Bind the input data to all the given classes and return best match.

        Args:
            data: The derived element dictionary
            classes: The target class types to try

        Returns:
            An instance of one of the class types representing the parsed content.
        """
        obj = None
        keys = set(data.keys())
        max_score = -1.0
        config = replace(self.config, fail_on_converter_warnings=True)
        decoder = CustomDictDecoder(config=config, context=self.context)
        if (
            "dimensions" in keys
            and isinstance(data["dimensions"], dict)
            and len(data["dimensions"].keys()) == 0
        ):
            data["dimensions"] = None
        if "mixed" in keys and "children" in keys:
            return decoder.bind_dataclass(data, LayerGroup)
        if "type" in keys:
            if data["type"] == "WMS":
                return decoder.bind_dataclass(data, WmsLayer)
            elif data["type"] == "WMTS":
                return decoder.bind_dataclass(data, WmtsLayer)
        print(data)
        for clazz in classes:
            if not self.context.class_type.is_model(clazz):
                continue

            if self.context.local_names_match(keys, clazz):
                candidate = None
                with suppress(Exception):
                    candidate = decoder.bind_dataclass(data, clazz)

                score = self.context.class_type.score_object(candidate)
                if score > max_score:
                    max_score = score
                    obj = candidate
        if obj:
            return obj

        raise ParserError(
            f"Failed to bind object with properties({list(data.keys())}) "
            f"to any of the {[cls.__qualname__ for cls in classes]}"
        )
