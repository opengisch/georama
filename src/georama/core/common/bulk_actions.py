from asgiref.sync import sync_to_async
from django.contrib.admin.utils import NestedObjects
from django.db import router as djdb_router
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from guardian.shortcuts import get_objects_for_user
from rest_framework.exceptions import PermissionDenied


class BulkAction:
    """An action which is applied to several selected objects of a list at once.

    A viewset lists the actions it offers in its `bulk_actions` attribute, everything
    else - the radio button in the list, the confirmation step, the permission check and
    the execution - is driven by the action itself. So adding a new action means writing
    one subclass and putting it into the list of the viewsets which should offer it.

    Each step is a method which can be overwritten. Most actions only need `execute`,
    the others are there for the ones which do not fit the default, like the deletion
    which wants to show everything that goes down with the selected objects.

    Attributes:
        name: The value which identifies the action in the form and the API.
        label: The text shown for the action in the list.
        icon_classes: The css classes of the icon shown next to the label.
        action_type: The bootstrap colour of the confirm button.
        confirmation_title: The title of the confirmation step.
        confirmation_text: The text explaining the impact in the confirmation step.
        permissions: The permissions the user needs, either on the model or on each
            selected object. The placeholders `%(app_label)s` and `%(model_name)s` are
            the same as in the `perms_map` of DRF and are filled with the model of the
            queryset, so one action serves every model.
    """

    name: str
    label: str
    icon_classes: str
    action_type: str
    confirmation_title: str
    confirmation_text: str
    permissions: list[str]

    def required_permissions(self, queryset: QuerySet) -> list[str]:
        """Fills the placeholders of the permissions with the model of the queryset.

        Args:
            queryset: The queryset the action runs on.

        Returns:
            The fully qualified permission names.
        """
        kwargs = {
            "app_label": queryset.model._meta.app_label,
            "model_name": queryset.model._meta.model_name,
        }
        return [permission % kwargs for permission in self.permissions]

    async def permitted(self, user, queryset: QuerySet) -> QuerySet:
        """Filters the queryset to the objects the user may run this action on.

        A user holding the model permissions gets all objects, otherwise the object
        permissions decide one by one. Guardian does both in one go for us, so the action
        doesn't need to care which kind of permission was granted.

        Args:
            user: The requesting user.
            queryset: The objects to be filtered.

        Returns:
            The objects the user is permitted to run this action on.
        """
        return await sync_to_async(get_objects_for_user)(
            user, self.required_permissions(queryset), klass=queryset
        )

    async def is_available(self, user, queryset: QuerySet) -> bool:
        """Tells if the action is worth offering in the list at all.

        Args:
            user: The requesting user.
            queryset: The objects of the list.

        Returns:
            True if the user may run the action on at least one object.
        """
        return await (await self.permitted(user, queryset)).aexists()

    async def resolve(self, view, ids: list[str]) -> QuerySet:
        """Turns the selected ids into the objects the action runs on.

        By default these are rows of the viewsets queryset. Actions working on something
        else, like files on disk waiting for their integration, overwrite this.

        Args:
            view: The viewset the action was called on.
            ids: The selected ids.

        Returns:
            The selected objects, filtered the same way the list is.
        """
        queryset = await view.afilter_queryset(view.get_queryset())
        return queryset.filter(pk__in=ids)

    async def check_permissions(self, user, queryset: QuerySet):
        """Makes sure the user may run the action on every selected object.

        We refuse the whole selection rather than silently skipping objects, else a user
        might wonder why half of the selection stayed untouched.

        Args:
            user: The requesting user.
            queryset: The selected objects.

        Raises:
            PermissionDenied: If at least one selected object is not permitted.
        """
        permitted = await self.permitted(user, queryset)
        if await permitted.acount() != await queryset.acount():
            raise PermissionDenied()

    async def preview(self, queryset: QuerySet) -> tuple[list, list]:
        """Collects what the confirmation step shows to the user.

        Args:
            queryset: The selected objects.

        Returns:
            The objects affected by the action and those which block it. By default the
            selected objects are affected and nothing blocks.
        """
        return [obj async for obj in queryset], []

    async def execute(self, request, queryset: QuerySet):
        """Does the actual work, this is the one method every action has to bring.

        Args:
            request: The request which triggered the action, handy for messages.
            queryset: The selected objects, permissions already checked.

        Raises:
            NotImplementedError: If a subclass forgot to implement it.
        """
        raise NotImplementedError


class DeleteBulkAction(BulkAction):
    """Deletes the selected objects, the same way the single delete does."""

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
        """Collects everything which goes down with the selected objects.

        Like the Django admin does it, a deletion shows the cascade and the protected
        objects which would stop it, nobody likes surprises on that one.

        Args:
            queryset: The selected objects.

        Returns:
            The nested related objects and the protected objects.
        """
        collector = NestedObjects(using=djdb_router.db_for_write(queryset.model))
        await sync_to_async(collector.collect)([obj async for obj in queryset])
        return collector.nested(), collector.protected

    async def execute(self, request, queryset: QuerySet):
        await queryset.adelete()


class PublicBulkAction(BulkAction):
    """Base for actions switching the `public` flag of the selected objects. Only offer
    its subclasses on models which have such a flag.

    Attributes:
        public: The value the `public` flag is set to.
    """

    action_type = "warning"
    permissions = ["%(app_label)s.change_%(model_name)s"]
    public: bool

    async def execute(self, request, queryset: QuerySet):
        await queryset.aupdate(public=self.public)


class MakePublicBulkAction(PublicBulkAction):
    """Makes the selected objects publicly accessible."""

    name = "make-public"
    label = _("Make public")
    icon_classes = "fa fa-unlock text-success"
    confirmation_title = _("Confirm making public")
    confirmation_text = _("The following selected items will become publicly accessible:")
    public = True


class MakeNonPublicBulkAction(PublicBulkAction):
    """Takes the public access away from the selected objects."""

    name = "make-non-public"
    label = _("Make non-public")
    icon_classes = "fa fa-lock text-secondary"
    confirmation_title = _("Confirm making non-public")
    confirmation_text = _("The following selected items will no longer be publicly accessible:")
    public = False
