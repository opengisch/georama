from django.contrib import admin

# Dummy Model ohne DB-Tabelle
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import path


class TaskRunner(models.Model):
    class Meta:
        managed = False
        verbose_name = "Aufgabe ausführen"
        verbose_name_plural = "Aufgaben"


class TaskRunnerAdmin(admin.ModelAdmin):
    change_list_template = "admin/qfield_link/projects.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("run/", self.admin_site.admin_view(self.run_task), name="orders-run-task"),
        ]
        return custom_urls + urls

    def run_task(self, request):
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


admin.site.register(TaskRunner, TaskRunnerAdmin)
