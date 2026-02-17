from django.forms import ModelForm
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from georama.core.menu import BreadCrumb, MenuItem
from georama.core.services.multi_model.base import Service


class FormView(View):
    service: type[Service] = Service
    forms: list[ModelForm] = []
    view_type_name: str = "form"
    name: str
    edit_name: str
    title: str
    edit_template = "core/detail/form.html"
    show_template = "core/detail/show.html"
    app_menu: MenuItem
    breadcrumbs: list[BreadCrumb] = []
    breadcrumb_action_url: str = None
    breadcrumb_action_title: str = None

    def extra_context(self, context: dict, service: Service):
        return context

    def get_form_by_db_object(self, instance, request: HttpRequest | None = None):
        for form in self.forms:
            if form._meta.model == instance._meta.model:
                if request is not None:
                    return form(request.POST, instance=instance)
                else:
                    return form(instance=instance)
        return None

    def get_empty_forms(self):
        forms = []
        for form in self.forms:
            forms.append(form(instance=None))
        return forms

    def get(self, request, pk=None, action=None):
        service = self.service()
        if pk is None:
            forms = self.get_empty_forms()
            instance = None
        else:
            instance = service.get(pk=pk)[0]
            forms = [self.get_form_by_db_object(instance)]
        context = {
            "edit_view_name": f"{self.app_menu.app_label}:{self.edit_name}",
            "instance": instance,
            "forms": forms,
            "breadcrumbs": self.breadcrumbs,
            "breadcrumb_action_url": self.breadcrumb_action_url,
            "breadcrumb_action_title": self.breadcrumb_action_title,
        }
        context.update(self.extra_context(context, service))
        if action == "edit":  # noqa SIM108
            template = self.edit_template
        else:
            template = self.show_template
        return render(request, template, context)

    def post(self, request, pk):
        service = self.service()
        instance = service.get(pk=pk)[0]
        form = self.get_form_by_db_object(instance, request=request)
        if form.is_valid():
            form.save()  # ✅ ORM-Update passiert hier automatisch
            return redirect(f"{self.app_menu.app_label}:{self.name}", pk=pk)
        context = {
            "instance": instance,
            "forms": [form],
            "breadcrumbs": self.breadcrumbs,
            "breadcrumb_action_url": self.breadcrumb_action_url,
            "breadcrumb_action_title": self.breadcrumb_action_title,
        }
        context.update(self.extra_context(context, service))
        return render(request, self.template, {"form": form})
