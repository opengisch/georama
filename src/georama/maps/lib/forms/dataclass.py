from dataclasses import fields, is_dataclass
from typing import Any, Union, get_args, get_origin, get_type_hints

from django import forms
from django.forms import formset_factory

from georama.maps.interfaces.ech271 import references
from georama.maps.interfaces.ech271.eCH0271_1 import eCH0271

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


def resolve_annotation(annotation, required=True):
    """Resolve Union[T, None], Optional[T], lists etc."""
    origin = get_origin(annotation)
    args = get_args(annotation)

    # Optional[T] / T | None
    if origin is Union and type(None) in args:
        non_none = [a for a in args if a is not type(None)][0]
        return resolve_annotation(non_none, required=False)

    # list[T]
    if origin is list:
        return list, args[0], required

    return annotation, None, required


def dataclass_to_form(dc: type, registry=None) -> type[forms.Form]:
    """Convert a dataclass to a Django Form, supporting nested dataclasses."""
    if registry is None:
        registry = FORM_REGISTRY

    if dc in registry:
        return registry[dc]
    globals_dict = vars(__import__(dc.__module__))
    globals_dict.update(vars(references))
    globals_dict.update(vars(eCH0271))
    type_hints = get_type_hints(dc, globalns=globals_dict)
    attrs = {}

    for f in fields(dc):
        annotation = type_hints[f.name]
        resolved, inner, required = resolve_annotation(annotation)

        # Nested dataclass
        if is_dataclass(resolved):
            # Single nested dataclass → JSONField (minimal)
            attrs[f.name] = forms.JSONField(required=required)
        elif resolved is list:
            # List[T] → Formset (handled separately)
            continue
        else:
            field_cls = TYPE_MAP.get(resolved, forms.CharField)
            attrs[f.name] = field_cls(required=required)

    FormClass = type(f"{dc.__name__}Form", (forms.Form,), attrs)
    registry[dc] = FormClass
    return FormClass


def dataclass_to_formset(dc: type, registry=None, extra=1) -> type[forms.BaseFormSet]:
    """Return a formset class for a dataclass that is a list of dataclasses."""
    if registry is None:
        registry = FORMSET_REGISTRY

    if dc in registry:
        return registry[dc]

    form_cls = dataclass_to_form(dc)
    FormSet = formset_factory(form_cls, extra=extra)
    registry[dc] = FormSet
    return FormSet


def generate_forms(dc: type) -> dict[str, Any]:
    """
    Returns a dict with:
    - 'form' : main form class
    - 'formsets': dict of field_name -> FormSet for list[Dataclass] fields
    """
    globals_dict = vars(__import__(dc.__module__))
    globals_dict.update(vars(references))
    globals_dict.update(vars(eCH0271))

    type_hints = get_type_hints(dc, globalns=globals_dict)
    formsets = {}
    main_form = dataclass_to_form(dc)

    for f in fields(dc):
        annotation = type_hints[f.name]
        resolved, inner, required = resolve_annotation(annotation)
        if resolved is list and is_dataclass(inner):
            formsets[f.name] = dataclass_to_formset(inner)

    return {"form": main_form, "formsets": formsets}


forms_dict = generate_forms(eCH0271.CHE_MD_Metadata)
CHE_MD_MetadataForm = forms_dict["form"]
CHE_MD_MetadataotherLocaleFormSet = forms_dict["formsets"]["otherLocale"]

x = 1
