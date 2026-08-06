from django import template

register = template.Library()


@register.simple_tag
def verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name.capitalize() or field_name


@register.simple_tag
def help_text(obj, field_name):
    return obj._meta.get_field(field_name).help_text or ""


@register.simple_tag
def get_dict_value_by_key(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def field_name_and_value(obj):
    result = []
    for field in obj._meta.fields:
        result.append([field.verbose_name, field.help_text, getattr(obj, field.name)])
    return result


@register.simple_tag(takes_context=True)
def querystring_remove(context, *keys):
    params = context["request"].GET.copy()
    for key in keys:
        params.pop(key, None)

    if params:
        return "?" + params.urlencode()
    return ""
