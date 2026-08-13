from abc import ABC
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Tuple

VERSION = "20060126"
ILI_VERSION = "2.3"

metadata: dict = {"interlis": {"meta_attributes": {}}}


class URI(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.URI",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": True,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 1023,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class NAME(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.NAME",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": True,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 255,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class INTERLIS_1_DATE(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.INTERLIS_1_DATE",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": True,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 8,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class I32OID(int):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.I32OID",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 0,
                    "max": 2147483647,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class STANDARDOID(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.STANDARDOID",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 16,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class UUIDOID(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.UUIDOID",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "max_length": 36,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class GregorianYear(int):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.GregorianYear",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 1582,
                    "max": 2999,
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class XMLTime(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.XMLTime",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": '"Hours/2":"Minutes":"Seconds"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "struct": "INTERLIS.UTC",
                    "min": "0:0:0.000",
                    "max": "23:59:59.999",
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class XMLDate(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.XMLDate",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": '"Year"-"Month"-"Day"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "struct": "INTERLIS.GregorianDate",
                    "min": "1582-1-1",
                    "max": "2999-12-31",
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class XMLDateTime(str):

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.XMLDateTime",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": '"Year"-"Month"-"Day"T"Hours/2":"Minutes":"Seconds"',
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": None,
                    "super": "INTERLIS.XMLDate",
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "struct": "INTERLIS.GregorianDateTime",
                    "min": "1582-1-1T0:0:0.000",
                    "max": "2999-12-31T23:59:59.999",
                },
            }
        }

    @property
    def existence_constraints(self) -> list:
        return []

    @property
    def set_constraints(self) -> list:
        return []

    @property
    def simple_constraints(self) -> list:
        return []

    @property
    def unique_constraints(self) -> list:
        return []


class BOOLEAN(str, Enum):
    FALSE = "false"
    TRUE = "true"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "INTERLIS.BOOLEAN",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class HALIGNMENT(str, Enum):
    LEFT = "Left"
    CENTER = "Center"
    RIGHT = "Right"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "INTERLIS.HALIGNMENT",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


class VALIGNMENT(str, Enum):
    TOP = "Top"
    CAP = "Cap"
    HALF = "Half"
    BASE = "Base"
    BOTTOM = "Bottom"

    @property
    def metadata(self) -> dict:
        return {
            "ili2py": {},
            "interlis": {
                "oid": "INTERLIS.VALIGNMENT",
                "kind": "Enumeration",
                "meta_attributes": {},
            },
        }


@dataclass
class LineCoordType:

    c1: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
        },
    )
    c2: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
        },
    )


@dataclass
class LineCoord:
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    coord: LineCoordType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {},
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.LineCoord",
                "kind": "Enumeration",
                "meta_attributes": {},
            }
        }


@dataclass
class LineCoordARCType(LineCoordType):
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    """
    This is an intermediate class which simplifies parsing of XTF later.
    """
    a1: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )
    a2: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )
    r: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )


@dataclass
class LineCoordARC:
    class Meta:
        namespace = "http://www.interlis.ch/geometry/1.0"

    """
    This is an intermediate class which simplifies parsing of XTF later.
    """
    arc: LineCoordARCType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/geometry/1.0",
            "interlis": {"meta_attributes": {}, "type_restrictions": {}},
        },
    )


