import types

import pytest
from georama.maps.lib.forms.dataclass import (
    ili_field_type_restrictions, ili_field_type_restrictions_mandatory,
    ili_field_type_restrictions_multiplicity_max,
    ili_field_type_restrictions_multiplicity_min, resolve_annotation)


class TestDataclassToFormLogic:

    @pytest.mark.parametrize(
        "annotation,expected",
        [
            (str, (str, [])),
            (str | None, (types.UnionType, [str])),
            (str | int | None, (types.UnionType, [str, int])),
            (list[str], (list, [str])),
            (list[str | None], (list, [str])),
            (list[str | int | None], (list, [str, int])),
        ],
    )
    def test_resolve_annotation(self, annotation, expected):
        assert resolve_annotation(annotation) == expected

    @pytest.mark.parametrize(
        "annotation,raises",
        [
            (list[list[str]], TypeError),
            (list[str | list[str]], TypeError),
        ],
    )
    def test_resolve_annotation_nested_list_fail(self, annotation, raises):
        with pytest.raises(raises):
            resolve_annotation(annotation)

    @pytest.mark.parametrize(
        "metadata,expected",
        [
            ({}, None),
            ({"interlis": {}}, None),
            ({"interlis": {"type_restrictions": None}}, None),
            ({"interlis": {"type_restrictions": {}}}, {}),
        ],
    )
    def test_ili_field_type_restrictions(self, metadata, expected):
        assert ili_field_type_restrictions(metadata) == expected

    @pytest.mark.parametrize(
        "metadata,expected",
        [
            ({}, False),
            ({"interlis": {}}, False),
            ({"interlis": {"type_restrictions": None}}, False),
            ({"interlis": {"type_restrictions": {}}}, False),
            ({"interlis": {"type_restrictions": {"mandatory": None}}}, False),
            ({"interlis": {"type_restrictions": {"mandatory": True}}}, True),
            ({"interlis": {"type_restrictions": {"mandatory": False}}}, False),
        ],
    )
    def test_ili_field_type_restrictions_mandatory(self, metadata, expected):
        assert ili_field_type_restrictions_mandatory(metadata) == expected

    @pytest.mark.parametrize(
        "metadata,expected",
        [
            ({}, 0),
            ({"interlis": {}}, 0),
            ({"interlis": {"type_restrictions": None}}, 0),
            ({"interlis": {"type_restrictions": {}}}, 0),
            ({"interlis": {"type_restrictions": {"multiplicity": None}}}, 0),
            ({"interlis": {"type_restrictions": {"multiplicity": {}}}}, 0),
            ({"interlis": {"type_restrictions": {"multiplicity": {"min": None}}}}, 0),
            ({"interlis": {"type_restrictions": {"multiplicity": {"min": 1}}}}, 1),
            ({"interlis": {"type_restrictions": {"multiplicity": {"min": 0}}}}, 0),
        ],
    )
    def test_ili_field_type_restrictions_multiplicity_min(self, metadata, expected):
        assert ili_field_type_restrictions_multiplicity_min(metadata) == expected

    @pytest.mark.parametrize(
        "metadata,expected",
        [
            ({}, None),
            ({"interlis": {}}, None),
            ({"interlis": {"type_restrictions": None}}, None),
            ({"interlis": {"type_restrictions": {}}}, None),
            ({"interlis": {"type_restrictions": {"multiplicity": None}}}, None),
            ({"interlis": {"type_restrictions": {"multiplicity": {}}}}, None),
            (
                {"interlis": {"type_restrictions": {"multiplicity": {"max": None}}}},
                None,
            ),
            ({"interlis": {"type_restrictions": {"multiplicity": {"max": 1}}}}, 1),
            ({"interlis": {"type_restrictions": {"multiplicity": {"max": 0}}}}, 0),
        ],
    )
    def test_ili_field_type_restrictions_multiplicity_max(self, metadata, expected):
        assert ili_field_type_restrictions_multiplicity_max(metadata) == expected
