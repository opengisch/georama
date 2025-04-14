

import logging
from typing import List

from django.http import HttpResponse
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer
from xsdata.models.datatype import XmlDateTime

from georama.maps.services.wfs_2_0_0 import WfsOperation
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.member_property_type import Member, ValueCollection



class WfsGetPropertyValue(WfsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]
        # ? add "application/gml+xml; version=3.2", "text/xml; subtype=gml/3.2.1", "text/xml; subtype=gml/3.1.1", "text/xml; subtype=gml/2.1.2",

    def create_member_property(self, property_value) -> Member:
        # TODO DD: implement
        raise NotImplementedError()
        return Member(
            content=property_value,
            actuate=property_value,
            arcrole=property_value,
            href=property_value,
            role=property_value,
            show=property_value,
            state=property_value,
            title=property_value,
        )

    def create_property_value_collection(self, property_values: List[Member]) -> ValueCollection:
        members = [self.create_member_property(pv) for pv in property_values]
        return ValueCollection(
            member=members,
            number_matched=len(members),
            number_returned=len(members),
            time_stamp=XmlDateTime.now(),
            # TODO DD: clarify how to complete additional fields
            additional_values=NotImplementedError(),
            next=NotImplementedError(),
            previous=NotImplementedError(),
            truncated_response=NotImplementedError(),
        )

    def get_property_value(self, params: dict) -> ValueCollection:
        typenames: List[str] = params["TYPENAMES"].split(",")
        value_references: List[str] = params["VALUEREFERENCE"].split(",")

        if len(typenames) > 1:
            # TODO DD: how to handle this case? possible to have multiple typenames according to standard, investigate
            raise Exception("WFS GetPropertyValue: more than 1 typenames in query")

        published_as = self.obtain_accessible_layers(typenames)
        if len(published_as) == 0:
            return HttpResponse(404)

        # TODO: QUERY QSL FOR PROPERTY VALUES, HOW??
        property_values = []
        raise NotImplementedError()

        return self.create_property_value_collection(property_values)

    @staticmethod
    def render_xml(value_collection: ValueCollection) -> str:
        serializer = XmlSerializer()
        return serializer.render(
            value_collection,
            ns_map={
                "wfs": "http://www.opengis.net/wfs/2.0",
                "xlink": "http://www.w3.org/1999/xlink",
                "fes": "http://www.opengis.net/fes/2.0",
                "ows": "http://www.opengis.net/ows/1.1",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )

    @staticmethod
    def render_json(value_collection: ValueCollection) -> str:
        serializer = JsonSerializer()
        return serializer.render(value_collection)

    def render(self, requested_format: str, value_collection: ValueCollection) -> str | None:
        if requested_format == "TEXT/XML":
            return self.render_xml(value_collection)
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(value_collection)
        else:
            logging.debug("No matching Format was found.")
            return None