@dataclass
class ANYCLASS:

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

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {"oid": "INTERLIS.ANYCLASS", "kind": "Class", "meta_attributes": {}}
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
class ANYSTRUCTURE:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.ANYSTRUCTURE",
                "kind": "Structure",
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
class METAOBJECT(ABC):

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

    Name: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Name",
            "interlis": {
                "oid": "INTERLIS.METAOBJECT.Name",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 255,
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
            "interlis": {"oid": "INTERLIS.METAOBJECT", "kind": "Class", "meta_attributes": {}}
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
class METAOBJECT_TRANSLATION(ABC):

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

    Name: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Name",
            "interlis": {
                "oid": "INTERLIS.METAOBJECT_TRANSLATION.Name",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 255,
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
    NameInBaseLanguage: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "NameInBaseLanguage",
            "interlis": {
                "oid": "INTERLIS.METAOBJECT_TRANSLATION.NameInBaseLanguage",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                    "max_length": 255,
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
                "oid": "INTERLIS.METAOBJECT_TRANSLATION",
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
class AXIS:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    Unit: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Unit",
            "interlis": {
                "oid": "INTERLIS.AXIS.Unit",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.ANYUNIT",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": None,
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
            "interlis": {"oid": "INTERLIS.AXIS", "kind": "Structure", "meta_attributes": {}}
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
class REFSYSTEM(METAOBJECT):

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

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {"oid": "INTERLIS.REFSYSTEM", "kind": "Class", "meta_attributes": {}}
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
class COORDSYSTEM(REFSYSTEM):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @dataclass
    class COORDSYSTEMAxisStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[AXIS]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "name": "AXIS",
                "interlis": {
                    "oid": "ili2py.INTERLIS.AXIS",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
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
                    "oid": "INTERLIS.COORDSYSTEM.Axis.TYPE",
                    "kind": "None",
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

    tid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "tid",
            "interlis": {"meta_attributes": {}, "type_restrictions": None},
        },
    )

    Axis: "list[COORDSYSTEMAxisStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Axis",
            "interlis": {
                "oid": "INTERLIS.COORDSYSTEM.Axis",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 3},
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
            "interlis": {"oid": "INTERLIS.COORDSYSTEM", "kind": "Class", "meta_attributes": {}}
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
class SCALSYSTEM(REFSYSTEM):

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
                "oid": "INTERLIS.SCALSYSTEM.Unit",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.ANYUNIT",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": None,
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
            "interlis": {"oid": "INTERLIS.SCALSYSTEM", "kind": "Class", "meta_attributes": {}}
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
class SIGN(METAOBJECT):

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

    Sign: "Any | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Sign",
            "interlis": {
                "oid": "INTERLIS.SIGN.Sign",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
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
        return {"interlis": {"oid": "INTERLIS.SIGN", "kind": "Class", "meta_attributes": {}}}

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
class TimeOfDay(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    Hours: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Hours",
            "interlis": {
                "oid": "INTERLIS.TimeOfDay.Hours",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.h",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 0,
                    "max": 23,
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
    Minutes: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Minutes",
            "interlis": {
                "oid": "INTERLIS.TimeOfDay.Minutes",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.min",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 0,
                    "max": 59,
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
    Seconds: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Seconds",
            "interlis": {
                "oid": "INTERLIS.TimeOfDay.Seconds",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.s",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 3,
                    "min": 0.0,
                    "max": 59.999,
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
                "oid": "INTERLIS.TimeOfDay",
                "kind": "Structure",
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
class UTC(TimeOfDay):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {"oid": "INTERLIS.UTC", "kind": "Structure", "meta_attributes": {}}
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
class GregorianDate:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    Year: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Year",
            "interlis": {
                "oid": "INTERLIS.GregorianDate.Year",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 1582,
                    "max": 2999,
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
    Month: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Month",
            "interlis": {
                "oid": "INTERLIS.GregorianDate.Month",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.M",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 1,
                    "max": 12,
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
    Day: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Day",
            "interlis": {
                "oid": "INTERLIS.GregorianDate.Day",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.d",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": False,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 1,
                    "max": 31,
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
                "oid": "INTERLIS.GregorianDate",
                "kind": "Structure",
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
class GregorianDateTime(GregorianDate):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    Hours: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Hours",
            "interlis": {
                "oid": "INTERLIS.GregorianDateTime.Hours",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.h",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 0,
                    "max": 23,
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
    Minutes: "int | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Minutes",
            "interlis": {
                "oid": "INTERLIS.GregorianDateTime.Minutes",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.min",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "min": 0,
                    "max": 59,
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
    Seconds: "float | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Seconds",
            "interlis": {
                "oid": "INTERLIS.GregorianDateTime.Seconds",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": "INTERLIS.s",
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": True,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                    "precision": 3,
                    "min": 0.0,
                    "max": 59.999,
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
                "oid": "INTERLIS.GregorianDateTime",
                "kind": "Structure",
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
class LineSegment(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    SegmentEndPoint: "LineCoord | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "SegmentEndPoint",
            "interlis": {
                "oid": "INTERLIS.LineSegment.SegmentEndPoint",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": True,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": "INTERLIS.LineCoord",
                    "type_related_type": False,
                    "multiplicity": {"min": 1, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": True,
                "multi": False,
                "point_like": True,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.LineSegment",
                "kind": "Structure",
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
        return [("SegmentEndPoint", self.SegmentEndPoint)]

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
        return ["SegmentEndPoint"]


@dataclass
class StartSegment(LineSegment):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.StartSegment",
                "kind": "Structure",
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
class StraightSegment(LineSegment):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.StraightSegment",
                "kind": "Structure",
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
class ArcSegment(LineSegment):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.ArcSegment",
                "kind": "Structure",
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
class SurfaceEdge:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @dataclass
    class SurfaceEdgeGeometryLineType:
        class Meta:
            namespace = "http://www.interlis.ch/geometry/1.0"

        @dataclass
        class Segment:
            class Meta:
                namespace = "http://www.interlis.ch/geometry/1.0"

            vertices: "list[Any]" = field(
                default_factory=list,
                metadata={
                    "type": "Elements",
                    "choices": (
                        {
                            "name": "coord",
                            "type": Any,
                            "namespace": "http://www.interlis.ch/geometry/1.0",
                        },
                        {
                            "name": "arc",
                            "type": Any,
                            "namespace": "http://www.interlis.ch/geometry/1.0",
                        },
                    ),
                    "interlis": {"meta_attributes": {}},
                },
            )

        polyline: Segment | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/geometry/1.0",
                "interlis": {"meta_attributes": {}},
            },
        )

        @property
        def metadata(self) -> dict:
            return {
                "interlis": {
                    "oid": "INTERLIS.SurfaceEdge.Geometry.TYPE",
                    "kind": "LineType",
                    "meta_attributes": {},
                    "max_overlap": None,
                    "straights": False,
                    "arcs": False,
                }
            }

    @dataclass
    class SurfaceEdgeLineAttrsStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "ANYSTRUCTURE | None" = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "name": "ANYSTRUCTURE",
                "interlis": {
                    "oid": "ili2py.INTERLIS.ANYSTRUCTURE",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
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
                    "oid": "INTERLIS.SurfaceEdge.LineAttrs.TYPE",
                    "kind": "None",
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

    Geometry: "SurfaceEdgeGeometryLineType | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Geometry",
            "interlis": {
                "oid": "INTERLIS.SurfaceEdge.Geometry",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": True,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": 1},
                },
            },
            "geometric": {
                "is_geometric": True,
                "multi": False,
                "point_like": False,
                "line_like": True,
                "polygon_like": False,
            },
        },
    )
    LineAttrs: "SurfaceEdgeLineAttrsStruct | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "LineAttrs",
            "interlis": {
                "oid": "INTERLIS.SurfaceEdge.LineAttrs",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
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
                "oid": "INTERLIS.SurfaceEdge",
                "kind": "Structure",
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
        return [("Geometry", self.Geometry)]

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
        return ["Geometry"]


@dataclass
class SurfaceBoundary:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @dataclass
    class SurfaceBoundaryLinesStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[SurfaceEdge]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "name": "SurfaceEdge",
                "interlis": {
                    "oid": "ili2py.INTERLIS.SurfaceEdge",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
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
                    "oid": "INTERLIS.SurfaceBoundary.Lines.TYPE",
                    "kind": "None",
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

    Lines: "list[SurfaceBoundaryLinesStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Lines",
            "interlis": {
                "oid": "INTERLIS.SurfaceBoundary.Lines",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": True,
                "multi": True,
                "point_like": False,
                "line_like": True,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.SurfaceBoundary",
                "kind": "Structure",
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
        return [("Lines", self.Lines)]

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
        return ["Lines"]


@dataclass
class LineGeometry:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

    @dataclass
    class LineGeometrySegmentsStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/INTERLIS"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[LineSegment]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
                "name": "LineSegment",
                "interlis": {
                    "oid": "ili2py.INTERLIS.LineSegment",
                    "meta_attributes": {},
                    "type_restrictions": {"type_related_type": True},
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
                    "oid": "INTERLIS.LineGeometry.Segments.TYPE",
                    "kind": "None",
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

    Segments: "list[LineGeometrySegmentsStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/INTERLIS",
            "name": "Segments",
            "interlis": {
                "oid": "INTERLIS.LineGeometry.Segments",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": None,
                    "format": None,
                    "unit": None,
                    "ref_sys": None,
                    "clockwise": None,
                    "circular": None,
                    "abstract": False,
                    "final": False,
                    "generic": False,
                    "super": None,
                    "type_related_type": False,
                    "multiplicity": {"min": 0, "max": None},
                },
            },
            "geometric": {
                "is_geometric": True,
                "multi": True,
                "point_like": True,
                "line_like": False,
                "polygon_like": False,
            },
        },
    )

    @property
    def metadata(self) -> dict:
        return {
            "interlis": {
                "oid": "INTERLIS.LineGeometry",
                "kind": "Structure",
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
        return [("Segments", self.Segments)]

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
        return ["Segments"]
