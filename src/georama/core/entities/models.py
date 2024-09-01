import logging
import uuid
from dataclasses import dataclass
from typing import List

from django.contrib.auth.models import User
from django.db import models

log = logging.getLogger(__name__)


@dataclass
class PermissionInterface:
    published_as_type: str
    action: str
    identifier: str
    name: str

    @property
    def codename(self) -> str:
        return f'{self.published_as_type}_{self.action}_{self.identifier}'
    
    @property
    def readable_name(self) -> str:
        return f'Can {self.action} {self.name}'


class PublishedAsRoleNameSystem(models.Model):
    published_as_type = None
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    name = models.CharField(max_length=1000, null=True, default=None, blank=True)
    public = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def read_permissions(self) -> List[PermissionInterface]:
        return [] if self.public else [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="read",
                identifier=self.identifier,
                name=self.name
            )
        ]

    @property
    def create_permissions(self) -> List[PermissionInterface]:
        return [] if self.public else [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="create",
                identifier=self.identifier,
                name=self.name
            )
        ]

    @property
    def update_permissions(self) -> List[PermissionInterface]:
        return [] if self.public else [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="update",
                identifier=self.identifier,
                name=self.name
            )
        ]

    @property
    def delete_permissions(self) -> List[PermissionInterface]:
        return [] if self.public else [
            PermissionInterface(
                published_as_type=self.published_as_type,
                action="delete",
                identifier=self.identifier,
                name=self.name
            )
        ]

    @property
    def permissions(self) -> List[PermissionInterface]:
        return (
                self.read_permissions +
                self.create_permissions +
                self.update_permissions +
                self.delete_permissions
        )

    @staticmethod
    def to_string(permissions: List[PermissionInterface]) -> List[str]:
        return [permission.codename for permission in permissions]

    @property
    def permission_codenames(self) -> List[str]:
        return self.to_string(self.permissions)

    def has_general_permission(self, user: User, app_name: str) -> bool:
        return self.has_grained_permission(user, self.permission_codenames, app_name)

    @staticmethod
    def has_grained_permission(user: User, permissions: List[str], app_name: str) -> bool:
        permissions = [f'{app_name}.{permission}' for permission in permissions]
        if user.is_superuser:
            log.debug(f'Superuser => has access')
            # superusers always have access
            return True
        if len(permissions) == 0:
            log.debug(f'Public dataset => has access')
            # this is a public dataset
            return True
        else:
            matching_permissions = list(set(permissions) & user.get_all_permissions())
            log.debug(f'Matching permissions: {permissions}')
            log.debug(f'Matching permissions: {matching_permissions}')
            if len(matching_permissions) > 0:
                log.debug(f'Access granted')
                return True
            else:
                log.debug(f'Access denied')
                return False

    def has_read_permission(self, user: User, app_name: str):
        return self.has_grained_permission(user, self.to_string(self.read_permissions), app_name)

    def has_create_permission(self, user: User, app_name: str):
        return self.has_grained_permission(user, self.to_string(self.create_permissions), app_name)

    def has_update_permission(self, user: User, app_name: str):
        return self.has_grained_permission(user, self.to_string(self.update_permissions), app_name)

    def has_delete_permission(self, user: User, app_name: str):
        return self.has_grained_permission(user, self.to_string(self.delete_permissions), app_name)


class PublishedAs(PublishedAsRoleNameSystem):
    title = models.CharField(max_length=1000, null=True, default=None, blank=True)
    description = models.TextField(null=True, default=None, blank=True)
    license = models.TextField(default="""
    This dataset is made available under the Open Database
    License: http://opendatacommons.org/licenses/odbl/1.0/.
    Any rights in individual contents of the database are licensed
    under the Database Contents
    License: http://opendatacommons.org/licenses/dbcl/1.0/
    """)
    fees = models.TextField(default="No fees apply.")
    access_constraints = models.TextField(default="No access constraints apply.")

    class Meta:
        abstract = True
