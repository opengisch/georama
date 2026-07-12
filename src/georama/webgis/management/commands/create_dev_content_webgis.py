import os
import random

from django.contrib.auth import get_user_model
from django.contrib.auth.models import ContentType
from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand
from django.db import transaction
from guardian.shortcuts import assign_perm

from georama.integration.models import Vector
from georama.webgis.factories import WmsLayerFactory
from georama.webgis.models import Theme

User = get_user_model()


class Command(BaseCommand):
    help = "Flushes db content of integration app and adds a lot of demo content"

    @transaction.atomic
    def handle(self, *args, **options):
        current_config = os.environ.get("DJANGO_CONFIGURATION")

        self.stdout.write(self.style.NOTICE(f"Current Environment: {current_config}"))
        # We only allow this command to run when in dev environment
        if current_config == "Dev":
            Theme.objects.all().delete()
            users = User.objects.all()
            permissions = Permission.objects.filter(
                content_type=ContentType.objects.get_for_model(Theme)
            )

            for vd in Vector.objects.all():
                WmsLayerFactory.create(datasource=vd)
            # Assign on average two permissions per user
            themes = Theme.objects.all()
            for _ in range(len(permissions) * len(users)):
                user = random.choice(users)
                feature_layer = random.choice(themes)
                permission = random.choice(permissions)
                assign_perm(permission, user, feature_layer)

            self.stdout.write(
                self.style.SUCCESS("Successfully created development content.")
            )
        else:
            self.stdout.write(
                self.style.ERROR("This command can be used only in Dev environments!")
            )
