from dataclasses import dataclass, field
from typing import Any, Tuple, Union

from georama.maps.interfaces.ech271.Dictionaries_V2.Dictionaries import (
    Dictionary as Dictionaries_V2_Dictionaries_Dictionary,
)

metadata: dict = {"interlis": {"meta_attributes": {}}}


@dataclass
class Dictionary(Dictionaries_V2_Dictionaries_Dictionary):

    class Meta:
        namespace = "http://www.interlis.ch/xtf/2.4/DictionariesCH_V2"

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
            "interlis": {
                "oid": "DictionariesCH_V2.Dictionaries.Dictionary",
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
        return [
            {
                "id": "DictionariesCH_V2.Dictionaries.Dictionary.Constraint1",
                "name": "Constraint1",
                "documentation": [],
                "to_class": "DictionariesCH_V2.Dictionaries.Dictionary",
                "to_domain": None,
                "kind": "MandC",
                "percentage": None,
                "logical_expression": {
                    "choice": {
                        "operation": "Or",
                        "sub_expressions": [
                            {
                                "choice": {
                                    "operation": "Or",
                                    "sub_expressions": [
                                        {
                                            "choice": {
                                                "operation": "Or",
                                                "sub_expressions": [
                                                    {
                                                        "choice": {
                                                            "operation": "Or",
                                                            "sub_expressions": [
                                                                {
                                                                    "choice": {
                                                                        "operation": "Relation.Equal",
                                                                        "sub_expressions": [
                                                                            {
                                                                                "choice": {
                                                                                    "path_els": [
                                                                                        {
                                                                                            "kind": "Attribute",
                                                                                            "ref": "Dictionaries_V2.Dictionaries.Dictionary.Language",
                                                                                            "num_index": None,
                                                                                            "spec_index": None,
                                                                                        }
                                                                                    ],
                                                                                    "inspection": None,
                                                                                }
                                                                            },
                                                                            {
                                                                                "choice": {
                                                                                    "value": "#de",
                                                                                    "type": "Enumeration",
                                                                                }
                                                                            },
                                                                        ],
                                                                    }
                                                                },
                                                                {
                                                                    "choice": {
                                                                        "operation": "Relation.Equal",
                                                                        "sub_expressions": [
                                                                            {
                                                                                "choice": {
                                                                                    "path_els": [
                                                                                        {
                                                                                            "kind": "Attribute",
                                                                                            "ref": "Dictionaries_V2.Dictionaries.Dictionary.Language",
                                                                                            "num_index": None,
                                                                                            "spec_index": None,
                                                                                        }
                                                                                    ],
                                                                                    "inspection": None,
                                                                                }
                                                                            },
                                                                            {
                                                                                "choice": {
                                                                                    "value": "#fr",
                                                                                    "type": "Enumeration",
                                                                                }
                                                                            },
                                                                        ],
                                                                    }
                                                                },
                                                            ],
                                                        }
                                                    },
                                                    {
                                                        "choice": {
                                                            "operation": "Relation.Equal",
                                                            "sub_expressions": [
                                                                {
                                                                    "choice": {
                                                                        "path_els": [
                                                                            {
                                                                                "kind": "Attribute",
                                                                                "ref": "Dictionaries_V2.Dictionaries.Dictionary.Language",
                                                                                "num_index": None,
                                                                                "spec_index": None,
                                                                            }
                                                                        ],
                                                                        "inspection": None,
                                                                    }
                                                                },
                                                                {
                                                                    "choice": {
                                                                        "value": "#it",
                                                                        "type": "Enumeration",
                                                                    }
                                                                },
                                                            ],
                                                        }
                                                    },
                                                ],
                                            }
                                        },
                                        {
                                            "choice": {
                                                "operation": "Relation.Equal",
                                                "sub_expressions": [
                                                    {
                                                        "choice": {
                                                            "path_els": [
                                                                {
                                                                    "kind": "Attribute",
                                                                    "ref": "Dictionaries_V2.Dictionaries.Dictionary.Language",
                                                                    "num_index": None,
                                                                    "spec_index": None,
                                                                }
                                                            ],
                                                            "inspection": None,
                                                        }
                                                    },
                                                    {
                                                        "choice": {
                                                            "value": "#rm",
                                                            "type": "Enumeration",
                                                        }
                                                    },
                                                ],
                                            }
                                        },
                                    ],
                                }
                            },
                            {
                                "choice": {
                                    "operation": "Relation.Equal",
                                    "sub_expressions": [
                                        {
                                            "choice": {
                                                "path_els": [
                                                    {
                                                        "kind": "Attribute",
                                                        "ref": "Dictionaries_V2.Dictionaries.Dictionary.Language",
                                                        "num_index": None,
                                                        "spec_index": None,
                                                    }
                                                ],
                                                "inspection": None,
                                            }
                                        },
                                        {"choice": {"value": "#en", "type": "Enumeration"}},
                                    ],
                                }
                            },
                        ],
                    }
                },
            }
        ]

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
                    "namespace": "http://www.interlis.ch/xtf/2.4/DictionariesCH_V2",
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
