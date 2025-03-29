import logging
import uuid
from dataclasses import dataclass
from typing import List

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db import models

log = logging.getLogger(__name__)


@dataclass
class PermissionInterface:
    published_as_type: str
    action: str
    target_identifier: str
    target_name: str

    @property
    def codename(self) -> str:
        return f"{self.published_as_type}_{self.action}_{self.target_identifier}"

    def readable_name(self, target_readable_identifier) -> str:
        """Creates the permission name stored in the db and used in the django admin

        Is a method and not a property to avoid database queries for Permission checking."""
        return f"Can {self.action} {self.target_name} ({target_readable_identifier})"


class PublishedAsRoleNameSystem(models.Model):
    """PublishedAsRoleNameSystem: a published resource with CRUD operations ruled by permissions

    This class does not have any database operation (save, update delete, ...),
    so that interactions with permissions are fast, without any database query.
    It should stay that way.
    """

    published_as_type = None
    identifier = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, null=False
    )
    name = models.CharField(max_length=1000, null=True, default=None, blank=True)
    public = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def readable_identifier(self) -> str:
        return f"{self.identifier}"

    @property
    def read_permissions(self) -> List[PermissionInterface]:
        return [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="read",
                target_identifier=f"{self.identifier}",
                target_name=self.name,
            )
        ]

    @property
    def create_permissions(self) -> List[PermissionInterface]:
        return [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="create",
                target_identifier=f"{self.identifier}",
                target_name=self.name,
            )
        ]

    @property
    def update_permissions(self) -> List[PermissionInterface]:
        return [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="update",
                target_identifier=f"{self.identifier}",
                target_name=self.name,
            )
        ]

    @property
    def delete_permissions(self) -> List[PermissionInterface]:
        return [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="delete",
                target_identifier=f"{self.identifier}",
                target_name=self.name,
            )
        ]

    @property
    def permissions(self) -> List[PermissionInterface]:
        return (
            self.read_permissions
            + self.create_permissions
            + self.update_permissions
            + self.delete_permissions
        )

    @staticmethod
    def to_string(permissions: List[PermissionInterface]) -> List[str]:
        return [permission.codename for permission in permissions]

    @property
    def permission_codenames(self) -> List[str]:
        return self.to_string(self.permissions)

    def has_general_permission(self, user: User, app_name: str) -> bool:
        return self._has_grained_permission(user, self.permission_codenames, app_name)

    @staticmethod
    def _has_grained_permission(user: User, permissions: List[str], app_name: str) -> bool:
        permissions = [f"{app_name}.{permission}" for permission in permissions]
        if user.is_superuser:
            log.debug(f"Superuser => has access")
            # superusers always have access
            return True
        else:
            matching_permissions = list(set(permissions) & user.get_all_permissions())
            log.debug(f"Matching permissions: {permissions}")
            log.debug(f"Matching permissions: {matching_permissions}")
            if len(matching_permissions) > 0:
                log.debug(f"Access granted")
                return True
            else:
                log.debug(f"Access denied")
                return False

    def has_read_permission(self, user: User, app_name: str) -> bool:
        if self.public:
            return True
        return self._has_grained_permission(
            user, self.to_string(self.read_permissions), app_name
        )

    def has_create_permission(self, user: User, app_name: str) -> bool:
        return self._has_grained_permission(
            user, self.to_string(self.create_permissions), app_name
        )

    def has_update_permission(self, user: User, app_name: str) -> bool:
        return self._has_grained_permission(
            user, self.to_string(self.update_permissions), app_name
        )

    def has_delete_permission(self, user: User, app_name: str) -> bool:
        return self._has_grained_permission(
            user, self.to_string(self.delete_permissions), app_name
        )


class PublishedAs(PublishedAsRoleNameSystem):
    title = models.CharField(max_length=1000, null=True, default=None, blank=True)
    description = models.TextField(null=True, default=None, blank=True)
    license = models.TextField(
        default="""
    This dataset is made available under the Open Database
    License: http://opendatacommons.org/licenses/odbl/1.0/.
    Any rights in individual contents of the database are licensed
    under the Database Contents
    License: http://opendatacommons.org/licenses/dbcl/1.0/
    """
    )
    fees = models.TextField(default="No fees apply.")
    access_constraints = models.TextField(default="No access constraints apply.")

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        models.signals.pre_delete.connect(delete_publishedas_db_permissions, sender=cls)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
        content_type = ContentType.objects.get_for_model(type(self))
        for permission in self.permissions:
            if Permission.objects.filter(codename=permission.codename).count() == 0:
                Permission(
                    codename=permission.codename,
                    name=permission.readable_name(self.readable_identifier),
                    content_type=content_type,
                ).save()

    def delete(self, using=None, keep_parents=False):
        super().delete(
            using=using,
            keep_parents=keep_parents,
        )

    class Meta:
        abstract = True


def delete_publishedas_db_permissions(sender, instance, **kwargs):
    Permission.objects.filter(codename__in=instance.permission_codenames).delete()


def save_group_permissions(groups_selected: List[Group], permission: Permission):
    groups_all = Group.objects.all()
    for group in groups_all:
        if group in groups_selected:
            group.permissions.add(permission)
        else:
            group.permissions.remove(permission)


def save_user_permissions(user_selected: List[User], permission: Permission):
    user_all = User.objects.all()
    for user in user_all:
        if user in user_selected:
            user.user_permissions.add(permission)
        else:
            user.user_permissions.remove(permission)
