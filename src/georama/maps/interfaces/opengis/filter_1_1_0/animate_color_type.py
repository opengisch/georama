from dataclasses import dataclass, field
from decimal import Decimal

from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_prototype import (
    AnimateColorPrototype,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_type_calc_mode import (
    AnimateColorTypeCalcMode,
)
from georama.maps.interfaces.opengis.filter_1_1_0.fill_default_type import (
    FillDefaultType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.fill_timing_attrs_type import (
    FillTimingAttrsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.lang_value import LangValue
from georama.maps.interfaces.opengis.filter_1_1_0.restart_default_type import (
    RestartDefaultType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.restart_timing_type import (
    RestartTimingType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.sync_behavior_default_type import (
    SyncBehaviorDefaultType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.sync_behavior_type import (
    SyncBehaviorType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/Language"


@dataclass
class AnimateColorType(AnimateColorPrototype):
    class Meta:
        name = "animateColorType"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: str | None = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    alt: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    longdesc: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    begin: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    end: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dur: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    repeat_dur: str | None = field(
        default=None,
        metadata={
            "name": "repeatDur",
            "type": "Attribute",
        },
    )
    repeat_count: Decimal | None = field(
        default=None,
        metadata={
            "name": "repeatCount",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        },
    )
    repeat: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    min: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sync_behavior: SyncBehaviorType = field(
        default=SyncBehaviorType.DEFAULT,
        metadata={
            "name": "syncBehavior",
            "type": "Attribute",
        },
    )
    sync_tolerance: str | None = field(
        default=None,
        metadata={
            "name": "syncTolerance",
            "type": "Attribute",
        },
    )
    sync_behavior_default: SyncBehaviorDefaultType = field(
        default=SyncBehaviorDefaultType.INHERIT,
        metadata={
            "name": "syncBehaviorDefault",
            "type": "Attribute",
        },
    )
    sync_tolerance_default: str = field(
        default="inherit",
        metadata={
            "name": "syncToleranceDefault",
            "type": "Attribute",
        },
    )
    restart: RestartTimingType = field(
        default=RestartTimingType.DEFAULT,
        metadata={
            "type": "Attribute",
        },
    )
    restart_default: RestartDefaultType = field(
        default=RestartDefaultType.INHERIT,
        metadata={
            "name": "restartDefault",
            "type": "Attribute",
        },
    )
    fill: FillTimingAttrsType = field(
        default=FillTimingAttrsType.DEFAULT,
        metadata={
            "type": "Attribute",
        },
    )
    fill_default: FillDefaultType = field(
        default=FillDefaultType.INHERIT,
        metadata={
            "name": "fillDefault",
            "type": "Attribute",
        },
    )
    target_element: str | None = field(
        default=None,
        metadata={
            "name": "targetElement",
            "type": "Attribute",
        },
    )
    calc_mode: AnimateColorTypeCalcMode = field(
        default=AnimateColorTypeCalcMode.LINEAR,
        metadata={
            "name": "calcMode",
            "type": "Attribute",
        },
    )
    skip_content: bool = field(
        default=True,
        metadata={
            "name": "skip-content",
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
