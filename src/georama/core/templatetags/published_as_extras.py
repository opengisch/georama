from django import template
from django.contrib.auth.models import User

from georama.core.entities.models import PublishedAsRoleNameSystem

register = template.Library()


@register.simple_tag
def can_view(obj: PublishedAsRoleNameSystem, user: User):
    return obj.has_read_permission(user, obj._meta.app_label)


@register.simple_tag
def can_add(obj: PublishedAsRoleNameSystem, user: User):
    return obj.has_create_permission(user, obj._meta.app_label)


@register.simple_tag
def can_change(obj: PublishedAsRoleNameSystem, user: User):
    return obj.has_update_permission(user, obj._meta.app_label)


@register.simple_tag
def can_delete(obj: PublishedAsRoleNameSystem, user: User):
    return obj.has_delete_permission(user, obj._meta.app_label)


@register.simple_tag
def can_access(obj: PublishedAsRoleNameSystem, user: User):
    return obj.has_general_permission(user, obj._meta.app_label)
