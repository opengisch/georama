from asgiref.sync import sync_to_async
from django.contrib.admin.utils import NestedObjects
from django.db import router as djdb_router
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from guardian.shortcuts import get_objects_for_user
from rest_framework.exceptions import PermissionDenied


class BulkAction:
    """An action which is applied to several selected objects of a list at once.

    Attributes:
        name: The value which identifies the action in the form and the API.
        label: The text shown for the action in the list.
        icon_classes: The css classes of the icon shown next to the label.
        action_type: The bootstrap colour of the confirm button.
        confirmation_title: The title of the confirmation step.
        confirmation_text: The text explaining the impact in the confirmation step.
        permissions: The permissions the user needs, either on the model or on each
            selected object. Placeholders `%(app_label)s` and `%(model_name)s` are
            filled with the model of the queryset.
    """

    name: str
    label: str
    icon_classes: str
    action_type: str
    confirmation_title: str
    confirmation_text: str
    permissions: list[str]

    def required_permissions(self, queryset: QuerySet) -> list[str]:
        kwargs = {
            "app_label": queryset.model._meta.app_label,
            "model_name": queryset.model._meta.model_name,
        }
        return [permission % kwargs for permission in self.permissions]

    async def permitted(self, user, queryset: QuerySet) -> QuerySet:
        """Model permissions grant all objects, otherwise object permissions decide."""
        return await sync_to_async(get_objects_for_user)(
            user, self.required_permissions(queryset), klass=queryset
        )

    async def is_available(self, user, queryset: QuerySet) -> bool:
        return await (await self.permitted(user, queryset)).aexists()

    async def resolve(self, view, ids: list[str]) -> QuerySet:
        queryset = await view.afilter_queryset(view.get_queryset())
        return queryset.filter(pk__in=ids)

    async def check_permissions(self, user, queryset: QuerySet):
        permitted = await self.permitted(user, queryset)
        if await permitted.acount() != await queryset.acount():
            raise PermissionDenied()

    async def preview(self, queryset: QuerySet) -> tuple[list, list]:
        """Returns the objects affected by the action and those which block it."""
        return [obj async for obj in queryset], []

    async def execute(self, request, queryset: QuerySet):
        raise NotImplementedError


class DeleteBulkAction(BulkAction):
    name = "delete"
    label = _("Delete")
    icon_classes = "fa fa-trash-alt text-danger"
    action_type = "danger"
    confirmation_title = _("Confirm deletion")
    confirmation_text = _(
        "Removing the selected items has an impact on the following content in Georama:"
    )
    permissions = ["%(app_label)s.delete_%(model_name)s"]

    async def preview(self, queryset: QuerySet) -> tuple[list, list]:
        collector = NestedObjects(using=djdb_router.db_for_write(queryset.model))
        await sync_to_async(collector.collect)([obj async for obj in queryset])
        return collector.nested(), collector.protected

    async def execute(self, request, queryset: QuerySet):
        await queryset.adelete()


class PublicBulkAction(BulkAction):
    """Base for actions switching the `public` flag of the selected objects.

    Attributes:
        public: The value the `public` flag is set to.
    """

    action_type = "warning"
    permissions = ["%(app_label)s.change_%(model_name)s"]
    public: bool

    async def execute(self, request, queryset: QuerySet):
        await queryset.aupdate(public=self.public)


class MakePublicBulkAction(PublicBulkAction):
    name = "make-public"
    label = _("Make public")
    icon_classes = "fa fa-unlock text-success"
    confirmation_title = _("Confirm making public")
    confirmation_text = _("The following selected items will become publicly accessible:")
    public = True


class MakeNonPublicBulkAction(PublicBulkAction):
    name = "make-non-public"
    label = _("Make non-public")
    icon_classes = "fa fa-lock text-secondary"
    confirmation_title = _("Confirm making non-public")
    confirmation_text = _("The following selected items will no longer be publicly accessible:")
    public = False
