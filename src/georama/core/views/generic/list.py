from django.conf import settings
from django.core.paginator import Page
from django.views.generic import ListView

from georama.core.views.generic.mixins import BreadcrumbMixin


class GeoramaListView(BreadcrumbMixin, ListView):
    paginate_by = settings.LIST_PAGE_SIZE_DEFAULT
    template_name = "core/entity_list.html"
    ordering = ("title", "name")

    def handle_per_page(self):
        per_page = self.request.GET.get("per_page")

        if per_page:
            try:
                per_page = int(per_page)
                # check back for only allowed-configured list sizes
                if per_page in settings.LIST_PAGE_SIZES:
                    return per_page
                else:
                    return settings.LIST_PAGE_SIZE_DEFAULT
            except ValueError:
                pass

        return self.paginate_by

    def get_paginate_by(self, queryset):
        return self.handle_per_page()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["per_page"] = self.handle_per_page()
        context["per_page_options"] = settings.LIST_PAGE_SIZES

        page: Page = context["page_obj"]
        context["page_range"] = page.paginator.get_elided_page_range(
            page.number, on_each_side=2, on_ends=1
        )

        return context
