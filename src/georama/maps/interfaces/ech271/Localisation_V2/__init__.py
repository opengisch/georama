from dataclasses import dataclass, field
from typing import Any, Tuple

from georama.maps.interfaces.ech271.InternationalCodes_V2 import (
    LanguageCode_ISO639_1 as InternationalCodes_V2LanguageCode_ISO639_1,
)
from georama.maps.interfaces.ech271.references import BinBlBoxType, XmlBlBoxType

VERSION = None
ILI_VERSION = "2.4"

metadata: dict = {
    "interlis": {
        "meta_attributes": {
            "furtherInformation": "https://www.geo.admin.ch/de/geoinformation-schweiz/geobasisdaten/geodata-models.html",
            "technicalContact": "mailto:models@geo.admin.ch",
        }
    }
}


@dataclass
class LocalisedText:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    Language: "InternationalCodes_V2LanguageCode_ISO639_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Language",
            "interlis": {
                "oid": "Localisation_V2.LocalisedText.Language",
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
    Text: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Text",
            "interlis": {
                "oid": "Localisation_V2.LocalisedText.Text",
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
                "oid": "Localisation_V2.LocalisedText",
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
class LocalisedMText:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    Language: "InternationalCodes_V2LanguageCode_ISO639_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Language",
            "interlis": {
                "oid": "Localisation_V2.LocalisedMText.Language",
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
    Text: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Text",
            "interlis": {
                "oid": "Localisation_V2.LocalisedMText.Text",
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
                "oid": "Localisation_V2.LocalisedMText",
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
class LocalisedUri:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    Language: "InternationalCodes_V2LanguageCode_ISO639_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Language",
            "interlis": {
                "oid": "Localisation_V2.LocalisedUri.Language",
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
    Text: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Text",
            "interlis": {
                "oid": "Localisation_V2.LocalisedUri.Text",
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
                    "max_length": 1023,
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
                "oid": "Localisation_V2.LocalisedUri",
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
class MultilingualText:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    @dataclass
    class MultilingualTextLocalisedTextStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[LocalisedText]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "LocalisedText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.LocalisedText",
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
                    "oid": "Localisation_V2.MultilingualText.LocalisedText.TYPE",
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

    LocalisedText: "list[MultilingualTextLocalisedTextStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "LocalisedText",
            "interlis": {
                "oid": "Localisation_V2.MultilingualText.LocalisedText",
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
                    "multiplicity": {"min": 1, "max": None},
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
                "oid": "Localisation_V2.MultilingualText",
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
        return [
            {
                "id": "Localisation_V2.MultilingualText.Constraint1",
                "name": "Constraint1",
                "documentation": [],
                "to_class": "Localisation_V2.MultilingualText",
                "to_domain": None,
                "kind": "LocalU",
                "unique_def": [
                    {
                        "path_els": [
                            {
                                "kind": "Attribute",
                                "ref": "Localisation_V2.MultilingualText.LocalisedText",
                                "num_index": None,
                                "spec_index": None,
                            }
                        ],
                        "inspection": None,
                    }
                ],
                "where": None,
            }
        ]

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
class MultilingualMText:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    @dataclass
    class MultilingualMTextLocalisedTextStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[LocalisedMText]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "LocalisedMText",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.LocalisedMText",
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
                    "oid": "Localisation_V2.MultilingualMText.LocalisedText.TYPE",
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

    LocalisedText: "list[MultilingualMTextLocalisedTextStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "LocalisedText",
            "interlis": {
                "oid": "Localisation_V2.MultilingualMText.LocalisedText",
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
                    "multiplicity": {"min": 1, "max": None},
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
                "oid": "Localisation_V2.MultilingualMText",
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
        return [
            {
                "id": "Localisation_V2.MultilingualMText.Constraint1",
                "name": "Constraint1",
                "documentation": [],
                "to_class": "Localisation_V2.MultilingualMText",
                "to_domain": None,
                "kind": "LocalU",
                "unique_def": [
                    {
                        "path_els": [
                            {
                                "kind": "Attribute",
                                "ref": "Localisation_V2.MultilingualMText.LocalisedText",
                                "num_index": None,
                                "spec_index": None,
                            }
                        ],
                        "inspection": None,
                    }
                ],
                "where": None,
            }
        ]

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
class MultilingualUri:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    @dataclass
    class MultilingualUriLocalisedTextStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[LocalisedUri]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "LocalisedUri",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.LocalisedUri",
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
                    "oid": "Localisation_V2.MultilingualUri.LocalisedText.TYPE",
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

    LocalisedText: "list[MultilingualUriLocalisedTextStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "LocalisedText",
            "interlis": {
                "oid": "Localisation_V2.MultilingualUri.LocalisedText",
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
                    "multiplicity": {"min": 1, "max": None},
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
                "oid": "Localisation_V2.MultilingualUri",
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
        return [
            {
                "id": "Localisation_V2.MultilingualUri.Constraint1",
                "name": "Constraint1",
                "documentation": [],
                "to_class": "Localisation_V2.MultilingualUri",
                "to_domain": None,
                "kind": "LocalU",
                "unique_def": [
                    {
                        "path_els": [
                            {
                                "kind": "Attribute",
                                "ref": "Localisation_V2.MultilingualUri.LocalisedText",
                                "num_index": None,
                                "spec_index": None,
                            }
                        ],
                        "inspection": None,
                    }
                ],
                "where": None,
            }
        ]

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
class LocalisedBlob:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    Language: "InternationalCodes_V2LanguageCode_ISO639_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Language",
            "interlis": {
                "oid": "Localisation_V2.LocalisedBlob.Language",
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
    Content: "BinBlBoxType | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Content",
            "interlis": {
                "oid": "Localisation_V2.LocalisedBlob.Content",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": "Binary",
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
                "oid": "Localisation_V2.LocalisedBlob",
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
class MultilingualBlob:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    @dataclass
    class MultilingualBlobLocalisedBlobStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[LocalisedBlob]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "LocalisedBlob",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.LocalisedBlob",
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
                    "oid": "Localisation_V2.MultilingualBlob.LocalisedBlob.TYPE",
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

    LocalisedBlob: "list[MultilingualBlobLocalisedBlobStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "LocalisedBlob",
            "interlis": {
                "oid": "Localisation_V2.MultilingualBlob.LocalisedBlob",
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
                    "multiplicity": {"min": 1, "max": None},
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
                "oid": "Localisation_V2.MultilingualBlob",
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
class LocalisedXML:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    Language: "InternationalCodes_V2LanguageCode_ISO639_1 | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Language",
            "interlis": {
                "oid": "Localisation_V2.LocalisedXML.Language",
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
    Content: "XmlBlBoxType | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "Content",
            "interlis": {
                "oid": "Localisation_V2.LocalisedXML.Content",
                "meta_attributes": {},
                "type_restrictions": {
                    "mandatory": False,
                    "kind": "Xml",
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
                "oid": "Localisation_V2.LocalisedXML",
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
class MultilingualXML:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

    @dataclass
    class MultilingualXMLLocalisedXMLStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/Localisation_V2"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[LocalisedXML]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
                "name": "LocalisedXML",
                "interlis": {
                    "oid": "ili2py.Localisation_V2.LocalisedXML",
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
                    "oid": "Localisation_V2.MultilingualXML.LocalisedXML.TYPE",
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

    LocalisedXML: "list[MultilingualXMLLocalisedXMLStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Localisation_V2",
            "name": "LocalisedXML",
            "interlis": {
                "oid": "Localisation_V2.MultilingualXML.LocalisedXML",
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
                    "multiplicity": {"min": 1, "max": None},
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
                "oid": "Localisation_V2.MultilingualXML",
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
