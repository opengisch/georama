from django import template

register = template.Library()


@register.simple_tag
def verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name.capitalize() or field_name


@register.simple_tag
def help_text(obj, field_name):
    return obj._meta.get_field(field_name).help_text or ""
