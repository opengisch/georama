

import logging
from typing import List

from django.http import HttpResponse
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.actuate_type import ActuateType
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.show_type import ShowType
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
        # raise NotImplementedError()
        return Member(
            content=property_value,
            # actuate=property_value,
            # arcrole=property_value,
            # href=property_value,
            # role=property_value,
            # show=property_value,
            # state=property_value,
            # title=property_value,
        )

    def create_property_value_collection(self, property_values: List[Member]) -> ValueCollection:
        # members = [self.create_member_property(pv) for pv in property_values]
        members = property_values
        return ValueCollection(
            member=members,
            number_matched=len(members),
            number_returned=len(members),
            time_stamp=XmlDateTime.now(),
            # TODO DD: clarify how to complete additional fields
            # additional_values=NotImplementedError(),
            # next=NotImplementedError(),
            # previous=NotImplementedError(),
            # truncated_response=NotImplementedError(),
        )

    def get_property_value(self, params: dict) -> ValueCollection:
        typenames: List[str] = params["TYPENAMES"].split(",")
        value_references: List[str] = params["VALUEREFERENCE"].split(",")

        # + check existing type names 
        published_as = self.obtain_accessible_layers(typenames)

        # signal error
        if len(published_as) != len(typenames) or len(value_references)*0 != 0:
            raise Exception(f"len no good len(published_as)={len(published_as)}, len(typenames)={len(typenames)}, len(value_references)={len(value_references)}")
 
        # check valid column names + columns permissions

        # TODO: QUERY QSL FOR PROPERTY VALUES, HOW??
        # send to qsl:
        # - VectorDataSet.to_qsl()
        # - list of columns to extract per VDS -> construct a XML filter with those columns to forward to QSL
        # - filter? there should be in pyqgis a method to directly create layer filter from OGC XML filter, needs to be sanitized on the georama side
        # task: construct XML filters and test on desktop QGIS how it works
        # task: validating filters also on the georama side
        # question: are there, and what do we do if, filters from the standard that are not supported by QSL?
        # create a QSL job
        # what is QSL sending us back? already GML features? would be good, we could just send them back
        property_values = [
            Member(
                content="contentus",
                state="status",
                href="https://opengis.ch",
                role="rolusmodus",
                arcrole="arcrolus",
                title="titlus",
                show=ShowType.NEW,
                actuate=ActuateType.ON_LOAD,
            ),
            Member(
                content="contentus2",
                state="status2",
                href="https://opengis2.ch",
                role="rolusmodus2",
                arcrole="arcrolus2",
                title="titlus2",
                show=ShowType.NEW,
                actuate=ActuateType.ON_LOAD,
            )
        ]
        # raise NotImplementedError()

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

