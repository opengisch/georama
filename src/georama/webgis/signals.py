from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from georama.webgis.models.theme import Theme, ThemeGroupObjectPermission, ThemeUserObjectPermission


@receiver([post_save, post_delete], sender=ThemeUserObjectPermission)
@receiver([post_save, post_delete], sender=ThemeGroupObjectPermission)
def refresh_theme_editable_layers(sender, instance, **kwargs):
    theme = Theme.objects.filter(pk=instance.content_object_id).first()
    if theme is not None:
        theme.refresh_editable_layers()
