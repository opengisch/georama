from django.template import loader
from django.utils.safestring import mark_safe
from rest_framework.renderers import HTMLFormRenderer


class CustomHTMLFormRenderer(HTMLFormRenderer):
    """Custom HTMLFormRenderer that handles Extent fields."""

    def render_field(self, field, parent_style):
        # Check if this is a extent field by field name
        if field.field_name.lower() == "extent_wgs84":
            field = field.as_form_field()
            template = loader.get_template("rest_framework/extent_field.html")
            return mark_safe(template.render({"field": field}).strip())

        return super().render_field(field, parent_style)
