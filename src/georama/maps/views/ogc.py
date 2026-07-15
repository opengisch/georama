import logging

from asgiref.sync import sync_to_async
from django.http import HttpRequest, HttpResponse
from django.views import View
from qgis_server_light.interface.dispatcher.common import Status
from qgis_server_light.interface.job.common.output import JobResult
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import DictDecoder, XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.core.common.request import GeoramaHttpRequest
from georama.maps.apps import MapsConfig, qsl_redis_queue
from georama.maps.exception.job import JobExecutionError, UnexpectedBehaviourError
from georama.maps.interfaces.georama.requests import GetMapRequestParams
from georama.maps.interfaces.ogc.wfs_2_0_0 import GetFeature as GetFeature200
from georama.maps.maps_config import Config
from georama.maps.models import WmsLayer
from georama.maps.services.wfs_2_0_0.describe_feature_type import WfsDescribeFeatureType
from georama.maps.services.wfs_2_0_0.get_capabilities import WfsGetCapabilities
from georama.maps.services.wfs_2_0_0.get_feature import WfsGetFeature
from georama.maps.services.wfs_2_0_0.get_metadata import WfsGetMetadata
from georama.maps.services.wms_1_3_0.get_capabilities import WmsGetCapabilities
from georama.maps.services.wms_1_3_0.get_map import WmsGetMap

log = logging.getLogger(__name__)


