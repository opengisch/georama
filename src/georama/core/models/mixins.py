from django.contrib.auth import get_permission_codename
from django.db import models


class GeoramaPermissionMixin(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def assemble_perm(cls, app_label: str, codename: str):
        return f"{app_label}.{codename}"

    @classmethod
    def perm(cls, action: str) -> str:
        opts = cls._meta
        codename = get_permission_codename(action, opts)
        return cls.assemble_perm(opts.app_label, codename)

    @classmethod
    def perm_add(cls):
        return cls.perm("add")

    @classmethod
    def perm_change(cls):
        return cls.perm("change")

    @classmethod
    def perm_delete(cls):
        return cls.perm("delete")

    @classmethod
    def perm_view(cls):
        return cls.perm("view")

    @classmethod
    def perm_manage_permissions(cls):
        return cls.assemble_perm(cls._meta.app_label, "can_manage_object_permissions")
