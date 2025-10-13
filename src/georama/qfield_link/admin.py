from django.conf import settings
from django.contrib import admin

# Dummy Model ohne DB-Tabelle
from django.db import models
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path
from qfieldcloud_sdk import sdk


class QfieldCloudProject(models.Model):
    class Meta:
        managed = False
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class QfieldCloudProjectAdmin(admin.ModelAdmin):
    change_list_template = "admin/qfield_link/projects.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "qfield_link_projects/",
                self.admin_site.admin_view(self.run_task),
                name="qfield_link_projects",
            ),
        ]
        return custom_urls + urls

    @property
    def qfield_cloud_client(self):
        client = sdk.Client(url=settings.QFIELD_LINK_URL)
        client.login(
            username=settings.QFIELD_LINK_USER,
            password=settings.QFIELD_LINK_PASSWORD,
        )
        return client

    def qfield_cloud_projects(self):
        client = self.qfield_cloud_client
        return client.list_projects()

    def changelist_view(self, request, extra_context=None):
        opts = self.model._meta
        extra_context = extra_context or {}
        extra_context["title"] = "Project"
        extra_context["qfield_cloud_projects"] = self.qfield_cloud_projects()
        extra_context["opts"] = opts
        extra_context["app_label"] = opts.app_label
        return TemplateResponse(request, self.change_list_template, extra_context)

    def run_task(self, request, extra_context=None):
        # Hier führst du deine Funktion aus
        print("Custom Task wurde ausgeführt!")
        self.message_user(request, "Aufgabe erfolgreich ausgeführt!")
        return HttpResponseRedirect("../")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True


if settings.QFIELD_LINK_URL and settings.QFIELD_LINK_USER and settings.QFIELD_LINK_PASSWORD:
    admin.site.register(QfieldCloudProject, QfieldCloudProjectAdmin)
