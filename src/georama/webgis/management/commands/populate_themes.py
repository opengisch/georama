from django.core.management.base import BaseCommand
from django.db import transaction

from georama.webgis import models


def create_interfaces():
    models.Interface.objects.all().delete()

    models.Interface.objects.create(
        name="Desktop",
        description="Interface desktop",
    )

    models.Interface.objects.create(
        name="Mobile",
        description="Interface mobile",
    )


def create_functionalities():
    models.Functionality.objects.all().delete()

    models.Functionality.objects.create(
        name="Functionality A",
        value="Dummy Functionality Value A",
        description="Dummy Functionality Description A",
    )

    models.Functionality.objects.create(
        name="Functionality B",
        value="Dummy Functionality Value B",
        description="Dummy Functionality Description B",
    )


def create_metadatas():

    models.Metadata.objects.all().delete()

    models.Metadata.objects.create(
        name="Test metadata A", description="Metadata fixture A", value="Dummy value A"
    )

    models.Metadata.objects.create(
        name="Test metadata B", description="Metadata fixture B", value="Dummy value B"
    )


def create_ogc_servers():

    models.OgcServer.objects.all().delete()

    models.OgcServer.objects.create(
        name="OGC QGIS Server",
        description="QGIS server",
        url="https://ogc.mapnv.ch/wms-mapnv",
        type="QGIS server",
        image_type="image/png",
        wfs_support=True,
        is_single_tile=True,
    )


def create_themes():

    layergroups = models.LayerGroupMp.objects.all()
    metadatas = models.Metadata.objects.all()
    interfaces = models.Interface.objects.all()
    functionalities = models.Functionality.objects.all()
    models.Theme.objects.all().delete()

    theme_1 = models.Theme.objects.create(
        name="Cadastre",
        icon="cadastre.svg",
        ordering=1,
        public=True,
    )

    theme_1.layergroupmp.set(layergroups)
    theme_1.metadata.set(metadatas)
    theme_1.interface.set(interfaces)
    theme_1.functionality.set(functionalities)

    theme_2 = models.Theme.objects.create(
        name="Environnement",
        icon="environnement.svg",
        ordering=2,
        public=True,
    )

    theme_2.layergroupmp.set(layergroups)
    theme_2.metadata.set(metadatas)
    theme_2.interface.set(interfaces)
    theme_2.functionality.set(functionalities)

    theme_3 = models.Theme.objects.create(
        name="Plan de Ville",
        icon="citymap.svg",
        ordering=3,
        public=True,
    )

    theme_3.layergroupmp.set(layergroups)
    theme_3.metadata.set(metadatas)
    theme_3.interface.set(interfaces)
    theme_3.functionality.set(functionalities)


def create_layers():

    models.Layer.objects.all().delete()
    models.LayerWms.objects.all().delete()
    models.LayerWmts.objects.all().delete()
    interfaces = models.Interface.objects.all()
    metadatas = models.Metadata.objects.all()

    layer_wms = models.Layer.objects.create(name="Layer WMS", public=True)
    layer_wms.interface.set(interfaces)
    layer_wms.metadata.set(metadatas)

    models.LayerWms.objects.all().delete()

    models.LayerWms.objects.create(
        layer=layer_wms,
        ogc_server=models.OgcServer.objects.first(),
    )

    layer_wtms = models.Layer.objects.create(name="Layer WMTS Swisstopo", public=True)
    layer_wtms.interface.set(interfaces)
    layer_wtms.metadata.set(metadatas)

    models.LayerWmts.objects.all().delete()

    models.LayerWmts.objects.create(
        layer=layer_wtms,
    )

    layergroups = models.LayerGroupMp.objects.all()
    layer_wms.layergroupmp.set(layergroups)


def create_layer_groups():

    models.LayerGroupMp.objects.all().delete()

    wms_layer = models.Layer.objects.get(name="Layer WMS")

    root_1 = models.LayerGroupMp.add_root(name="Points d'intérêts")
    root_1.layer.set([wms_layer])
    root_1.add_child(name="Mobilité")
    child_1 = root_1.add_child(name="Transports publics")
    child_1.layer.set([wms_layer])
    child_1.add_child(name="Lignes de bus")
    child_1.add_child(name="Lignes de train")
    root_2 = models.LayerGroupMp.add_root(name="Mensuration")
    root_2.add_child(name="Limites")
    root_2.layer.set([wms_layer])
    child_2 = root_2.add_child(name="Surfaces")
    child_2.add_child(name="Couveture du sol")
    child_2.layer.set([wms_layer])


class Command(BaseCommand):
    help = "Populate basic themes, layer groups and layers"

    @transaction.atomic
    def handle(self, *args, **options):
        create_functionalities()
        create_metadatas()
        create_ogc_servers()
        create_interfaces()
        create_layers()
        create_layer_groups()
        create_themes()

        print(f"👥 added demo themes, layer groups and layers for demo!")
