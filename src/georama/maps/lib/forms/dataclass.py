import types
from dataclasses import Field, asdict, fields, is_dataclass
from enum import Enum
from typing import Union, get_args, get_origin, get_type_hints

from django import forms
from django.forms import BaseFormSet, formset_factory

from georama.maps.interfaces.ech271 import Localisation_V2, references
from georama.maps.interfaces.ech271.eCH0271_1 import eCH0271
from georama.maps.interfaces.ech271.references import Ref


class DataclassForm(forms.Form):
    dataclass: None

    def to_dataclass_instance(self):
        return self.dataclass(**self.cleaned_data)

    @classmethod
    def from_dataclass_instance(cls, dataclass_instance):
        return cls(asdict(dataclass_instance))


class DataclassCache(dict):
    pass


class DataclassFieldCache(dict):
    pass


class FormCache(dict):
    pass


class FormFieldCache(dict):
    pass


class FormSetCache(dict):
    pass


class Tree(dict):
    def add_new(self, key: str):
        self[key] = []

    def add_child(self, key, child_key):
        if key not in self:
            self.add_new(key)
        self[key].append(child_key)

    @property
    def root(self) -> str:
        return self[""][0]


class Cache:
    def __init__(self):
        self.dataclass_cache = DataclassCache()
        self.dataclass_field_cache = DataclassFieldCache()
        self.form_cache = FormCache()
        self.form_field_cache = FormFieldCache()
        self.form_set_cache = FormSetCache()
        self.tree = Tree()

    @property
    def main_form_key(self) -> str:
        main_match = list(self.form_cache.keys() - self.form_set_cache.keys())
        if len(main_match) == 1:
            return main_match[0]
        else:
            raise LookupError(
                "There should be a difference of exactly 1 between form and formset cache"
            )

    @property
    def main_form(self):
        return self.form_cache[self.main_form_key]

    def create_tree_item(self, key: str, formset: BaseFormSet):
        return {"id": key, "fs": formset, "child_fs": []}

    def unwrap_tree(self, fs_key: str, tree: list, parent_tree_item: dict | None = None):
        tree_item = {"id": fs_key, "fs": self.form_set_cache[fs_key], "child_fs": []}
        tree.append(tree_item)
        children = self.tree.get(fs_key, [])
        for child_key in children:
            if parent_tree_item is not None:
                parent_tree_item["child_fs"].append(self.form_set_cache[child_key])
            self.unwrap_tree(child_key, tree, tree_item)

    @property
    def formset_tree(self) -> list[dict]:
        tree = []
        for fs_key in self.tree[self.main_form_key]:
            self.unwrap_tree(fs_key, tree)
        return tree


def all_fields(cls):
    out = []
    for c in reversed(cls.__mro__):
        if hasattr(c, "__dataclass_fields__"):
            out.extend(fields(c))
    return out


# Primitive Mapping
TYPE_MAP = {
    str: forms.CharField,
    int: forms.IntegerField,
    float: forms.FloatField,
    bool: forms.BooleanField,
}

# Registry, um zyklische Referenzen zu vermeiden
FORM_REGISTRY: dict[type, type[forms.Form]] = {}
FORMSET_REGISTRY: dict[type, type[forms.BaseFormSet]] = {}


def resolve_annotation(annotation):
    """Resolve Union[T, None], Optional[T], lists etc."""
    origin = get_origin(annotation)
    args = list(get_args(annotation))

    # Optional[T] / T | None
    if origin in [types.UnionType, Union, list]:
        args = [a for a in args if a is not type(None)]
        unchained_args = []
        for arg in args:
            if get_origin(arg) is list:
                raise TypeError("Nested 'list' are not covered")
            o, a = resolve_annotation(arg)
            if len(a) == 0:
                unchained_args.append(o)
            else:
                unchained_args += a

        return origin, unchained_args

    return annotation, []


def ili_oid_key_from_dataclass(dataclass) -> str:
    return dataclass().metadata["interlis"]["oid"]


def ili_oid_key_from_dataclass_field(field: Field) -> str:
    return field.metadata["interlis"]["oid"]


def ili_field_type_restrictions(metadata: dict) -> dict | None:
    ili_type_restrictions = metadata.get("interlis", {}).get("type_restrictions", None)
    return ili_type_restrictions


