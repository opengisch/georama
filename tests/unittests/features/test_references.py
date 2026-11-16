import pytest
from qgis_server_light.interface.exporter.extract import (
    EditorWidget,
    Relation,
    RelationFieldPair,
    RelationReference,
    ValueMap,
    ValueRelation,
)

from georama.features.references import ReferenceResolver, ReferenceTarget


class TestReferenceResolver:
    """Resolves the fields of the layer `parcels_1a2b` against a mount on which the owners
    (`owners_3c4d`, key `id`) and the land use types (`land_use_5e6f`, key `code`) are
    published. Fields which can't be resolved stay plain, so they get no keywords.
    """

    @pytest.fixture
    def resolver(self):
        yield ReferenceResolver(
            layer_id="parcels_1a2b",
            relations=[
                Relation(
                    id="parcels_owners_rel",
                    name="Parcel owner",
                    referencing_layer_id="parcels_1a2b",
                    referenced_layer_id="owners_3c4d",
                    field_pairs=[
                        RelationFieldPair(referencing_field="owner_id", referenced_field="id")
                    ],
                ),
                Relation(
                    id="parcels_owners_composite_rel",
                    name="Parcel owner by country",
                    referencing_layer_id="parcels_1a2b",
                    referenced_layer_id="owners_3c4d",
                    field_pairs=[
                        RelationFieldPair(referencing_field="owner_id", referenced_field="id"),
                        RelationFieldPair(
                            referencing_field="owner_country", referenced_field="country"
                        ),
                    ],
                ),
                Relation(
                    id="buildings_owners_rel",
                    name="Building owner",
                    referencing_layer_id="buildings_7a8b",
                    referenced_layer_id="owners_3c4d",
                    field_pairs=[
                        RelationFieldPair(referencing_field="owner_id", referenced_field="id")
                    ],
                ),
            ],
            targets={
                "owners_3c4d": ReferenceTarget(collection_id="owners", key_field="id"),
                "land_use_5e6f": ReferenceTarget(collection_id="land_use", key_field="code"),
            },
        )

    @pytest.mark.parametrize(
        "value_relation,expected",
        [
            # the referenced layer is published and the stored value is its key
            (
                ValueRelation(layer_id="land_use_5e6f", key_field="code", value_field="label"),
                {"x-ogc-role": "reference", "x-ogc-collectionId": "land_use"},
            ),
            # the referenced layer is not published on the mount
            (
                ValueRelation(layer_id="streets_9c0d", key_field="code", value_field="label"),
                {},
            ),
            # the stored value is not the key of the referenced layer
            (
                ValueRelation(layer_id="land_use_5e6f", key_field="label", value_field="label"),
                {},
            ),
            # multi selection needs more than a plain reference
            (
                ValueRelation(
                    layer_id="land_use_5e6f",
                    key_field="code",
                    value_field="label",
                    allow_multi=True,
                ),
                {},
            ),
            # a filter needs its own collection
            (
                ValueRelation(
                    layer_id="land_use_5e6f",
                    key_field="code",
                    value_field="label",
                    filter_expression='"active" = true',
                ),
                {},
            ),
        ],
    )
    def test_value_relation(self, resolver, value_relation, expected):
        widget = EditorWidget(value_relation=value_relation)
        assert resolver.keywords("land_use", widget) == expected

    @pytest.mark.parametrize(
        "field_name,relation_id,expected",
        [
            # the field is the referencing field of the relation to the published owners
            (
                "owner_id",
                "parcels_owners_rel",
                {"x-ogc-role": "reference", "x-ogc-collectionId": "owners"},
            ),
            # the relation exists, but it is another field of the layer which references
            ("area", "parcels_owners_rel", {}),
            # composite keys can't be expressed as one reference
            ("owner_id", "parcels_owners_composite_rel", {}),
            # the relation is the one of another layer
            ("owner_id", "buildings_owners_rel", {}),
            # the relation is not part of the project export
            ("owner_id", "unknown_rel", {}),
        ],
    )
    def test_relation_reference(self, resolver, field_name, relation_id, expected):
        widget = EditorWidget(relation_reference=RelationReference(relation_id=relation_id))
        assert resolver.keywords(field_name, widget) == expected

    @pytest.mark.parametrize(
        "widget",
        [
            # field without exported editor widget
            None,
            # a value map is a value list, not a reference
            EditorWidget(value_map=ValueMap()),
        ],
    )
    def test_other_fields_stay_plain(self, resolver, widget):
        assert resolver.keywords("owner_id", widget) == {}
