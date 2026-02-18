from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import migrations

from georama.qfield_link.apps import central_app_label


def create_app_permission(apps, schema_editor):
    content_type, _ = ContentType.objects.get_or_create(
        app_label=central_app_label, model="qfield_link_permission"
    )
    Permission.objects.create(
        codename="can_use_app",
        name="Can use the QFieldLinkApp",
        content_type=content_type,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("data_integration", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_app_permission),
    ]