def ili_field_type_restrictions_mandatory(metadata: dict):
    tr = ili_field_type_restrictions(metadata)
    if tr is None:
        mandatory = False
    else:
        mandatory = tr.get("mandatory", False)
        if mandatory is None:
            mandatory = False
    return mandatory


def ili_field_type_restrictions_multiplicity_min(metadata: dict) -> int:
    tr = ili_field_type_restrictions(metadata)
    if tr is None:
        minimum = 0
    else:
        multiplicity = tr.get("multiplicity", {})
        if multiplicity is None:
            multiplicity = {}
        minimum = multiplicity.get("min", 0)
        if minimum is None:
            minimum = 0
    return minimum


def ili_field_type_restrictions_multiplicity_max(metadata: dict) -> int | None:
    tr = ili_field_type_restrictions(metadata)
    if tr is None:
        maximum = None
    else:
        multiplicity = tr.get("multiplicity", {})
        if multiplicity is None:
            multiplicity = {}
        maximum = multiplicity.get("max")
    return maximum


def enum_to_choices(enum_cls):
    return [(e.value, e.name.replace("_", " ").title()) for e in enum_cls]


def dataclass_to_form(
    dc: type,
    cache: Cache,
    parent: str,
):
    """Convert a dataclass to a Django Form, supporting nested dataclasses."""
    oid_key = ili_oid_key_from_dataclass(dc)
    if oid_key not in cache.dataclass_cache:
        cache.dataclass_cache[oid_key] = dc

    globals_dict = vars(__import__(dc.__module__))
    globals_dict.update(vars(references))
    globals_dict.update(vars(eCH0271))
    globals_dict.update(vars(Localisation_V2))
    type_hints = get_type_hints(dc, globalns=globals_dict)
    attrs = {}

    for f in all_fields(dc):
        annotation = type_hints[f.name]
        resolved, inner = resolve_annotation(annotation)

        chosen = resolved

        if resolved in [types.UnionType, list]:
            if len(inner) > 1:
                raise TypeError(
                    "More than one type on the same field is not allowed currently"
                )
            else:
                chosen = inner[0]
        if is_dataclass(chosen) and chosen != Ref:
            dataclass_to_formset(
                f.name,
                chosen,
                cache,
                ili_field_type_restrictions_multiplicity_min(dict(f.metadata)),
                ili_field_type_restrictions_multiplicity_max(dict(f.metadata)),
                oid_key,
            )
        field_cls = TYPE_MAP.get(chosen)
        kwargs = {}
        if field_cls is None and issubclass(chosen, Enum):
            field_cls = forms.ChoiceField
            kwargs["choices"] = enum_to_choices(chosen)
        if field_cls is not None:
            if f.name == "struct_content":
                kwargs["label"] = False
            mandatory = ili_field_type_restrictions_mandatory(dict(f.metadata))
            kwargs["required"] = mandatory
            attrs[f.name] = field_cls(**kwargs)
        attrs["dataclass"] = dc

    FormClass = type(f"{dc.__name__}Form", (DataclassForm,), attrs)
    cache.form_cache[oid_key] = FormClass
    cache.tree.add_child(parent, oid_key)


def dataclass_to_formset(
    name: str,
    dc: type,
    cache: Cache,
    extra,
    max_num,
    parent: str,
):
    """Return a formset class for a dataclass that is a list of dataclasses."""
    oid_key = ili_oid_key_from_dataclass(dc)
    if oid_key not in cache.dataclass_cache:
        cache.dataclass_cache[oid_key] = dc
    else:
        return

    dataclass_to_form(dc, cache, parent)
    FormSet = formset_factory(cache.form_cache[oid_key], extra=1, max_num=max_num)
    FormSet.title = name.title() if name != "struct_content" else parent
    cache.form_set_cache[oid_key] = FormSet


def generate_forms(dc: type) -> Cache:
    """
    Returns a dict with:
    - 'form' : main form class
    - 'formsets': dict of field_name -> FormSet for list[Dataclass] fields
    """

    cache = Cache()
    dataclass_to_form(dc, cache, "")

    return cache


# generate_forms(eCH0271.CHE_MD_DataIdentification)
