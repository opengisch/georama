from typing import List
from django.contrib.auth.models import Group, User, Permission


def save_group_permissions(groups_selected: List[Group], permission: Permission):
    groups_all = Group.objects.all()
    for group in groups_all:
        if group in groups_selected:
            group.permissions.add(
                permission
            )
        else:
            group.permissions.remove(
                permission
            )


def save_user_permissions(user_selected: List[User], permission: Permission):
    user_all = User.objects.all()
    for user in user_all:
        if user in user_selected:
            user.user_permissions.add(
                permission
            )
        else:
            user.user_permissions.remove(
                permission
            )