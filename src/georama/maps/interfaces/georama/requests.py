"""This module is an interface to fill the missing specs for
WMS requests and their params.
"""

import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


def handle_list_encoding(parameter_value: str) -> List[str]:
    """
    Try to derive if the parameter_value is encoded as a list as it is defined in WFS 2.0
        => (param1,param2)(param3,param4)
    Args:
        parameter_value: The string which will be checked.
    Returns:
        The list of matches. With the example above this would be
            => ["param1,param2", "param3,param4"]
    """
    pattern = r"\((.+?)\)"
    matches = re.findall(pattern, parameter_value)
    if len(matches) == 0:
        # parameter value is not list encoded, we handle it as simple comma separated string
        return [parameter_value]
    else:
        return matches


class ServiceType(Enum):
    wms = "WMS"


class RequestType(Enum):
    get_map = "GETMAP"
    get_feature_info = "GETFEATUREINFO"
    get_legend = "GETLEGEND"


class Version(Enum):
    v_1_0_0 = "1.0.0"
    v_1_1_0 = "1.1.0"
    v_1_3_0 = "1.3.0"


@dataclass
class AbstractRequestParams:
    SERVICE: "ServiceType"
    REQUEST: "RequestType"
    VERSION: "Version"


@dataclass
class AbstractGetMapRequestParams(AbstractRequestParams):
    _default_style_name = "default"
    LAYERS: str = field(metadata={"type": "Element"})
    BBOX: str = field(metadata={"type": "Element"})
    CRS: str = field(metadata={"type": "Element"})
    WIDTH: int = field(metadata={"type": "Element"})
    HEIGHT: int = field(metadata={"type": "Element"})
    FORMAT: str = field(metadata={"type": "Element"})
    TRANSPARENT: Optional[bool] = field(default=True, metadata={"type": "Element"})
    STYLES: Optional[str] = field(default=None, metadata={"type": "Element"})
    DPI: Optional[int] = field(default=72, metadata={"type": "Element"})
    FILTER: Optional[str] = field(default=None, metadata={"type": "Element"})

    @property
    def layer_list(self) -> List[str]:
        return self.LAYERS.split(",")

    @property
    def bbox_list(self) -> List[float]:
        bbox_list = self.BBOX.split(",")
        return [float(part) for part in bbox_list[0:4]]

    @property
    def bbox_crs(self) -> Optional[str]:
        bbox_list = self.BBOX.split(",")
        try:
            bbox_crs = bbox_list[5]
        except IndexError:
            logging.info(
                f"There was no SRS definition in the BBOX parameter, we assume"
                f" it has the SRS of the request: {self.CRS}"
            )
            bbox_crs = self.CRS
        return bbox_crs

    @property
    def style_list(self) -> List[str]:
        if self.STYLES:
            logging.debug("There were styles in the request. Processing them further...")
            style_list = self.STYLES.split(",")
            self.validate_normalisation(style_list)
            logging.debug(f"Old list of styles was: {style_list}")
            style_list = self.apply_default_style(style_list)
            logging.debug(f"New list of styles is: {style_list}")
            return style_list
        else:
            logging.debug(
                "No styles were passed to the request, so we apply the default styles to all layers"
            )
            return [self._default_style_name] * len(self.layer_list)

    def apply_default_style(self, style_list: List[str]) -> List[str]:
        for index, style in enumerate(style_list):
            if style == "":
                style_list[index] = self._default_style_name
        return style_list

    @property
    def filter_list(self) -> List[str] | None:
        if self.FILTER:
            logging.debug("There were filters in the request. Processing them further...")
            filter_list = handle_list_encoding(self.FILTER)
            self.validate_normalisation(filter_list)
            return filter_list
        else:
            return None

    def validate_normalisation(self, compare_list: List[str]):
        if len(compare_list) != len(self.layer_list):
            logging.debug(
                "Length of layer list has to be same as compared list. That"
                f" is not the case: layer_list ({len(self.layer_list)}) != {len(compare_list)})"
                f"{self.layer_list} - {compare_list}"
                "We stop here."
            )
            raise ValueError(
                "Each passed layer needs a corresponding element in style or filter"
                "(comma separated lists need to be of same length)."
            )


@dataclass
class GetMapRequestParams(AbstractGetMapRequestParams):
    MAP_RESOLUTION: Optional[int] = None
    FORMAT_OPTIONS: Optional[str] = None
