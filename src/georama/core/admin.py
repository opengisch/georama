from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, TabularInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from georama.core.common.admin import OrganisationalModelAdmin
from georama.core.common.request import GeoramaHttpRequest
from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation

admin.site.unregister(Group)

User = get_user_model()


class MembershipInlineAdmin(TabularInline):
    model = Membership


class ProviderAccountListFilter(admin.SimpleListFilter):
    """Tells local accounts apart from accounts linked to an identity provider. The
    unlinked ones with an email are the ones whose first provider login ends on the
    signup form, as long as GEORAMA_OIDC_EMAIL_AUTHENTICATION is off.
    """

    title = _("provider account")
    parameter_name = "provider_account"

    def lookups(self, request, model_admin):
        return [("linked", _("linked")), ("not_linked", _("not linked"))]

    def queryset(self, request, queryset):
        if self.value() == "linked":
            return queryset.filter(socialaccount__isnull=False).distinct()
        if self.value() == "not_linked":
            return queryset.filter(socialaccount__isnull=True)
        return queryset


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    inlines = [MembershipInlineAdmin]
    list_display = (*BaseUserAdmin.list_display, "provider_accounts")
    list_filter = (*BaseUserAdmin.list_filter, ProviderAccountListFilter)

    def get_queryset(self, request: GeoramaHttpRequest):
        return (
            super()
            .get_queryset(request)
            .filter(memberships__organisation=request.georama_organisation)
            .prefetch_related("memberships__organisation", "socialaccount_set")
        )

    @admin.display(description=_("provider account"))
    def provider_accounts(self, user) -> str:
        """Shows which identity providers a user is linked to, a dash for a local
        account only.

        Args:
            user: The user of the row.

        Returns:
            The provider ids, comma separated.
        """
        return ", ".join(account.provider for account in user.socialaccount_set.all()) or "–"

    def get_readonly_fields(self, request, obj=None):
        """Make is_superuser read-only for non-superuser staff members."""
        readonly_fields = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            return (*readonly_fields, "is_superuser")
        return readonly_fields


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
