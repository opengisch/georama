import copy

from django.contrib.auth.models import Group, Permission, User

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
    action_icons = {
        "create": "fa-circle-plus",
        "read": "fa-eye",
        "update": "fa-pencil",
        "delete": "fa-trash-can",
    }
    default_icon = "fa-check"

    def icon_lookup(self, action):
        selected_icon = self.action_icons.get(action)
        if selected_icon is None:
            selected_icon = self.default_icon
        return selected_icon

    def filter(self, query, **kwargs):
        return query.filter(
            content_type__model=PublishedAsOgcApiFeatures._meta.model_name
        ).filter(codename__startswith=central_app_label)

    def get_by_object_pk(self, object_pk):
        items = []
        for model in self.models:
            items += (
                self.filter(model.objects).filter(codename__icontains=str(object_pk)).all()
            )
        return items

    def get_users_by_permission(self, permission: Permission):
        users = User.objects.filter(user_permissions=permission).distinct()
        return users

    def get_groups_by_permission(self, permission: Permission):
        groups = Group.objects.filter(permissions=permission).distinct()
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
                permission_dict[permission_interface.action] = {
                    "allowed": False,
                    "id": permission.pk,
                    "icon": self.icon_lookup(permission_interface.action),
                }
            if permission_interface.action not in permission_actions:
                permission_actions.append(permission_interface.action)
        for permission in permissions:
            permission_interface = PermissionInterface.from_code_name(
                permission.codename, instance.name
            )

            groups = self.get_groups_by_permission(permission)
            for group in groups:
                if group.pk not in permission_lookup["groups"]:
                    permission_lookup["groups"][group.pk] = copy.deepcopy(permission_dict)
                permission_lookup["groups"][group.pk][permission_interface.action][
                    "allowed"
                ] = True
                permission_lookup["groups"][group.pk]["name"] = group.name
            users = self.get_users_by_permission(permission)
            for user in users:
                if user.pk not in permission_lookup["users"]:
                    permission_lookup["users"][user.pk] = copy.deepcopy(permission_dict)
                permission_lookup["users"][user.pk][permission_interface.action][
                    "allowed"
                ] = True
                permission_lookup["users"][user.pk]["name"] = user.username
        lookup = {"users": [], "groups": []}
        for key in permission_lookup["users"]:
            item = permission_lookup["users"][key]
            item["id"] = key
            lookup["users"].append(item)
        for key in permission_lookup["groups"]:
            item = permission_lookup["groups"][key]
            item["id"] = key
            lookup["groups"].append(item)
        return {"lookup": lookup, "actions": permission_actions}
