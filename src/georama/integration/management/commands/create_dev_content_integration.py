import os
from importlib import import_module
from typing import TYPE_CHECKING

import psycopg
from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker
from faker.utils.loading import find_available_providers

from georama.integration.builders import create_dataset_table, create_vector_from_dataset
from georama.integration.factories import CustomFactory, RasterFactory
from georama.integration.models import Datasource, Project, Vector, VectorField

if TYPE_CHECKING:
    from georama.core.common.faker.gis import Dataset

META_PROVIDERS_MODULES = [
    "georama.core.common.faker",
]

PROVIDERS = find_available_providers([import_module(path) for path in META_PROVIDERS_MODULES])

fake = Faker(locale="de_CH", providers=PROVIDERS)


class Command(BaseCommand):
    help = "Flushes db content of integration app and adds a lot of demo content"

    @property
    def db_settings(self) -> dict:
        return {
            "dbname": settings.DB_NAME,
            "user": settings.DB_USER,
            "password": settings.DB_PW,
            "host": settings.DB_HOST,
            "port": settings.DB_PORT,
        }

    def handle(self, *args, **options):
        current_config = os.environ.get("DJANGO_CONFIGURATION")

        self.stdout.write(self.style.NOTICE(f"Current Environment: {current_config}"))
        # We only allow this command to run when in dev environment
        if current_config == "Dev":
            # deleting old content
            Project.objects.all().delete()
            Datasource.objects.all().delete()
            Vector.objects.all().delete()
            VectorField.objects.all().delete()

            schema_name = "dummy"
            datasets: list[Dataset] = fake.vector_datasets(schema_name, amount=150)
            with psycopg.connect(**self.db_settings) as conn, conn.cursor() as cur:
                cur.execute(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE;")
                conn.commit()
                cur.execute(f"CREATE SCHEMA {schema_name};")
                conn.commit()
                for dataset in datasets:
                    create_dataset_table(cur, dataset)
                    conn.commit()
            for dataset in datasets:
                create_vector_from_dataset(
                    dataset, schema_name, self.db_settings, fake.bounds(), fake.bounds_wgs84()
                )

            RasterFactory.create_batch(150)
            CustomFactory.create_batch(150)
            self.stdout.write(self.style.SUCCESS("Successfully created development content."))
        else:
            self.stdout.write(
                self.style.ERROR("This command can be used only in Dev environments!")
            )
