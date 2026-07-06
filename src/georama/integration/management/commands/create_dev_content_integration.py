import os
from importlib import import_module

import psycopg
from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker
from faker.utils.loading import find_available_providers

from georama.core.common.faker.gis import Dataset
from georama.integration.factories import CustomFactory, FieldFactory, RasterFactory, VectorFactory
from georama.integration.models import Datasource, Vector, VectorField, Project

META_PROVIDERS_MODULES = [
    "georama.core.common.faker",
]

PROVIDERS = find_available_providers([import_module(path) for path in META_PROVIDERS_MODULES])

fake = Faker(locale="de_CH", providers=PROVIDERS)


class Command(BaseCommand):
    help = "Flushes db content of integration app and adds a lot of demo content"

    @property
    def get_psycopg_context(self):
        return psycopg.connect(
            dbname=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PW,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
        )

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
            with self.get_psycopg_context as conn, conn.cursor() as cur:
                cur.execute(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE;")
                conn.commit()
                cur.execute(f"CREATE SCHEMA {schema_name};")
                conn.commit()
                for dataset in datasets:
                    cur.execute(dataset.create_table_sql)
                    cur.execute(dataset.insert_values_sql)
                    conn.commit()
            for dataset in datasets:
                vd = VectorFactory.create(
                    name=dataset.name,
                    geometry_type_wkb=dataset.geometry_type_wkb,
                    geometry_type_simple=dataset.geometry_type_simple,
                    crs={
                        "auth_id": f"EPSG:{dataset.epsg_id}",
                        "ogc_uri": f"http://www.opengis.net/def/crs/EPSG/0/{dataset.epsg_id}",
                        "ogc_urn": f"urn:ogc:def:crs:EPSG::{dataset.epsg_id}",
                        "postgis_srid": dataset.epsg_id,
                    },
                    driver="postgres",
                    source={
                        "ogr": None,
                        "wfs": None,
                        "wms": None,
                        "xyz": None,
                        "gdal": None,
                        "wmts": None,
                        "postgres": {
                            "key": "id",
                            "sql": None,
                            "host": settings.DB_HOST,
                            "port": settings.DB_PORT,
                            "srid": f"{dataset.epsg_id}",
                            "type": None,
                            "table": dataset.table_name.lower(),
                            "dbname": settings.DB_NAME,
                            "schema": schema_name,
                            "service": None,
                            "sslmode": 0,
                            "password": settings.DB_PW,
                            "username": settings.DB_USER,
                            "ssl_mode_text": "prefer",
                            "geometry_column": dataset.geometry_field_name,
                            "check_primary_key_unicity": None,
                        },
                        "vector_tile": None,
                    },
                    styles={},
                    bbox="{},{},{},{}".format(*fake.bounds()),
                    bbox_wgs84="{},{},{},{}".format(*fake.bounds_wgs84()),
                    fields=[],
                )
                fields = []
                for field in dataset.selected_fields:
                    fields.append(
                        FieldFactory(
                            datasource=vd,
                            name=field.name,
                            type=field.type,
                            alias=field.alias,
                            nullable=field.nullable,
                            type_oapif=field.type_oapif,
                            is_primary_key=field.is_primary_key,
                            length=field.length,
                            precision=field.precision,
                            type_oapif_format=field.type_oapif_format,
                            type_wfs=field.type_wfs,
                            comment=field.comment,
                        )
                    )

            RasterFactory.create_batch(150)
            CustomFactory.create_batch(150)
            self.stdout.write(self.style.SUCCESS("Successfully created development content."))
        else:
            self.stdout.write(
                self.style.ERROR("This command can be used only in Dev environments!")
            )