class OgcServer(View):
    model = WmsLayer
    appname = MapsConfig.get_simple_appname()

    def wms_130_capabilities(self, request: GeoramaHttpRequest, params: dict) -> HttpResponse:
        """
        Handling the wms 1.3.0 capabilities.

        Args:
            request: The django request object.
            params: the parameters which were send.

        Returns:
            The response object.
        """
        requested_format = params.get("FORMAT", "TEXT/XML")
        operation = WmsGetCapabilities(
            self.appname,
            f"{request.build_absolute_uri('.')}?",
            request.user,
            self.model,
            request.georama_organisation,
        )
        if requested_format not in operation.allowed_formats:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed."
                    f"Allowed is {operation.allowed_formats}"
                ),
                status=400,
                content_type="text/xml",
            )
        if requested_format == "TEXT/XML":
            return HttpResponse(
                operation.render_xml(operation.get_capabilities()),
                content_type="text/xml",
            )
        elif requested_format == "APPLICATION/JSON":
            return HttpResponse(
                operation.render_json(operation.get_capabilities()),
                content_type="application/json",
            )

    def wfs_200_capabilities(self, request: GeoramaHttpRequest, params: dict) -> HttpResponse:
        requested_format = params.get("FORMAT", "TEXT/XML")
        operation = WfsGetCapabilities(
            self.appname,
            f"{request.build_absolute_uri('.')}?",
            request.user,
            self.model,
            request.georama_organisation,
        )

        if requested_format not in operation.allowed_formats:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed."
                    f"Allowed is {operation.allowed_formats}"
                ),
                status=400,
                content_type="text/xml",
            )
        if requested_format == "TEXT/XML":
            return HttpResponse(
                operation.render_xml(operation.get_capabilities()),
                content_type="text/xml",
            )
        elif requested_format == "APPLICATION/JSON":
            return HttpResponse(
                operation.render_json(operation.get_capabilities()),
                content_type="application/json",
            )

    def wfs_get_metadata(self, request: HttpRequest, params: dict) -> HttpResponse:
        requested_layer = params.get("LAYER")
        language = "en-US"
        requested_format = params.get("FORMAT", "TEXT/XML")
        operation = WfsGetMetadata(
            self.appname, f"{request.build_absolute_uri('.')}?", request.user, self.model
        )
        if requested_layer:
            if requested_format not in operation.allowed_formats:
                return HttpResponse(
                    operation.render_operation_parsing_failed(
                        f"Format {requested_format} is not allowed."
                        f"Allowed is {operation.allowed_formats}"
                    ),
                    status=400,
                    content_type="text/xml",
                )
            if requested_format == "TEXT/XML":
                return HttpResponse(
                    operation.render_xml(operation.get_metadata(requested_layer, language)),
                    content_type="text/xml",
                )
            elif requested_format == "APPLICATION/JSON":
                return HttpResponse(
                    operation.render_json(operation.get_metadata(requested_layer, language)),
                    content_type="application/json",
                )
        else:
            return HttpResponse(
                operation.render_operation_parsing_failed("Query paramater 'layer' has to be set!"),
                status=400,
                content_type="text/xml",
            )

    def wfs_200_describefeaturetype(
        self, request: GeoramaHttpRequest, params: dict
    ) -> HttpResponse:
        # refering spec document `TYPENAME` is a comma separated
        # list of *layers* which should be described
        # it is an optional query parameter
        requested_layer = params.get("TYPENAME")
        if requested_layer:
            requested_layer = requested_layer.split(",")
        requested_format = params.get("OUTPUTFORMAT", "APPLICATION/GML+XML; VERSION=3.2").upper()
        operation = WfsDescribeFeatureType(
            self.appname,
            f"{request.build_absolute_uri('.')}?",
            request.user,
            self.model,
            request.georama_organisation,
        )
        content, content_type, success = operation.render(
            requested_format, operation.describe_feature_type(requested_layer)
        )
        if not success:
            return HttpResponse(
                content,
                status=400,
                content_type=content_type,
            )
        else:
            return HttpResponse(
                content,
                content_type=content_type,
            )

    async def wfs_200_getfeature(self, request: GeoramaHttpRequest, params: dict) -> HttpResponse:
        operation = WfsGetFeature(
            self.appname,
            f"{request.build_absolute_uri('.')}?",
            request.user,
            self.model,
            request.georama_organisation,
        )
        get_feature_parameter = operation.query_parameters_to_get_feature_request(params)

        job = await sync_to_async(operation.getfeature_to_qslgetfeaturejob, thread_sensitive=True)(
            get_feature_parameter
        )
        result, status = await qsl_redis_queue.post(job, Config().job_timeout)

        self.handle_job_result(result, status)

        content, content_type, success = operation.render(
            get_feature_parameter.output_format,
            operation.get_feature(
                # we use only one query here, since this is implemented
                # for URL GET query params
                # TODO: This has to be improved for XML body via POST
                get_feature_parameter,
                result,
                job,
            ),
            operation.unwrap_type_names(get_feature_parameter),
        )
        if not success:
            return HttpResponse(
                content,
                status=400,
                content_type=content_type,
            )
        else:
            return HttpResponse(
                content,
                content_type=content_type,
            )

    def sanitize_query_parameters(self, parameters: dict) -> dict:
        params = {}
        for key in parameters:
            if (
                key.upper() == "LAYERS"
                or key.upper() == "STYLES"
                or key.upper() == "TYPENAME"
                or key.upper() == "TYPENAMES"
                or key.upper() == "ALIASES"
                or key.upper() == "FILTER"
                or key.upper() == "LAYER"
            ):
                params[str(key).upper()] = str(parameters[key])
            else:
                params[str(key).upper()] = str(parameters[key]).upper()
        return params

    def handle_job_result(self, result: JobResult, status: str):
        """Handles general behavior on job result and status.

        Args:
            result: The result received from redis queue.
            status: The status of the job execution.

        Raises:
            JobExecutionError: If the job has status failed.
            UnexpectedBehaviourError: In any other case then Status.FAILURE,
                Status.SUCCESS.
        """
        if status == Status.FAILURE.value:
            raise JobExecutionError(job_id=result.id)
        elif status == Status.SUCCESS.value:
            pass
        else:
            raise UnexpectedBehaviourError(job_id=result.id)

    async def get(self, request: GeoramaHttpRequest, *args, **kwargs):
        params = self.sanitize_query_parameters(request.GET.dict())

        if "REQUEST" not in params:
            return HttpResponse("REQUEST parameter is mandatory", 400)

        if "SERVICE" not in params:
            if params["REQUEST"].upper() == "GETMETADATA":
                return await sync_to_async(self.wfs_get_metadata, thread_sensitive=True)(
                    request, params
                )
            else:
                return HttpResponse(
                    "Only request allowed without service param is GetMetadata", 400
                )

        if params["SERVICE"].upper() == "WMS":
            if params["REQUEST"] == "GETCAPABILITIES":
                if params.get("VERSION", "1.3.0") == "1.3.0":
                    return await sync_to_async(self.wms_130_capabilities, thread_sensitive=True)(
                        request, params
                    )
                else:
                    return HttpResponse("Only VERSION 1.3.0 is available", 400)
            elif params["REQUEST"] == "GETMAP":
                # This is especially usefull for input from foreign
                # systems which might send whatever query
                # params we don't have knowledge of
                parser_config = ParserConfig(
                    fail_on_unknown_properties=False, fail_on_unknown_attributes=False
                )
                service_params = DictDecoder(parser_config).decode(params, GetMapRequestParams)
                operation = WmsGetMap(
                    self.appname,
                    f"{request.build_absolute_uri('.')}?",
                    request.user,
                    self.model,
                    request.georama_organisation,
                )
                try:
                    job = await sync_to_async(operation.prepare_job_content, thread_sensitive=True)(
                        service_params
                    )
                    logging.debug(job)
                except ValueError as e:
                    return HttpResponse(e, status=400, content_type="text/plain")
                except PermissionError as e:
                    return HttpResponse(e, status=403, content_type="text/plain")

            elif params["REQUEST"] == "GETFEATUREINFO":
                raise NotImplementedError("Currently not supported")
            else:
                return HttpResponse("Only WMS Service is available", 500)
            config = Config()
            result, status = await qsl_redis_queue.post(job, config.job_timeout)

            self.handle_job_result(result, status)

            return HttpResponse(result.data, result.content_type)
        elif params["SERVICE"].upper() == "WFS":
            if params.get("VERSION", "2.0.0") == "2.0.0":
                pass
            else:
                return HttpResponse("Only VERSION 2.0.0 is available", 400)
            if params["REQUEST"] == "GETCAPABILITIES":
                return await sync_to_async(self.wfs_200_capabilities, thread_sensitive=True)(
                    request, params
                )
            elif params["REQUEST"] == "DESCRIBEFEATURETYPE":
                return await sync_to_async(self.wfs_200_describefeaturetype, thread_sensitive=True)(
                    request, params
                )
            elif params["REQUEST"] == "GETFEATURE":
                try:
                    return await self.wfs_200_getfeature(request, params)
                except AttributeError as e:
                    return HttpResponse(e, status=400, content_type="text/xml")
                except PermissionError as e:
                    return HttpResponse(e, status=400, content_type="text/xml")
                # except Exception as e:
                #     logging.error(e)
                #     # TODO: Provide the error info also in the response if we are in DEBUG?
                #     return HttpResponse(
                #         "An unexpected error happened while processing the request",
                #         400
                #     )
            else:
                return HttpResponse("Not supported operation", 403)
        else:
            return HttpResponse("Only WMS|WFS Service is available", 400)

    async def post(self, request: GeoramaHttpRequest, *args, **kwargs):
        try:
            operation = WfsGetFeature(
                self.appname,
                f"{request.build_absolute_uri('.')}?",
                request.user,
                self.model,
                request.georama_organisation,
            )
            try:
                get_feature_parameter = XmlParser().from_bytes(request.body, GetFeature200)
                job = await sync_to_async(
                    operation.getfeature_to_qslgetfeaturejob, thread_sensitive=True
                )(get_feature_parameter)
            except ParserError as e:
                logging.error(e)
                return HttpResponse(
                    WfsGetFeature.render_exception("Could not parse payload"),
                    status=400,
                    content_type="text/xml",
                )
            result, status = await qsl_redis_queue.post(job, Config().job_timeout)

            self.handle_job_result(result, status)

            content, content_type, success = operation.render(
                get_feature_parameter.output_format.upper(),
                operation.get_feature(
                    # we use only one query here, since this is
                    # implemented for URL GET query params
                    # TODO: This has to be improved for XML body via POST
                    get_feature_parameter,
                    result,
                    job,
                ),
                operation.unwrap_type_names(get_feature_parameter),
            )
            if not success:
                return HttpResponse(
                    content,
                    status=400,
                    content_type=content_type,
                )
            else:
                return HttpResponse(
                    content,
                    content_type=content_type,
                )
        except AttributeError as e:
            logging.error(e)
            return HttpResponse(e, status=400, content_type="text/xml")
