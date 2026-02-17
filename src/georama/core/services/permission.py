import copy

from django.contrib.auth.models import Group, Permission, User

from georama.core.entities.models import PermissionInterface


class DBService:
    action_icons = {
        "create": "fa-circle-plus",
        "read": "fa-eye",
        "update": "fa-pencil",
        "delete": "fa-trash-can",
    }
    default_icon = "fa-check"

    def __init__(self, model, app_label):
        self.model = model
        self.app_label = app_label

    def icon_lookup(self, action):
        selected_icon = self.action_icons.get(action)
        if selected_icon is None:
            selected_icon = self.default_icon
        return selected_icon

    def get_users_by_permission(self, permission: Permission):
        users = User.objects.filter(user_permissions=permission).distinct()
        return users

    def get_groups_by_permission(self, permission: Permission):
        groups = Group.objects.filter(permissions=permission).distinct()
        return groups

    def get_by_object_pk(self, object_pk: str):
        queryset = (
            Permission.objects.filter(content_type__model=self.model._meta.model_name)
            .filter(codename__startswith=self.app_label)
            .filter(codename__icontains=str(object_pk))
            .all()
        )
        return queryset

    def get_permitted_object(self, object_pk: str):
        return self.model.objects.filter(pk=object_pk).get()

    def get_permission_lookup(self, object_pk: str):
        instance = self.get_permitted_object(object_pk)
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
        lookup["users"].sort(key=lambda x: x["name"].lower())
        for key in permission_lookup["groups"]:
            item = permission_lookup["groups"][key]
            item["id"] = key
            lookup["groups"].append(item)
        lookup["groups"].sort(key=lambda x: x["name"].lower())
        return {"lookup": lookup, "actions": permission_actions}
