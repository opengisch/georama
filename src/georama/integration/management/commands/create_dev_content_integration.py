import os

from django.core.management.base import BaseCommand

from georama.integration.factories import CustomFactory, RasterFactory, VectorFactory


class Command(BaseCommand):
    help = "Flushes db content of integration app and adds a lot of demo content"

    def handle(self, *args, **options):
        current_config = os.environ.get("DJANGO_CONFIGURATION")

        self.stdout.write(self.style.NOTICE(f"Current Environment: {current_config}"))
        # We only allow this command to run when in dev environment
        if current_config == "Dev":
            VectorFactory.create_batch(150)
            RasterFactory.create_batch(150)
            CustomFactory.create_batch(150)
            self.stdout.write(self.style.SUCCESS("Successfully created development content."))
        else:
            self.stdout.write(
                self.style.ERROR("This command can be used only in Dev environments!")
            )
