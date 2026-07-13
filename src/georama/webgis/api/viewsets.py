from django.apps import apps
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action

from georama.core.common.api import (
    GeoramaManagerViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.models import Project
from georama.webgis.api.serializers import ThemeSerializer
from georama.webgis.models import Metadata, Theme


class ManageThemeViewSet(GeoramaManagerViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []

    @property
    async def bread_crumb_action_context(self):
        """Prepares the breadcrumb action to add a theme.

        Returns:
            The context with an action to add a new theme in case the user has add-permission
            on the theme model and is permitted to view projects.
        """
        context = {}
        perm_checker = GeoramaModelPermissions()
        # post is the DRF method which is used for add/create a new object
        local_perms = perm_checker.get_required_permissions("POST", self.queryset.model)
        # we also check if the remote data can be used (view)
        remote_perms = perm_checker.get_required_permissions("GET", Project)
        if all(
            [
                await self.request.user.ahas_perms(local_perms),
                await self.request.user.ahas_perms(remote_perms),
            ]
        ):
            context["breadcrumb_action"] = BreadcrumbAction(
                url=reverse("integration:manager-project-list"),
                tooltip=_("Publish a Project as Theme"),
                hint=_("Select a project to publish it as a new Theme"),
                title=_("Theme"),
                type=ActionType.EMBEDDED,
                icon="fa fa-circle-plus",
            )
        return context

    @staticmethod
    async def transfer_to_theme(project: Project):
        highest_theme = Theme.objects.order_by("ordering").last()
        metadata = Metadata(title=project.name)

        theme = Theme(
            project=project,
            metadata=metadata,
            public=False,
            ordering=highest_theme.ordering + 1 if highest_theme else 1,
            zoom=4,
            # temporarily we set this
            theme_json={},
        )
        await theme.asave()

    @property
    def publish_from_project_url_name(self):
        return self.url_name("publish-from-project")

    @action(detail=False, methods=["post"], url_path="publish_from_project")
    async def publish_from_project(self, request: GeoramaDrfRequest, *args, **kwargs):
        qs = Project.objects.organisation_objects(request.georama_organisation)
        project = qs.aget(id=request.data["pk"])  # noqa: F841
        return redirect(reverse(self.url_name_list))


class ThemeViewSet(GeoramaObjPermViewSetReadOnly):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    required_obj_perms = ["webgis.view_published_theme"]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]
