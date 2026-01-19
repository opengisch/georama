import os

from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from qfieldcloud_sdk import sdk
from qfieldcloud_sdk.sdk import FileTransferType


class LinkProjects(View):
    def get(self, request: HttpRequest):
        client = sdk.Client(url="https://app.qfield.cloud/api/v1/")
        client.login(
            username="signedav",
            password="Tdr4.wh0th",
        )
        client.list_projects()

        # for project in projects:
        #     path = os.path.join(settings.DATA_INTEGRATION_ROOT, project['id'])
        #     os.makedirs(path, exist_ok = True)
        #     client.download_project(project['id'], str(path))
        #     project_files = client.list_remote_files(project['id'])
        #     client.download_files(project_files, project['id'], FileTransferType.PROJECT, str(path))  # noqa: E501


# Create your views here.


class QfieldCloudDownloader(View):
    @property
    def qfield_cloud_client(self):
        client = sdk.Client(url=settings.QFIELD_LINK_URL)
        client.login(
            username=settings.QFIELD_LINK_USER,
            password=settings.QFIELD_LINK_PASSWORD,
        )
        return client

    def qfield_cloud_projects(self):
        client = self.qfield_cloud_client
        return client.list_projects()

    def get(self, request: HttpRequest, qfield_cloud_project_id: str):
        client = self.qfield_cloud_client
        path = os.path.join(settings.DATA_INTEGRATION_ROOT, qfield_cloud_project_id)
        os.makedirs(path, exist_ok=True)
        client.download_project(qfield_cloud_project_id, str(path))
        project_files = client.list_remote_files(qfield_cloud_project_id)
        client.download_files(
            project_files, qfield_cloud_project_id, FileTransferType.PROJECT, str(path)
        )
        return redirect("admin:data_integration_qgis_projects")
