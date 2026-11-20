from django.template import loader
from django.utils.safestring import mark_safe
from qgis_server_light.interface.common import BBox
from rest_framework.renderers import HTMLFormRenderer


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

        return super().render_field(field, parent_style)

    @staticmethod
    def get_datasource_extent(wms_layer) -> str | None:
        if wms_layer is None or not wms_layer.get_datasource.bbox_wgs84:
            return None
        return BBox.from_string(wms_layer.get_datasource.bbox_wgs84).to_2d_string()
