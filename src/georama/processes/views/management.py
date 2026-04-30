from asgiref.sync import sync_to_async
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from qgis_server_light.interface.exporter.extract import Process
from qgis_server_light.interface.job.process.input import (
    ParameterInput,
    QslJobParameterExecuteProcess,
)
from qgis_server_light.interface.job.process.process_list import available
from xsdata.formats.dataclass.parsers import DictDecoder

from georama.core.views.entities.permission_detail import GeoramaPermissionDetailView
from georama.core.views.entities.permission_group import GeoramaGroupListView
from georama.core.views.entities.permission_user import GeoramaUserListView
from georama.core.views.generic.mixins import GeoramaLoginRequiredMixin
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.data_integration.views import PermissionRequiredMixin
from georama.maps.views import (
    GeoramaAnyPermissionRequiredMixin,
    GeoramaEntityListView,
    GeoramaEntityUpdateView,
)
from georama.processes.apps import central_app_label, qsl_redis_queue
from georama.processes.models import PublishedAsDataset, PublishedAsProcess
from georama.webgis.views import (
    GeoramaEntityDeleteView,
    GeoramaEntityDetailView,
    GeoramaEntityPublishListView,
)


class ExecuteProcess(View):
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


class PublishDataset(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    model = PublishedAsDataset
    permission_required = model.perm_add()

    def get(self, request: HttpRequest, dataset_type: str, dataset_id: str):
        """
        helper function to hide actual connection in the database but make
        publishing straight forward.
        """
        if dataset_type == "raster":
            dataset = RasterDataSet.objects.get(id=dataset_id)
            published_as_wms = self.model(raster_dataset=dataset)
        elif dataset_type == "vector":
            dataset = VectorDataSet.objects.get(id=dataset_id)
            published_as_wms = self.model(vector_dataset=dataset)
        elif dataset_type == "custom":
            dataset = CustomDataSet.objects.get(id=dataset_id)
            published_as_wms = self.model(custom_dataset=dataset)
        else:
            raise Http404
        published_as_wms.name = dataset.name
        published_as_wms.title = dataset.title
        published_as_wms.save()

        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(next_url)
        return redirect(f"{central_app_label}:dataset-list")


class PublishDatasetListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityPublishListView
):
    template_name = "processes/publish.html"
    model_publish = PublishedAsDataset
    entity_name = "dataset"
    permission_required = model_publish.perm_add()

    def get_queryset(self):
        items = []
        items += list(VectorDataSet.objects.all())
        items += list(RasterDataSet.objects.all())
        items += list(CustomDataSet.objects.all())
        return items


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


class PublishedAsDatasetPermissionView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaPermissionDetailView
):
    model_entity = PublishedAsDataset
    permission_required = model_entity.perm_manage_permissions()
    entity_name = "dataset"


class PublishedAsDatasetUserListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaUserListView
):
    model_entity = PublishedAsDataset
    permission_required = model_entity.perm_manage_permissions()
    entity_name = "dataset"


class PublishedAsDatasetGroupListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaGroupListView
):
    model_entity = PublishedAsDataset
    permission_required = model_entity.perm_manage_permissions()
    entity_name = "dataset"


class PublishedAsProcessListView(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, GeoramaEntityListView
):
    template_name = "processes/process/entity_list.html"
    model = PublishedAsProcess
    permission_required = [
        model.perm_view(),
        model.perm_change(),
        model.perm_delete(),
        model.perm_add(),
        model.perm_manage_permissions(),
    ]
    entity_name = "process"


class PublishProcess(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    model = PublishedAsProcess
    permission_required = model.perm_add()

    def get(self, request: HttpRequest, process_id: str):
        published_as_process = self.model(process_id=process_id)
        published_as_process.save()

        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(next_url)
        return redirect(f"{central_app_label}:process-list")


class PublishProcessListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityPublishListView
):
    template_name = "processes/process/publish.html"
    model_publish = PublishedAsProcess
    entity_name = "process"
    permission_required = model_publish.perm_add()

    def get_queryset(self):
        process = DictDecoder().decode(available, Process)
        return process.algorithms


class PublishedAsProcessDetailView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityDetailView
):
    model = PublishedAsProcess
    entity_name = "process"
    permission_required = model.perm_view()


class PublishedAsProcessUpdateView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityUpdateView
):
    model = PublishedAsProcess
    entity_name = "process"
    fields = [
        "public",
    ]
    permission_required = model.perm_change()


class PublishedAsProcessDeleteView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaEntityDeleteView
):
    model = PublishedAsProcess
    entity_name = "process"
    permission_required = model.perm_delete()


class PublishedAsProcessPermissionView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaPermissionDetailView
):
    model_entity = PublishedAsProcess
    permission_required = model_entity.perm_manage_permissions()
    entity_name = "process"


class PublishedAsProcessUserListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaUserListView
):
    model_entity = PublishedAsProcess
    permission_required = model_entity.perm_manage_permissions()
    entity_name = "process"


class PublishedAsProcessGroupListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaGroupListView
):
    model_entity = PublishedAsProcess
    permission_required = model_entity.perm_manage_permissions()
    entity_name = "process"
