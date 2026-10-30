from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin, TabularInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from georama.core.common.admin import OrganisationalModelAdmin
from georama.core.common.request import GeoramaHttpRequest
from georama.core.models.fence import Fence
from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation

admin.site.unregister(Group)

User = get_user_model()


class MembershipInlineAdmin(TabularInline):
    model = Membership


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    inlines = [MembershipInlineAdmin]

    def get_queryset(self, request: GeoramaHttpRequest):
        return (
            super()
            .get_queryset(request)
            .filter(memberships__organisation=request.georama_organisation)
            .prefetch_related("memberships__organisation")
        )


@admin.register(Group)
class DjangoGroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(Membership)
class MembershipAdmin(OrganisationalModelAdmin):
    search_fields = ("user__username", "organisation__name")


@admin.register(Organisation)
class OrganisationAdmin(ModelAdmin):
    inlines = [MembershipInlineAdmin]
    list_display = ["name", "public_access"]


@admin.register(Fence)
class FenceAdmin(OrganisationalModelAdmin):
    pass
