from django.core.management.base import BaseCommand

from georama.processes.models.job import Job


class Command(BaseCommand):
    help = "Deletes expired process jobs together with their output dir"

    def handle(self, *args, **options):
        _, deleted_by_model = Job.objects.expired().delete()
        deleted = deleted_by_model.get(Job._meta.label, 0)
        self.stdout.write(self.style.SUCCESS(f"Deleted {deleted} expired jobs"))
