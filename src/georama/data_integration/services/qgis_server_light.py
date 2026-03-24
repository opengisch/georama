import requests
from qgis_server_light.interface.exporter.api import ExportParameters, ExportResult
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.data_integration.lib.data_integration_config import Config


class ExporterService:

    def execute_export(self, mandant_name: str, project_name: str):
        config = Config()
        response = requests.post(
            config.qgis_server_light_exporter_url,
            # Add the dataclass from QSL interface here
            data=JsonSerializer().render(
                ExportParameters(
                    mandant_name,
                    project_name,
                    unify_layer_names_by_group=True,
                    output_format="json",
                )
            ),
            headers={"Content-Type": "application/json"},
        )

        status_report = DictDecoder().decode(response.json(), ExportResult)
        if not status_report.successful:
            raise RuntimeError(f"Something went wrong while exporting, {response.json()}")
