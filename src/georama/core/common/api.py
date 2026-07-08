import json

from adrf import viewsets
from asgiref.sync import sync_to_async
from django.apps import apps
from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.db import router as djdb_router
from django.forms import ModelForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from drf_spectacular.plumbing import build_mock_request as original_build_mock_request
from rest_framework import filters, renderers, status
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from georama.core.common.menu import Breadcrumb
from georama.core.common.request import GeoramaDrfRequest
from georama.core.patches.adrf import pagination


class GeoramaModelPermissions(DjangoModelPermissions):
    """A permission which also checks view permission on read endpoints."""

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": ["%(app_label)s.view_%(model_name)s"],
        "HEAD": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


def build_mock_request(method, path, view, original_request, **kwargs):
    """we need to hook in here since the generator for schemas seem to not
    transport all attributes (DRF SPectacular), this method is configured in the
    settings py then!
    """
    request = original_build_mock_request(method, path, view, original_request, **kwargs)
    if original_request:
        request.georama_organisation = original_request.georama_organisation
    return request


class GeoramaPartialsRenderer(renderers.TemplateHTMLRenderer):
    media_type = "text/html"
    format = "p-html"


class GeoramaAsyncTemplateModelViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    renderer_classes = [
        renderers.TemplateHTMLRenderer,
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        GeoramaPartialsRenderer,
    ]
    list_template_name: str = "core/drf/default/list.html"
    partial_list_template_name: str = "core/drf/default/partials/list.html"
    form_template_name: str = "core/drf/default/form.html"
    form: ModelForm
    show_template_name: str = "core/drf/default/detail.html"
    delete_template_name: str = "core/drf/default/delete_preview.html"

    def url_name(self, action):
        """
        Reverse the action for the given `url_name`.
        """
        url_name = f"{self.basename}-{action}"
        url_name = self.queryset.model._meta.app_label + ":" + url_name
        return url_name

    @property
    def url_name_list(self):
        return self.url_name("list")

    async def _prepare_many_context(self):
        search_fields = getattr(self, "search_fields", [])
        context = {
            "per_page_options": settings.LIST_PAGE_SIZES,
            # this is how the filters.SearchFilter does it too
            "search_fields": search_fields,
            "search_param": filters.SearchFilter.search_param,
            "search_fields_hint": _(f"searchable fields: {', '.join(search_fields)}"),
            "ordering_param": filters.OrderingFilter.ordering_param,
            "breadcrumbs": await self.get_breadcrumbs(),
            "view": self,
        }
        return context

    async def alist(self, request, *args, **kwargs):
        if request.accepted_renderer.format in ["html", "p-html"]:
            qs = self.filter_queryset(self.get_queryset())
            context = await self._prepare_many_context()
            ordering = filters.OrderingFilter()
            ordering_current_direction = ordering.get_ordering(request, qs, self) or []
            ordering_context = {}
            for o in ordering_current_direction:
                direction = "descending" if o.startswith("-") else "ascending"
                field = o.removeprefix("-")
                ordering_context[field] = {
                    "name": field,
                    "direction": direction,
                }
            # this is how the filters.OrderingFilter does it too
            for field in getattr(self, "ordering_fields", []):
                if field not in ordering_context:
                    ordering_context[field] = {"name": field, "direction": None}
            pqs = await self.apaginate_queryset(qs)
            context["object_list"] = pqs
            context["limit"] = self.paginator.limit
            ordering_context_list = [v for _, v in ordering_context.items()]
            ordering_context_list.sort(key=lambda d: d["name"])
            context["ordering_context"] = ordering_context_list
            context["ordering_context_json"] = json.dumps(ordering_context)
            context.update(await self._get_model_permissions())
            context.update(self.paginator.get_html_context())
            if request.accepted_renderer.format == "html":
                return Response(context, template_name=self.list_template_name)
            else:
                return Response(context, template_name=self.partial_list_template_name)
        else:
            return await super().alist(request, *args, **kwargs)

    async def _get_model_permissions(self):
        user = self.request.user
        opts = self.queryset.model._meta
        return {
            "can_add": user.has_perm(f"{opts.app_label}.add_{opts.model_name}"),
            "can_change": user.has_perm(f"{opts.app_label}.change_{opts.model_name}"),
            "can_delete": user.has_perm(f"{opts.app_label}.delete_{opts.model_name}"),
        }

    async def _prepare_single_context(self):
        instance = await self.aget_object()
        breadcrumbs = await self.get_breadcrumbs()
        breadcrumbs[-1].view_name = self.reverse_action("list")
        breadcrumbs += [Breadcrumb(str(instance))]
        context = {
            "object": instance,
            "view": self,
            "breadcrumbs": breadcrumbs,
        }
        context.update(await self._get_model_permissions())
        return context

    async def aretrieve(self, request: GeoramaDrfRequest, *args, **kwargs):
        """Handles the standard retrieve of a model view
        but returns a form in case of HTML format
        """
        if request.accepted_renderer.format == "html":
            context = await self._prepare_single_context()
            context["form"] = self.form(instance=context["object"])
            return Response(context, template_name=self.form_template_name)
        else:
            return await super().aretrieve(request, *args, **kwargs)

    @property
    def url_name_retrieve(self):
        return self.url_name("detail")

    @action(
        detail=True,
        methods=["post"],
        name="Update instance with a form request",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def aform_update(self, request, *args, **kwargs):
        await self.aupdate(request, *args, **kwargs)
        instance = await self.aget_object()
        return redirect(reverse("core:georamauser-detail", kwargs={"pk": instance.pk}))

    @action(
        detail=True,
        methods=["get"],
        name="Show instance read only",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def ashow(self, request, *args, **kwargs):
        """Shows a read only representation of the detail."""
        context = await self._prepare_single_context()
        return Response(context, template_name=self.show_template_name)

    @property
    def url_name_show(self):
        return self.url_name("ashow")

    @action(
        detail=False,
        methods=["get"],
        name="Add new instance",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def aadd(self, request, *args, **kwargs):
        """Shows an empty form to create a new item or the default list."""
        context = {
            "view": self,
            "breadcrumbs": await self.get_breadcrumbs(),
        }
        context.update(await self._get_model_permissions())
        context["form"] = self.form()
        return Response(context, template_name=self.form_template_name)

    @property
    def url_name_add(self):
        return self.url_name("aadd")

    @action(
        detail=True,
        methods=["get", "post"],
        name="Delete an instance",
        renderer_classes=[renderers.TemplateHTMLRenderer],
    )
    async def adelete_confirm(self, request, *args, **kwargs):
        """Shows a confirmation dialog before data is actually deleted"""
        context = await self._prepare_single_context()
        using = djdb_router.db_for_write(self.queryset.model)
        collector = NestedObjects(using=using)
        await sync_to_async(collector.collect)([context["object"]])
        context["expected_status"] = status.HTTP_204_NO_CONTENT
        context["related_objects"] = collector.nested()
        context["protected"] = collector.protected
        return Response(context, template_name=self.delete_template_name)

    @property
    def url_name_delete_confirm(self):
        return self.url_name("adelete-confirm")

    async def adestroy(self, request, *args, **kwargs):
        response = await super().adestroy(request, *args, **kwargs)
        if request.accepted_renderer.format == "html":
            if response.status_code == status.HTTP_204_NO_CONTENT:
                response = redirect(self.url_name_list)
            else:
                response = redirect(self.url_name_delete_confirm, self.get_object().pk)
            # we set this, so the browser can change http method to get
            # (https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Redirections#temporary_redirections)
            response.status_code = status.HTTP_303_SEE_OTHER
            return response
        else:
            return response

    @property
    def url_name_destroy(self):
        return self.url_name("detail")

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title, reverse(f"{self.queryset.model._meta.app_label}:index")),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]


class OrganisationalModelViewSet(viewsets.ModelViewSet):
    """
    A DRF ViewSet which uses organisational bound tables to filter automatically for
    only organisations defined by the request.

    Attributes:
        request: The normal rest_framework.request.Request which is extended by the
            georama.core.middleware.organisation.OrganisationMiddleware with the
            georama_organisation attribute.
    """

    request: GeoramaDrfRequest

    def get_queryset(self):
        """
        The queryset is automatically filtered by the organisation.

        Returns:
            The filtered queryset.
        """
        qs = super().get_queryset()
        return qs.organisation_objects(self.request.georama_organisation)
