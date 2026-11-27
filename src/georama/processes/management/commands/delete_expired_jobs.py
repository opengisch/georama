from django.core.management.base import BaseCommand, CommandError
from django.db import OperationalError, ProgrammingError

from georama.processes.models.job import Job


class Command(BaseCommand):
    help = "Deletes expired process jobs together with their output dir"

    def handle(self, *args, **options):
        try:
            _, deleted_by_model = Job.objects.expired().delete()
        except (OperationalError, ProgrammingError) as error:
            # an unreachable database or missing migrations are no reason for a
            # traceback, the caller gets a clean message and a failing exit code
            raise CommandError(
                f"Database not reachable or not migrated, no jobs deleted: {error}"
            ) from error
        deleted = deleted_by_model.get(Job._meta.label, 0)
        self.stdout.write(self.style.SUCCESS(f"Deleted {deleted} expired jobs"))
