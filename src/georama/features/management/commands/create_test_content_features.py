import os

from django.core.management.base import BaseCommand
from django.db import transaction

from georama.features.builders import create_test_feature_layer
from georama.integration.builders import create_test_point_vector, create_test_project


class Command(BaseCommand):
    help = "Flushes db content of integration app and adds a lot of demo content"

    @transaction.atomic
    def handle(self, *args, **options):
        current_config = os.environ.get("DJANGO_CONFIGURATION")

        self.stdout.write(self.style.NOTICE(f"Current Environment: {current_config}"))
        # We only allow this command to run when in dev environment
        create_test_feature_layer(create_test_point_vector(create_test_project()))
