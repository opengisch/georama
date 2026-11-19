from django import template
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.exporter.extract import ExportMessage

register = template.Library()

EXPORT_MESSAGE_CATEGORIES = {
    ExportMessage.Code.PROJECT_VERSION_UNSUPPORTED: _("Unsupported project version"),
    ExportMessage.Code.TREE_NODE_UNSUPPORTED: _("Unsupported project item"),
    ExportMessage.Code.LAYER_INVALID: _("Invalid layer"),
    ExportMessage.Code.LAYER_EMPTY: _("Empty layer"),
    ExportMessage.Code.LAYER_EXTENT_MISSING: _("Missing layer extent"),
    ExportMessage.Code.LAYER_EXTENT_FROM_PROJECT: _("Layer extent taken from project"),
    ExportMessage.Code.LAYER_EXTENT_REPROJECTION_FAILED: _("Layer extent reprojection failed"),
    ExportMessage.Code.LAYER_PROVIDER_UNSUPPORTED: _("Unsupported layer provider"),
    ExportMessage.Code.LAYER_TYPE_UNSUPPORTED: _("Unsupported layer type"),
    ExportMessage.Code.UNEXPECTED_ERROR: _("Unexpected error"),
}


@register.filter
def export_message_category(code):
    return EXPORT_MESSAGE_CATEGORIES.get(code, code)
