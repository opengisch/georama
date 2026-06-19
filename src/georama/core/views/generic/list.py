import logging

from django.conf import settings
from django.core.paginator import Page
from django.views.generic import ListView

from georama.core.views.generic.mixins import BreadcrumbMixin


class GeoramaListView(BreadcrumbMixin, ListView):
    paginate_by = settings.LIST_PAGE_SIZE_DEFAULT
    template_name = "core/entity_list.html"
    ordering = ("title",)
    sortable_by = ("title", "name")

    def get_ordering(self):
        """Return the field or fields to use for ordering the queryset."""
        sort_request = self.request.GET.get("sort")
        if sort_request is not None:
            valid_keys = set().union(*({s, f"-{s}"} for s in self.sortable_by))
            return [k for k in sort_request.split(",") if k in valid_keys]
        return self.ordering

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
        current_ordering = self.get_ordering()
        context["sort"] = ",".join(current_ordering)
        # We want the web interface to only show the first element, so that clicking on a sort
        # button is mutually exclusive of the others
        # Remove the following line for multiple sorting options accepted in the UI
        current_ordering = set(ordering[:1]) if (ordering := self.get_ordering()) else set()
        context["sort_options"] = []
        for field in self.sortable_by:
            if field in current_ordering:
                direction = "ascending"
                # Uncomment for multiple sorting options accepted in the UI
                # new_ordering -= {field}
                # new_ordering |= {f"-{field}"}
                new_ordering = {f"-{field}"}
            elif f"-{field}" in current_ordering:
                direction = "descending"
                # Uncomment for multiple sorting options accepted in the UI
                # new_ordering -= {f"-{field}"}
                new_ordering = set()
            else:
                direction = None
                # Uncomment for multiple sorting options accepted in the UI
                # new_ordering |= {field}
                new_ordering = {field}
            name = self.model._meta.get_field(field).verbose_name if self.model else field
            context["sort_options"].append(
                {
                    "name": name,
                    "field": field,
                    "direction": direction,
                    "qs": ",".join(new_ordering),
                }
            )
            logging.debug(context["sort_options"])
        context["per_page"] = self.handle_per_page()
        context["per_page_options"] = settings.LIST_PAGE_SIZES

        page: Page = context["page_obj"]
        context["page_range"] = page.paginator.get_elided_page_range(
            page.number, on_each_side=2, on_ends=1
        )

        return context
