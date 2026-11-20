from django.template import loader
from django.utils.safestring import mark_safe
from qgis_server_light.interface.common import BBox
from rest_framework.renderers import HTMLFormRenderer

from georama.core.common.serializers import PngPreviewField


class CustomHTMLFormRenderer(HTMLFormRenderer):
    """Custom HTMLFormRenderer that handles Extent fields."""

    def render_field(self, field, parent_style):
        # Check if this is a extent field by field name
        if field.field_name.lower() == "extent_wgs84":
            datasource_extent = self.get_datasource_extent(field._field.parent.instance)
            field = field.as_form_field()
            template = loader.get_template("rest_framework/extent_field.html")
            return mark_safe(
                template.render({"field": field, "datasource_extent": datasource_extent}).strip()
            )

        if isinstance(field._field, PngPreviewField):
            preview_field = field._field
            field = field.as_form_field()
            template = loader.get_template("rest_framework/png_preview_field.html")
            return mark_safe(
                template.render(
                    {
                        "field": field,
                        "width": preview_field.width,
                        "height": preview_field.height,
                        "project_preview": self.get_project_preview(
                            preview_field.parent.instance, preview_field
                        ),
                    }
                ).strip()
            )

        return super().render_field(field, parent_style)

    @staticmethod
    def get_project_preview(instance, preview_field: PngPreviewField) -> str | None:
        project = getattr(instance, "project", None)
        if project is None or project.preview is None:
            return None
        return preview_field.to_representation(project.preview)

    @staticmethod
    def get_datasource_extent(wms_layer) -> str | None:
        if wms_layer is None or not wms_layer.get_datasource.bbox_wgs84:
            return None
        return BBox.from_string(wms_layer.get_datasource.bbox_wgs84).to_2d_string()
