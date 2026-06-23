from django.views import generic


class Index(generic.TemplateView):
    template_name = "integration/index.html"
