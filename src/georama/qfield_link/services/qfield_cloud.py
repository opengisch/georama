import os

from django.conf import settings
from qfieldcloud_sdk import sdk
from qfieldcloud_sdk.sdk import FileTransferType


class ApiService:

    def __init__(self):
        self.client = sdk.Client(url=settings.QFIELD_LINK_URL)
        self.client.login(
            username=settings.QFIELD_LINK_USER,
            password=settings.QFIELD_LINK_PASSWORD,
        )

    def get_project_list(self):
        return self.client.list_projects()

    def download_project(self, qfield_cloud_project_id):
        path = os.path.join(settings.DATA_INTEGRATION_ROOT, qfield_cloud_project_id)
        os.makedirs(path, exist_ok=True)
        self.client.download_project(qfield_cloud_project_id, str(path))
        project_files = self.client.list_remote_files(qfield_cloud_project_id)
        self.client.download_files(
            project_files, qfield_cloud_project_id, FileTransferType.PROJECT, str(path)
        )
