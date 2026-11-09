from dataclasses import replace

from asgiref.sync import sync_to_async
from qgis_server_light.interface.job.process.description import (
    InputDescription,
    ProcessDescription,
    ProcessDescriptions,
    QslLayerMarker,
    Schema,
)
from qgis_server_light.interface.job.process.input import ParameterInput

from georama.processes.models.process_input import ProcessInput


class LayerInputMapper:
    """Offers process inputs to the layer inputs of process descriptions. QSL marks the
    schema of a layer input with `x-qsl-layer`, the mapper replaces it with the process
    inputs which fit the marker, as `oneOf` of `{const, title}`.
    """

    def __init__(self, process_inputs: list[ProcessInput]):
        self.process_inputs = process_inputs

    def map_process_descriptions(
        self, process_descriptions: ProcessDescriptions
    ) -> ProcessDescriptions:
        return replace(
            process_descriptions,
            processes=[
                self.map_process_description(process_description)
                for process_description in process_descriptions.processes
            ],
        )

    def map_process_description(
        self, process_description: ProcessDescription
    ) -> ProcessDescription:
        return replace(
            process_description,
            inputs=[
                self.map_input_description(input_description)
                for input_description in process_description.inputs
            ],
        )

    def map_input_description(self, input_description: InputDescription) -> InputDescription:
        if input_description.schema.x_qsl_layer is None:
            return input_description
        return replace(input_description, schema=self.map_schema(input_description.schema))

    async def amap_parameter_inputs(
        self, process_description: ProcessDescription, values: dict
    ) -> list[ParameterInput]:
        layer_markers = {
            input_description.id: input_description.schema.x_qsl_layer
            for input_description in process_description.inputs
        }
        return [
            ParameterInput(name=name, value=await self.amap_value(layer_markers[name], value))
            for name, value in values.items()
            # a layer input which was left empty is not passed to the process
            if layer_markers[name] is None or value
        ]

    async def amap_value(self, layer_marker: QslLayerMarker | None, value):
        if layer_marker is None:
            return value
        fitting_process_inputs = {
            process_input.identifier: process_input
            for process_input in self.process_inputs
            if process_input.fits(layer_marker)
        }
        return await sync_to_async(fitting_process_inputs[value].to_qsl_job_layer)()

    def map_schema(self, schema: Schema) -> Schema:
        return replace(
            schema,
            format=None,
            x_qsl_layer=None,
            one_of=[
                Schema(const=process_input.identifier, title=process_input.title)
                for process_input in self.process_inputs
                if process_input.fits(schema.x_qsl_layer)
            ],
        )
