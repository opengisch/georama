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
        permission_lookup = {"users": {}, "groups": {}}
        permissions = self.get_by_object_pk(instance.pk)
        permission_dict = {}
        permission_actions = []
        for permission in permissions:
            permission_interface = PermissionInterface.from_code_name(
                permission.codename, instance.name
            )
            if permission_interface.action not in permission_dict:
                permission_dict[permission_interface.action] = False
                permission_dict[f"{permission_interface.action}_id"] = permission.pk
            if permission_interface.action not in permission_actions:
                permission_actions.append(permission_interface.action)
        for permission in permissions:
            permission_interface = PermissionInterface.from_code_name(
                permission.codename, instance.name
            )

            groups = self.get_groups_by_permission(permission)
            for group in groups:
                if group.pk not in permission_lookup["groups"]:
                    permission_lookup["groups"][group.pk] = permission_dict.copy()
                permission_lookup["groups"][group.pk][permission_interface.action] = True
                permission_lookup["groups"][group.pk]["name"] = group.name
            users = self.get_users_by_permission(permission)
            for user in users:
                if user.pk not in permission_lookup["users"]:
                    permission_lookup["users"][user.pk] = permission_dict.copy()
                permission_lookup["users"][user.pk][permission_interface.action] = True

        return {"lookup": permission_lookup, "actions": permission_actions}
