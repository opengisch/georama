from django.contrib.auth.models import Group, Permission, User
from django.db.models import Q

from georama.core.entities.models import PermissionInterface
from georama.core.services import Service
from georama.data_integration.models import VectorDataSet
from georama.features.apps import central_app_label
from georama.features.models import PublishedAsOgcApiFeatures


class PublishedAsOgcApiFeaturesService(Service):
    models = [PublishedAsOgcApiFeatures]
    name = "ogcapi-f"


class VectorDatasetService(Service):
    models = [VectorDataSet]
    name = "vector_dataset"


class PermissionService(Service):
    models = [Permission]
    name = "permission"

    def filter(self, query, **kwargs):
        return query.filter(
            content_type__model=PublishedAsOgcApiFeatures._meta.model_name
        ).filter(codename__startswith=central_app_label)

    def get_by_object_pk(self, object_pk):
        items = []
        for model in self.models:
            items += self.filter(model.objects).filter(codename__icontains=object_pk).all()
        return items

    def get_users_by_permission(self, permission: Permission):
        users = User.objects.filter(Q(user_permissions=permission)).distinct()
        return users

    def get_groups_by_permission(self, permission: Permission):
        groups = Group.objects.filter(Q(permissions=permission)).distinct()
        return groups

    def get_permission_lookup(self, instance):
        permission_lookup = {}
        permissions = self.get_by_object_pk(instance.pk)
        permission_dict = {}
        permission_actions = []
        for permission in permissions:
            permission_interface = PermissionInterface.from_code_name(
                permission.codename, instance.name
            )
            if permission_interface.action not in permission_dict:
                permission_dict[permission_interface.action] = False
            if permission_interface.action not in permission_actions:
                permission_actions.append(permission_interface.action)
        for permission in permissions:
            permission_interface = PermissionInterface.from_code_name(
                permission.codename, instance.name
            )

            groups = self.get_groups_by_permission(permission)
            for group in groups:
                if group.name not in permission_lookup:
                    permission_lookup[group.name] = permission_dict.copy()
                permission_lookup[group.name][permission_interface.action] = True
            users = self.get_users_by_permission(permission)
            for user in users:
                if user.username not in permission_lookup:
                    permission_lookup[user.username] = permission_dict.copy()
                permission_lookup[user.username][permission_interface.action] = True

        return {"lookup": permission_lookup, "actions": permission_actions}
