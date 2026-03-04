from dataclasses import dataclass, field
from typing import Any, Tuple, Union

from georama.maps.interfaces.ech271 import INTERLIS

metadata: dict = {"interlis": {"meta_attributes": {}}}


@dataclass
class CALENDAR(INTERLIS.SCALSYSTEM):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    Unit: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Unit",
            "interlis": {
                "oid": "INTERLIS.TIMESYSTEMS.CALENDAR.Unit",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.TIME",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": "INTERLIS.SCALSYSTEM.Unit.TYPE",
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.TIMESYSTEMS.CALENDAR",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class TIMEOFDAYSYS(INTERLIS.SCALSYSTEM):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    Unit: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Unit",
            "interlis": {
                "oid": "INTERLIS.TIMESYSTEMS.TIMEOFDAYSYS.Unit",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.TIME",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": "INTERLIS.SCALSYSTEM.Unit.TYPE",
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": False,
                "multi": False,
                "point_like": False,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.TIMESYSTEMS.TIMEOFDAYSYS",
                "kind": "Class",
                "meta_attributes": {},
            }
        }

    @property
    def existence_constraints(self) -> list:
        """
        Delivers the existence constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def set_constraints(self) -> list:
        """
        Delivers the set constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def simple_constraints(self) -> list:
        """
        Delivers the simple constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def unique_constraints(self) -> list:
        """
        Delivers the unique constraints applying to this object.

        Returns:
            The list of constraints as dict. They can be deserialized with the
            corresponding classes.
        """
        return []

    @property
    def geom_point_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for point like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_line_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for line like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_polygon_like_attribute_values(self) -> list[Tuple[str, Any]]:
        """
        Gives back a list of tuples which contain the name of the attribute and
        the corresponding value for polygon like geometries.

        Returns:
            Tuple, first element is the attribute name, second the geometry value.
        """
        return []

    @property
    def geom_attributes(self) -> list[str]:
        """
        Delivers a list of attributes names which contain geometric information.

        Returns:
            The list of geometry attribute names. Empty list when no geometry attributes at this class.
        """
        return []


@dataclass
class TIMESYSTEMSTOPIC:
    class Meta:
        name = "TIMESYSTEMS"

    elements: list[
        Union[
            CALENDAR,
            TIMEOFDAYSYS,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CALENDAR",
                    "type": CALENDAR,
                    "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                },
                {
                    "name": "TIMEOFDAYSYS",
                    "type": TIMEOFDAYSYS,
                    "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                },
            ),
        },
    )
    bid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
    kind: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
        },
    )
