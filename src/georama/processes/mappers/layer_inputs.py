from dataclasses import replace

from qgis_server_light.interface.job.process.description import (
    InputDescription,
    ProcessDescription,
    ProcessDescriptions,
    Schema,
)

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
