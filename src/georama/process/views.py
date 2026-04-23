from asgiref.sync import sync_to_async
from django.http import HttpResponse
from django.views import View
from qgis_server_light.interface.job.process.input import (
    ParameterInput,
    QslJobParameterExecuteProcess,
)

from georama.core.views.generic.mixins import GeoramaLoginRequiredMixin
from georama.data_integration.models import VectorDataSet
from georama.data_integration.views import PermissionRequiredMixin
from georama.maps.views import (
    GeoramaAnyPermissionRequiredMixin,
    GeoramaEntityListView,
    GeoramaEntityUpdateView,
)
from georama.process.apps import qsl_redis_queue
from georama.process.models import PublishedAsDataset
from georama.webgis.views import (
    GeoramaEntityDeleteView,
    GeoramaEntityDetailView,
    GeoramaEntityPublishListView,
)


class Index(View):
    def get(self, request):
        return HttpResponse("TODO")


class Process(View):
    def retrieve_job_layer_dataset(self):
        test_dataset = VectorDataSet.objects.first()
        return test_dataset.to_qsl_job_layer()

    async def get(self, request):
        # layer = await VectorDataSet.objects.afirst()
        qsl_job_layer = await sync_to_async(
            self.retrieve_job_layer_dataset, thread_sensitive=True
        )()
        job_parameters = QslJobParameterExecuteProcess(
            process_id="native:buffer",
            parameters=[
                ParameterInput("INPUT", qsl_job_layer),
                ParameterInput("DISTANCE", 1.0),
                ParameterInput("OUTPUT", "/tmp/test.geojson"),
                ParameterInput("END_CAP_STYLE", "Round"),
                ParameterInput("JOIN_STYLE", "Round"),
                ParameterInput("MITER_LIMIT", 2.0),
                ParameterInput("DISSOLVE", False),
                ParameterInput("SEPARATE_DISJOINT", False),
            ],
        )
        await qsl_redis_queue.post(job_parameters)
        return HttpResponse("ok")


class PublishedAsDatasetListView(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, GeoramaEntityListView
):
    model = PublishedAsDataset
    permission_required = [
        model.perm_view(),
        model.perm_change(),
        model.perm_delete(),
        model.perm_add(),
        model.perm_manage_permissions(),
    ]
    entity_name = "dataset"


class PublishDatasetListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityPublishListView
):
    model = VectorDataSet
    model_publish = PublishedAsDataset
    entity_name = "dataset"
    permission_required = model_publish.perm_add()


class PublishedAsDatasetDetailView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityDetailView
):
    model = PublishedAsDataset
    entity_name = "dataset"
    permission_required = model.perm_view()


class PublishedAsDatasetUpdateView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityUpdateView
):
    model = PublishedAsDataset
    entity_name = "dataset"
    fields = [
        "title",
        "name",
        "description",
        "public",
    ]
    permission_required = model.perm_change()


class PublishedAsDatasetDeleteView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityDeleteView
):
    model = PublishedAsDataset
    entity_name = "dataset"
    permission_required = model.perm_delete()
