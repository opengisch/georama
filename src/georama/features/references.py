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


@dataclass
class ReferenceResolver:
    """Resolves the reference fields of one layer against the collections of a mount.

    Attributes:
        layer_id: The QGIS layer id of the layer whose fields are resolved.
        relations: The relations of the QGIS project the layer belongs to.
        targets: The layers which can be referenced on the mount, keyed by QGIS layer id.
    """

    layer_id: str
    relations: list[Relation]
    targets: dict[str, ReferenceTarget]

    def keywords(self, field_name: str, widget: EditorWidget | None) -> dict:
        """Returns the `x-ogc-role` / `x-ogc-collectionId` keywords of a reference field.

        Empty if the field is no reference, or if it can't be resolved on the mount. Such
        fields stay plain.
        """
        if widget is None:
            return {}
        if widget.value_relation is not None:
            return self.value_relation_keywords(widget.value_relation)
        if widget.relation_reference is not None:
            return self.relation_reference_keywords(field_name, widget.relation_reference)
        return {}

    def value_relation_keywords(self, value_relation: ValueRelation) -> dict:
        # multi selection and filters need the filter collections, not part of this step
        if value_relation.allow_multi or value_relation.filter_expression:
            return {}
        target = self.targets.get(value_relation.layer_id)
        if target is None or target.key_field != value_relation.key_field:
            return {}
        return self.reference(target)

    def relation_reference_keywords(
        self, field_name: str, relation_reference: RelationReference
    ) -> dict:
        relation = next((r for r in self.relations if r.id == relation_reference.relation_id), None)
        # composite keys are not supported yet
        if relation is None or relation.referencing_layer_id != self.layer_id:
            return {}
        if len(relation.field_pairs) != 1:
            return {}
        pair = relation.field_pairs[0]
        if pair.referencing_field != field_name:
            return {}
        target = self.targets.get(relation.referenced_layer_id)
        if target is None or target.key_field != pair.referenced_field:
            return {}
        return self.reference(target)

    @staticmethod
    def reference(target: ReferenceTarget) -> dict:
        return {"x-ogc-role": "reference", "x-ogc-collectionId": target.collection_id}
