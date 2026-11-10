import logging

from crispy_bootstrap5.bootstrap5 import Switch
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.forms import fields, forms, widgets
from qgis_server_light.interface.job.process.description import (
    InputDescription,
    OutputDescription,
    Schema,
)


class BaseStrategy:
    def map_form_field(
        self,
        input_description: InputDescription,
        schema: Schema,
        **context,
    ) -> fields.Field:
        raise NotImplementedError

    def required(self, input_description: InputDescription):
        if input_description.min_occurs > 0:
            return input_description.schema.default is None
        else:
            return False

    def form_field(self, input_description: InputDescription, **context):
        return self.map_form_field(input_description, input_description.schema, **context)


class StringStrategy(BaseStrategy):
    def map_form_field(
        self,
        input_description: InputDescription,
        schema: Schema,
        **context,
    ) -> fields.CharField:
        return fields.CharField(
            initial=schema.default,
            required=self.required(input_description),
        )


class BooleanStrategy(BaseStrategy):
    def map_form_field(
        self,
        input_description: InputDescription,
        schema: Schema,
        **context,
    ) -> fields.BooleanField:
        return fields.BooleanField(
            initial=schema.default,
            required=self.required(input_description),
            widget=widgets.CheckboxInput(),
        )


class NumberStrategy(BaseStrategy):
    def map_form_field(
        self,
        input_description: InputDescription,
        schema: Schema,
        **context,
    ) -> fields.FloatField:
        return fields.FloatField(
            initial=schema.default,
            required=self.required(input_description),
            min_value=schema.minimum,
            max_value=schema.maximum,
        )


class IntegerStrategy(BaseStrategy):
    def map_form_field(
        self,
        input_description: InputDescription,
        schema: Schema,
        **context,
    ) -> fields.IntegerField:
        return fields.IntegerField(
            initial=schema.default,
            required=self.required(input_description),
            min_value=schema.minimum,
            max_value=schema.maximum,
        )


class EnumStrategy(BaseStrategy):
    coerce_by_type = {
        "string": str,
        "integer": int,
    }

    def map_form_field(
        self,
        input_description: InputDescription,
        schema: Schema,
        **context,
    ) -> fields.TypedChoiceField:
        return fields.TypedChoiceField(
            initial=schema.default,
            required=self.required(input_description),
            choices={option.const: option.title for option in schema.one_of},
            coerce=self.coerce_by_type[schema.type],
        )


class HtmlInputMapper:
    def __init__(self):
        self._mappings = {
            "string": StringStrategy,
            "boolean": BooleanStrategy,
            "number": NumberStrategy,
            "integer": IntegerStrategy,
        }

    def register(self, schema_type: str, mapping_strategy: type[BaseStrategy]):
        if self._mappings.get(schema_type):
            logging.debug(f"mapping exists already {schema_type}")
            return
        self._mappings[schema_type] = mapping_strategy

    def map(self, input_description: InputDescription, **context):
        if input_description.schema.one_of is not None:
            mapping_strategy = EnumStrategy
        else:
            mapping_strategy = self._mappings.get(input_description.schema.type)

        if mapping_strategy is None:
            raise ValueError(f"No mapping strategy for {input_description.schema.type}")

        return mapping_strategy().form_field(input_description, **context)

    def form_class(self, input_descriptions: list[InputDescription]) -> type[forms.Form]:
        attrs = {}
        switch_fields = []
        for input_description in input_descriptions:
            field = self.map(input_description)
            attrs[input_description.id] = field
            if isinstance(field, fields.BooleanField):
                switch_fields.append(Switch(input_description.id))
        attrs["helper"] = FormHelper()
        attrs["helper"].layout = Layout(*tuple(switch_fields))

        return type("DynamicParamsForm", (forms.Form,), attrs)


class HtmlOutputFormatMapper:
    """Offers the formats of the file outputs of a process as choice, the formats are the
    `oneOf` entries with `contentMediaType` of the output schema. Without a choice the
    worker writes the first offered format.
    """

    def map(self, output_description: OutputDescription) -> fields.ChoiceField:
        media_types = [schema.content_media_type for schema in output_description.schema.one_of]
        return fields.ChoiceField(
            label=output_description.title,
            initial=media_types[0],
            required=False,
            choices={media_type: media_type for media_type in media_types},
        )

    def form_class(self, output_descriptions: list[OutputDescription]) -> type[forms.Form]:
        attrs = {
            output_description.id: self.map(output_description)
            for output_description in output_descriptions
            if output_description.schema.one_of is not None
        }
        attrs["helper"] = FormHelper()
        attrs["helper"].form_tag = False
        return type("DynamicOutputFormatsForm", (forms.Form,), attrs)
