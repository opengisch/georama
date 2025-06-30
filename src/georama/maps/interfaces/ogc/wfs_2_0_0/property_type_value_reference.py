from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.update_action_type import UpdateActionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class PropertyTypeValueReference:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    action: UpdateActionType = field(
        default=UpdateActionType.REPLACE,
        metadata={
            "type": "Attribute",
        },
    )
