import os

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from georama.core.factories import AdminUserFactory, MembershipFactory, UserFactory
from georama.core.models import GeoramaUser
from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation


class Command(BaseCommand):
    help = "Flushes db content of core app and adds a lot of demo content"

    def handle(self, *args, **options):
        current_config = os.environ.get("DJANGO_CONFIGURATION")

        self.stdout.write(self.style.NOTICE(f"Current Environment: {current_config}"))
        # We only allow this command to run when in dev environment
        if current_config == "Dev":
            GeoramaUser.objects.exclude(username="AnonymousUser").all().delete()
            Membership.objects.all().delete()
            Organisation.objects.all().delete()
            Group.objects.all().delete()
            AdminUserFactory.create()
            users = UserFactory.create_batch(50)
            for user in users:
                MembershipFactory(user=user)
            self.stdout.write(self.style.SUCCESS("Successfully created development content."))
        else:
            self.stdout.write(
                self.style.ERROR("This command can be used only in Dev environments!")
            )
