from django.db import models


class Permission(models.Model):
    class Meta:
        managed = False
        default_permissions = ()
        permissions = [
            ("can_use_manage_api", "Can use the management API"),
        ]
