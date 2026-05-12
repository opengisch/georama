import logging

from django.forms import fields, widgets
from qgis_server_light.interface.exporter import extract


class BaseStrategy:
    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterType,
        **context,
    ) -> dict:
        raise NotImplementedError

    def map_form_field(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterType,
        **context,
    ) -> fields.Field:
        raise NotImplementedError

    def schema(self, parameter: extract.Parameter, **context):
        schema = {
            "title": parameter.name,
            "description": parameter.description,
            "maxOccurs": 1,
            "minOccurs": 0 if parameter.optional else 1,
            "default": parameter.default,
        }
        schema.update(self.map_schema(parameter, parameter.type, **context))
        return schema

    def required(self, parameter: extract.Parameter):
        if not parameter.optional:
            return parameter.default is None
        else:
            return False

    def form_field(self, parameter: extract.Parameter, **context):
        return self.map_form_field(parameter, parameter.type, **context)


class StringStrategy(BaseStrategy):
    def length(self, parameter_type: extract.ProcessingParameterTypeString):
        k = {}
        if hasattr(parameter_type, "length") and isinstance(parameter_type.length, int):
            k["length"] = parameter_type.length
        return k

    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeString,
        **context,
    ) -> dict:
        type_schema = {"type": "string"}
        type_schema.update(self.length(parameter_type))
        return type_schema

    def map_form_field(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeString,
        **context,
    ) -> fields.CharField:
        return fields.CharField(
            initial=parameter.default,
            required=self.required(parameter),
            max_length=self.length(parameter_type).get("length"),
        )


class MultiStringStrategy(BaseStrategy):
    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeBoolean,
        **context,
    ) -> dict:
        type_schema = {"type": "string"}
        if parameter_type.allow_multiple:
            return {"type": "array", "items": type_schema}
        return type_schema


class BooleanStrategy(BaseStrategy):
    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeBoolean,
        **context,
    ) -> dict:
        return {"type": "boolean"}

    def map_form_field(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeBoolean,
        **context,
    ) -> fields.BooleanField:
        return fields.BooleanField(
            initial=parameter.default,
            required=self.required(parameter),
            widget=widgets.CheckboxInput(),
        )


class NumberStrategy(BaseStrategy):
    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeFloat
        | extract.ProcessingParameterTypeInt,
        **context,
    ) -> dict:
        type_schema = {"type": "number"}
        if isinstance(parameter_type.minimum, (int, float)):
            type_schema["minimum"] = parameter_type.minimum
        if isinstance(parameter_type.maximum, (int, float)):
            type_schema["maximum"] = parameter_type.maximum
        return type_schema

    def map_form_field(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeFloat
        | extract.ProcessingParameterTypeInt,
        **context,
    ) -> fields.FloatField | fields.IntegerField:
        if isinstance(parameter_type, extract.ProcessingParameterTypeFloat):
            return fields.FloatField(
                initial=parameter.default,
                required=self.required(parameter),
                min_value=parameter_type.minimum,
                max_value=parameter_type.maximum,
            )
        else:
            return fields.IntegerField(
                initial=parameter.default,
                required=self.required(parameter),
                min_value=parameter_type.minimum,
                max_value=parameter_type.maximum,
            )


class ExtentStrategy(BaseStrategy):
    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeExtent,
        **context,
    ) -> dict:
        return {
            "type": "array",
            "prefixItems": [
                {"type": "number", "title": "minX"},
                {"type": "number", "title": "minY"},
                {"type": "number", "title": "maxX"},
                {"type": "number", "title": "maxY"},
            ],
            "items": False,
        }

    def map_form_field(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeExtent,
        **context,
    ) -> fields.JSONField:
        return fields.JSONField(
            required=self.required(parameter),
        )


