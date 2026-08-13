from abc import ABC
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Tuple, Union

metadata: dict = {"interlis": {"meta_attributes": {}}}


@dataclass
class Entry(ABC):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Dictionaries_V2"

    Text: "str | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Dictionaries_V2",
            "name": "Text",
            "interlis": {
                "oid": "Dictionaries_V2.Dictionaries.Entry.Text",
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
                "oid": "Dictionaries_V2.Dictionaries.Entry",
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
class Dictionary:

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/Dictionaries_V2"

    class DictionaryLanguageEnum(str, Enum):
        DE = "de"
        FR = "fr"
        IT = "it"
        RM = "rm"
        EN = "en"
        AA = "aa"
        AB = "ab"
        AF = "af"
        AM = "am"
        AR = "ar"
        AS = "as"
        AY = "ay"
        AZ = "az"
        BA = "ba"
        BE = "be"
        BG = "bg"
        BH = "bh"
        BI = "bi"
        BN = "bn"
        BO = "bo"
        BR = "br"
        CA = "ca"
        CO = "co"
        CS = "cs"
        CY = "cy"
        DA = "da"
        DZ = "dz"
        EL = "el"
        EO = "eo"
        ES = "es"
        ET = "et"
        EU = "eu"
        FA = "fa"
        FI = "fi"
        FJ = "fj"
        FO = "fo"
        FY = "fy"
        GA = "ga"
        GD = "gd"
        GL = "gl"
        GN = "gn"
        GU = "gu"
        HA = "ha"
        HE = "he"
        HI = "hi"
        HR = "hr"
        HU = "hu"
        HY = "hy"
        IA = "ia"
        ID = "id"
        IE = "ie"
        IK = "ik"
        IS = "is"
        IU = "iu"
        JA = "ja"
        JW = "jw"
        KA = "ka"
        KK = "kk"
        KL = "kl"
        KM = "km"
        KN = "kn"
        KO = "ko"
        KS = "ks"
        KU = "ku"
        KY = "ky"
        LA = "la"
        LN = "ln"
        LO = "lo"
        LT = "lt"
        LV = "lv"
        MG = "mg"
        MI = "mi"
        MK = "mk"
        ML = "ml"
        MN = "mn"
        MO = "mo"
        MR = "mr"
        MS = "ms"
        MT = "mt"
        MY = "my"
        NA = "na"
        NE = "ne"
        NL = "nl"
        NO = "no"
        OC = "oc"
        OM = "om"
        OR = "or"
        PA = "pa"
        PL = "pl"
        PS = "ps"
        PT = "pt"
        QU = "qu"
        RN = "rn"
        RO = "ro"
        RU = "ru"
        RW = "rw"
        SA = "sa"
        SD = "sd"
        SG = "sg"
        SH = "sh"
        SI = "si"
        SK = "sk"
        SL = "sl"
        SM = "sm"
        SN = "sn"
        SO = "so"
        SQ = "sq"
        SR = "sr"
        SS = "ss"
        ST = "st"
        SU = "su"
        SV = "sv"
        SW = "sw"
        TA = "ta"
        TE = "te"
        TG = "tg"
        TH = "th"
        TI = "ti"
        TK = "tk"
        TL = "tl"
        TN = "tn"
        TO = "to"
        TR = "tr"
        TS = "ts"
        TT = "tt"
        TW = "tw"
        UG = "ug"
        UK = "uk"
        UR = "ur"
        UZ = "uz"
        VI = "vi"
        VO = "vo"
        WO = "wo"
        XH = "xh"
        YI = "yi"
        YO = "yo"
        ZA = "za"
        ZH = "zh"
        ZU = "zu"

        @property
        def metadata(self) -> dict:
            return {
                "ili2py": {},
                "interlis": {
                    "oid": "Dictionaries_V2.Dictionaries.Dictionary.Language_ENUM",
                    "kind": "Enumeration",
                    "meta_attributes": {},
                },
            }

    @dataclass
    class DictionaryEntriesStruct:

        class Meta:
            namespace = "http://www.interlis.ch/xtf/2.4/Dictionaries_V2"

        """
        This Class is a HOP-Class to correctly parse XTF. It was inserted by ili2py

        Args:
            struct_content: This attribute is a HOP-Type to correctly parse XTF.
        """

        struct_content: "list[Entry]" = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.interlis.ch/xtf/2.4/Dictionaries_V2",
                "name": "Entry",
                "interlis": {
                    "oid": "ili2py.Dictionaries_V2.Dictionaries.Entry",
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
                    "oid": "Dictionaries_V2.Dictionaries.Dictionary.Entries.TYPE",
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

    Language: "DictionaryLanguageEnum | None" = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Dictionaries_V2",
            "name": "Language",
            "interlis": {
                "oid": "Dictionaries_V2.Dictionaries.Dictionary.Language",
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
                    "super": "InternationalCodes_V2.LanguageCode_ISO639_1",
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
    Entries: "list[DictionaryEntriesStruct]" = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.interlis.ch/xtf/2.4/Dictionaries_V2",
            "name": "Entries",
            "interlis": {
                "oid": "Dictionaries_V2.Dictionaries.Dictionary.Entries",
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
                "oid": "Dictionaries_V2.Dictionaries.Dictionary",
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
class DictionariesTOPIC:
    class Meta:
        name = "Dictionaries"

    elements: list[Union[Dictionary,]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Dictionary",
                    "type": Dictionary,
                    "namespace": "http://www.interlis.ch/xtf/2.4/Dictionaries_V2",
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
