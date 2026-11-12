from dataclasses import dataclass

from qgis_server_light.interface.exporter.extract import (
    EditorWidget,
    Relation,
    RelationReference,
    ValueRelation,
)


@dataclass(frozen=True)
class ReferenceTarget:
    """A feature layer published on the same mount, which can be referenced.

    Attributes:
        collection_id: The collection identifier on the mount.
        key_field: The name of its primary key field, the value a reference stores.
    """

    collection_id: str
    key_field: str


def reference_keywords(
    field_name: str,
    layer_id: str,
    widget: EditorWidget | None,
    relations: list[Relation],
    targets: dict[str, ReferenceTarget],
) -> dict:
    """Returns the `x-ogc-role` / `x-ogc-collectionId` keywords of a reference field.

    Empty if the field is no reference, or if it can't be resolved on the mount. Such
    fields stay plain.
    """
    if widget is None:
        return {}
    if widget.value_relation is not None:
        return value_relation_keywords(widget.value_relation, targets)
    if widget.relation_reference is not None:
        return relation_reference_keywords(
            field_name, layer_id, widget.relation_reference, relations, targets
        )
    return {}


def value_relation_keywords(
    value_relation: ValueRelation, targets: dict[str, ReferenceTarget]
) -> dict:
    # multi selection and filters need the filter collections, not part of this step
    if value_relation.allow_multi or value_relation.filter_expression:
        return {}
    target = targets.get(value_relation.layer_id)
    if target is None or target.key_field != value_relation.key_field:
        return {}
    return _reference(target)


def relation_reference_keywords(
    field_name: str,
    layer_id: str,
    relation_reference: RelationReference,
    relations: list[Relation],
    targets: dict[str, ReferenceTarget],
) -> dict:
    relation = next((r for r in relations if r.id == relation_reference.relation_id), None)
    # composite keys are not supported yet
    if relation is None or relation.referencing_layer_id != layer_id:
        return {}
    if len(relation.field_pairs) != 1:
        return {}
    pair = relation.field_pairs[0]
    if pair.referencing_field != field_name:
        return {}
    target = targets.get(relation.referenced_layer_id)
    if target is None or target.key_field != pair.referenced_field:
        return {}
    return _reference(target)


def _reference(target: ReferenceTarget) -> dict:
    return {"x-ogc-role": "reference", "x-ogc-collectionId": target.collection_id}