class EnumStrategy(BaseStrategy):
    def map_schema(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeEnum,
        **context,
    ) -> dict:

        type_schema = {"type": "string", "enum": parameter_type.options}
        if parameter_type.allow_multiple:
            return {"type": "array", "items": type_schema}
        return type_schema

    def map_form_field(
        self,
        parameter: extract.Parameter,
        parameter_type: extract.ProcessingParameterTypeEnum,
        **context,
    ) -> fields.ChoiceField:
        return fields.ChoiceField(
            initial=parameter.default,
            required=self.required(parameter),
            choices={k: k for k in parameter_type.options},
        )


class JsonSchemaMapper:
    def __init__(self):
        self._mappings = {
            extract.ProcessingParameterTypeString: StringStrategy,
            extract.ProcessingParameterTypeBoolean: BooleanStrategy,
            extract.ProcessingParameterTypeFloat: NumberStrategy,
            extract.ProcessingParameterTypeInt: NumberStrategy,
            extract.ProcessingParameterTypeExtent: ExtentStrategy,
            extract.ProcessingParameterTypeCrs: StringStrategy,
            extract.ProcessingParameterTypeBand: MultiStringStrategy,
            extract.ProcessingParameterTypeField: MultiStringStrategy,
            extract.ProcessingParameterTypeLayout: StringStrategy,
            extract.ProcessingParameterTypeMapTheme: StringStrategy,
            extract.ProcessingParameterTypeExpression: StringStrategy,
            extract.ProcessingParameterTypeEnum: EnumStrategy,
            extract.ProcessingParameterTypeVectorLayer: StringStrategy,
            extract.ProcessingParameterTypeRasterLayer: StringStrategy,
            extract.ProcessingParameterTypeFile: StringStrategy,
            extract.ProcessingParameterTypeMapLayer: StringStrategy,
            extract.ProcessingParameterTypeAnyLayer: StringStrategy,
        }

    def register(self, parameter: extract.Parameter, mapping_strategy: BaseStrategy):
        if self._mappings.get(type(parameter.type)):
            logging.debug(f"mapping exists already {type(parameter.type)}")
            return
        self._mappings[type(parameter.type)] = mapping_strategy

    def map(self, parameter: extract.Parameter, **context):
        mapping_strategy = self._mappings.get(type(parameter.type))

        if mapping_strategy is None:
            raise ValueError(f"No mapping strategy for {type(parameter.type)}")

        return mapping_strategy().schema(parameter, **context)


class HtmlInputMapper:
    def __init__(self):
        self._mappings = {
            extract.ProcessingParameterTypeString: StringStrategy,
            extract.ProcessingParameterTypeBoolean: BooleanStrategy,
            extract.ProcessingParameterTypeFloat: NumberStrategy,
            extract.ProcessingParameterTypeInt: NumberStrategy,
            extract.ProcessingParameterTypeExtent: ExtentStrategy,
            extract.ProcessingParameterTypeCrs: StringStrategy,
            extract.ProcessingParameterTypeBand: MultiStringStrategy,
            extract.ProcessingParameterTypeField: MultiStringStrategy,
            extract.ProcessingParameterTypeLayout: StringStrategy,
            extract.ProcessingParameterTypeMapTheme: StringStrategy,
            extract.ProcessingParameterTypeExpression: StringStrategy,
            extract.ProcessingParameterTypeEnum: EnumStrategy,
            extract.ProcessingParameterTypeVectorLayer: StringStrategy,
            extract.ProcessingParameterTypeRasterLayer: StringStrategy,
            extract.ProcessingParameterTypeFile: StringStrategy,
            extract.ProcessingParameterTypeMapLayer: StringStrategy,
            extract.ProcessingParameterTypeAnyLayer: StringStrategy,
        }

    def register(self, parameter: extract.Parameter, mapping_strategy: BaseStrategy):
        if self._mappings.get(type(parameter.type)):
            logging.debug(f"mapping exists already {type(parameter.type)}")
            return
        self._mappings[type(parameter.type)] = mapping_strategy

    def map(self, parameter: extract.Parameter, **context):
        mapping_strategy = self._mappings.get(type(parameter.type))

        if mapping_strategy is None:
            raise ValueError(f"No mapping strategy for {type(parameter.type)}")

        return mapping_strategy().form_field(parameter, **context)
