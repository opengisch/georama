from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


def perm(model: models.Model, action: str) -> Permission:
    return Permission.objects.get(
        content_type=ContentType.objects.get_for_model(model),
        codename=f"{action}_{model._meta.model_name}",
    )


def view_perm(model) -> Permission:
    return perm(model, "view")


def add_perm(model) -> Permission:
    return perm(model, "add")


def delete_perm(model) -> Permission:
    return perm(model, "delete")


def change_perm(model) -> Permission:
    return perm(model, "change")


def api_perm(model: models.Model) -> Permission:
    return Permission.objects.get(
        content_type=ContentType.objects.get_for_model(model),
        codename="can_use_manage_api",
    )
