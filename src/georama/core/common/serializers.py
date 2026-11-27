import base64
import binascii
import struct

from adrf import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.fields import Field, empty

User = get_user_model()


class PngPreviewField(Field):
    PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
    DATA_URL_PREFIX = "data:image/png;base64,"

    def __init__(self, width: int, height: int, **kwargs):
        self.width = width
        self.height = height
        super().__init__(**kwargs)

    def get_value(self, dictionary):
        value = super().get_value(dictionary)
        # an empty form input means something went wrong, we keep the old one
        if value == "":
            return empty
        return value

    def to_representation(self, value):
        return f"{self.DATA_URL_PREFIX}{base64.b64encode(bytes(value)).decode()}"

    def to_internal_value(self, data):
        if not isinstance(data, str) or not data.startswith(self.DATA_URL_PREFIX):
            raise ValidationError(_("The preview must be a PNG image."))
        try:
            image = base64.b64decode(data.removeprefix(self.DATA_URL_PREFIX), validate=True)
        except binascii.Error as error:
            raise ValidationError(_("The preview image could not be decoded.")) from error
        if not image.startswith(self.PNG_SIGNATURE) or len(image) < 24:
            raise ValidationError(_("The preview must be a PNG image."))
        # the PNG header chunk (IHDR) directly follows the signature and holds the dimensions
        width, height = struct.unpack(">II", image[16:24])
        if (width, height) != (self.width, self.height):
            raise ValidationError(
                _("The preview must be %(width)s×%(height)s pixels.")
                % {"width": self.width, "height": self.height}
            )
        return image


class ObjectPermissionSerializer(serializers.Serializer):
    permission_time_created = serializers.DateTimeField(allow_null=True, format=None)
    entity_name = serializers.CharField(read_only=True)
    entity_id = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return self.drop_empty_inherited_permissions(data)

    async def ato_representation(self, instance):
        # this has to be overwritten to async JSNO renders the same content
        # by the serializer
        data = await super().ato_representation(instance)
        return self.drop_empty_inherited_permissions(data)

    @staticmethod
    def drop_empty_inherited_permissions(data):
        if data.get("inherited_permissions", None) is None:
            data.pop("inherited_permissions", None)
        return data


class PermissionActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=[])
    users = serializers.ListField(
        child=serializers.UUIDField(),
        default=list,
    )
    groups = serializers.ListField(
        child=serializers.IntegerField(),
        default=list,
    )


class BulkActionSerializer(serializers.Serializer):
    """Validates a bulk action request against the actions passed as context
    `bulk_actions`. The validated `action` is the matching bulk action itself.
    """

    action = serializers.ChoiceField(choices=[])
    ids = serializers.ListField(child=serializers.CharField(), allow_empty=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bulk_actions = {
            bulk_action.name: bulk_action for bulk_action in self.context["bulk_actions"]
        }
        self.fields["action"].choices = list(self.bulk_actions)

    def validate_action(self, value):
        return self.bulk_actions[value]
