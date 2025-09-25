from django.http import HttpRequest
from django.views import View
from qfieldcloud_sdk import sdk


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
        #     client.download_files(project_files, project['id'], FileTransferType.PROJECT, str(path))


# Create your views here.
