from rest_framework import renderers


class StandaloneTemplateHTMLRenderer(renderers.TemplateHTMLRenderer):
    """Renders the template without the request, so no context processor runs. Pages
    which have to render while the database is down (health) use it, since context
    processors like `menu_items` hit the database.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        return super().render(data, accepted_media_type, {**renderer_context, "request": None})
