"""POC: forwards the metadata of published layers to GeoNetwork as ISO 19139 record.

Only the content of the metadata table (`BaseMetadata`) is forwarded. The record
identifier is the primary key of the metadata, so a repeated push overwrites the
record instead of creating a new one.

GeoNetwork has to run with `geonetwork.security.type=openidconnectbearer`. The access
token is fetched from keycloak with the client credentials of a service account.
"""

import logging
import secrets
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import UTC, datetime

import httpx
from django.conf import settings
from xsdata.models.datatype import XmlDate

from georama.core.common.models import BaseMetadata
from georama.maps.exception.geonetwork import GeoNetworkError
from georama.maps.interfaces.iso.tc211.gmd.dataclasses import (
    CharacterString,
    CharacterStringPropertyType,
    CiCitation,
    CiCitationPropertyType,
    CiOnlineResource,
    CiOnlineResourcePropertyType,
    Date,
    DatePropertyType,
    MdConstraintsPropertyType,
    MdDataIdentification,
    MdDigitalTransferOptions,
    MdDigitalTransferOptionsPropertyType,
    MdDistribution,
    MdDistributionPropertyType,
    MdDistributor,
    MdDistributorPropertyType,
    MdIdentificationPropertyType,
    MdLegalConstraints,
    MdMetadata,
    MdRestrictionCode,
    MdRestrictionCodePropertyType,
    MdScopeCode,
    MdScopeCodePropertyType,
    MdStandardOrderProcess,
    MdStandardOrderProcessPropertyType,
    Url,
    UrlPropertyType,
)
from georama.maps.services.wfs_2_0_0.get_metadata import WfsGetMetadata

CODE_LIST_URL = "http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml"

# GeoNetwork compares the cookie with the header (double submit), the value itself is
# not checked against a session.
XSRF_COOKIE_NAME = "XSRF-TOKEN"
XSRF_HEADER_NAME = "X-XSRF-TOKEN"

# reserved GeoNetwork group of all users, its view privilege makes a record public
ALL_GROUP_ID = 1


# protocol values of the iso19139 picklist of GeoNetwork
PROTOCOL_WMS = "OGC:WMS"
PROTOCOL_WFS = "OGC:WFS"
PROTOCOL_OAPIF = "OGC API - Features"
PROTOCOL_LINK = "WWW:LINK"


@dataclass
class RecordState:
    uuid: str
    public: bool


@dataclass
class OnlineResource:
    """A service endpoint where the data of the record can be used.

    Attributes:
        url: Base url of the service (WMS / WFS without parameters, OAPIF landing page).
        protocol: One of the `PROTOCOL_*` values.
        name: Name of the layer / feature type / collection within the service.
        description: Human readable description of the link.
    """

    url: str
    protocol: str
    name: str
    description: str


@dataclass
class RecordContent:
    """What a published item forwards to GeoNetwork as one record.

    Attributes:
        metadata: The metadata of the item, its primary key is the record uuid.
        online_resources: The service endpoints of the item.
    """

    metadata: BaseMetadata
    online_resources: list[OnlineResource]


@dataclass
class SearchHit:
    uuid: str
    title: str


def character_string(value: str) -> CharacterStringPropertyType:
    return CharacterStringPropertyType(character_string=CharacterString(value=value))


def other_restrictions() -> MdRestrictionCodePropertyType:
    return MdRestrictionCodePropertyType(
        md_restriction_code=MdRestrictionCode(
            value="otherRestrictions",
            code_list=f"{CODE_LIST_URL}#MD_RestrictionCode",
            code_list_value="otherRestrictions",
        )
    )


def create_identification_info(metadata: BaseMetadata) -> MdIdentificationPropertyType:
    return MdIdentificationPropertyType(
        md_data_identification=MdDataIdentification(
            citation=CiCitationPropertyType(
                ci_citation=CiCitation(title=character_string(metadata.title))
            ),
            abstract=character_string(metadata.description),
            resource_constraints=[
                MdConstraintsPropertyType(
                    md_legal_constraints=MdLegalConstraints(
                        use_constraints=[other_restrictions()],
                        other_constraints=[character_string(metadata.license.strip())],
                    )
                ),
                MdConstraintsPropertyType(
                    md_legal_constraints=MdLegalConstraints(
                        access_constraints=[other_restrictions()],
                        other_constraints=[character_string(metadata.access_constraints)],
                    )
                ),
            ],
        )
    )


def create_online_resource(online_resource: OnlineResource) -> CiOnlineResourcePropertyType:
    return CiOnlineResourcePropertyType(
        ci_online_resource=CiOnlineResource(
            linkage=UrlPropertyType(url=Url(value=online_resource.url)),
            protocol=character_string(online_resource.protocol),
            name=character_string(online_resource.name),
            description=character_string(online_resource.description),
        )
    )


def create_distribution_info(
    metadata: BaseMetadata, online_resources: list[OnlineResource]
) -> MdDistributionPropertyType:
    return MdDistributionPropertyType(
        md_distribution=MdDistribution(
            transfer_options=[
                MdDigitalTransferOptionsPropertyType(
                    md_digital_transfer_options=MdDigitalTransferOptions(
                        on_line=[create_online_resource(o) for o in online_resources]
                    )
                )
            ],
            distributor=[
                MdDistributorPropertyType(
                    md_distributor=MdDistributor(
                        distribution_order_process=[
                            MdStandardOrderProcessPropertyType(
                                md_standard_order_process=MdStandardOrderProcess(
                                    fees=character_string(metadata.fees)
                                )
                            )
                        ]
                    )
                )
            ],
        )
    )


def create_record(metadata: BaseMetadata, online_resources: list[OnlineResource]) -> MdMetadata:
    """Builds the ISO 19139 dataset record from the metadata table and the services the
    layer is published with.

    Mandatory ISO elements which are not part of the metadata table (contact, citation
    date, language) are left out. GeoNetwork accepts the record as long as it is not
    pushed with `rejectIfInvalid`.

    Args:
        metadata: The metadata of a published layer.
        online_resources: The service endpoints of the layer.

    Returns:
        The record, its file identifier is the primary key of the metadata.
    """
    return MdMetadata(
        file_identifier=character_string(str(metadata.id)),
        hierarchy_level=[
            MdScopeCodePropertyType(
                md_scope_code=MdScopeCode(
                    value="dataset",
                    code_list=f"{CODE_LIST_URL}#MD_ScopeCode",
                    code_list_value="dataset",
                )
            )
        ],
        date_stamp=DatePropertyType(date=Date(value=XmlDate.from_date(datetime.now(UTC).date()))),
        identification_info=[create_identification_info(metadata)],
        distribution_info=create_distribution_info(metadata, online_resources),
    )


async def fetch_access_token(client: httpx.AsyncClient) -> str:
    response = await client.post(
        settings.GEONETWORK_TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": settings.GEONETWORK_CLIENT_ID,
            "client_secret": settings.GEONETWORK_CLIENT_SECRET,
            # keycloak answers the userinfo request of GeoNetwork only for openid tokens
            "scope": "openid",
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


@asynccontextmanager
async def geonetwork_api(uuid: str) -> AsyncIterator[httpx.AsyncClient]:
    """Opens an authenticated client on the api of GeoNetwork.

    Failing requests inside the context are translated into `GeoNetworkError`.

    Args:
        uuid: The uuid of the record which is handled, used for the error message.

    Yields:
        The client, paths are relative to `{GEONETWORK_URL}/api/`.

    Raises:
        GeoNetworkError: In case GeoNetwork or keycloak could not be reached or
            answered with an error status.
    """
    xsrf_token = secrets.token_urlsafe(16)
    async with httpx.AsyncClient(
        base_url=f"{settings.GEONETWORK_URL}/api/",
        cookies={XSRF_COOKIE_NAME: xsrf_token},
        headers={XSRF_HEADER_NAME: xsrf_token, "Accept": "application/json"},
    ) as client:
        try:
            access_token = await fetch_access_token(client)
            client.headers["Authorization"] = f"Bearer {access_token}"
            yield client
        except httpx.HTTPStatusError as e:
            raise GeoNetworkError(
                f"{e.response.status_code} from {e.request.url}: {e.response.text}", uuid
            ) from e
        except httpx.RequestError as e:
            raise GeoNetworkError(f"{e.request.url} not reachable: {e}", uuid) from e


async def push_record(
    metadata: BaseMetadata, publish_to_all: bool, online_resources: list[OnlineResource]
) -> str:
    """Creates or overwrites the record of the metadata in GeoNetwork.

    Args:
        metadata: The metadata of a published layer.
        online_resources: The service endpoints of the layer.
        publish_to_all: Whether the record is visible for everybody in GeoNetwork.

    Returns:
        The uuid of the record.

    Raises:
        GeoNetworkError: In case GeoNetwork did not accept the record.
    """
    uuid = str(metadata.id)
    async with geonetwork_api(uuid) as client:
        logging.debug(f"Pushing record {uuid} to {settings.GEONETWORK_URL}")
        response = await client.put(
            "records",
            params={
                "uuidProcessing": "OVERWRITE",
                "publishToAll": str(publish_to_all).lower(),
                "group": settings.GEONETWORK_GROUP,
            },
            content=WfsGetMetadata.render_xml(create_record(metadata, online_resources)),
            headers={"Content-Type": "application/xml"},
        )
        response.raise_for_status()
    report = response.json()
    if report.get("errors") or report.get("metadataErrors"):
        raise GeoNetworkError(f"GeoNetwork rejected the record: {report}", uuid)
    return uuid


async def fetch_record_state(uuid: str) -> RecordState | None:
    """Reads whether the record exists in GeoNetwork and whether it is public.

    Args:
        uuid: The uuid of the record.

    Returns:
        The state of the record, `None` if GeoNetwork does not know the record.
    """
    async with geonetwork_api(uuid) as client:
        response = await client.get(f"records/{uuid}/sharing")
        if response.status_code == httpx.codes.NOT_FOUND:
            return None
        response.raise_for_status()
    public = any(
        privilege["group"] == ALL_GROUP_ID and privilege["operations"].get("view", False)
        for privilege in response.json()["privileges"]
    )
    return RecordState(uuid=uuid, public=public)


async def publish_record(uuid: str):
    """Grants the privileges of the group `all`, everybody can find the record."""
    async with geonetwork_api(uuid) as client:
        response = await client.put(f"records/{uuid}/publish")
        response.raise_for_status()


async def unpublish_record(uuid: str):
    """Removes the privileges of the group `all`, the record stays in GeoNetwork."""
    async with geonetwork_api(uuid) as client:
        response = await client.put(f"records/{uuid}/unpublish")
        response.raise_for_status()


async def sync_record_visibility(uuid: str, public: bool):
    """Mirrors the `public` switch of a layer to its record, if GeoNetwork has one.

    Args:
        uuid: The uuid of the record.
        public: Whether the layer is public.
    """
    record = await fetch_record_state(uuid)
    if record is None or record.public == public:
        return
    if public:
        await publish_record(uuid)
    else:
        await unpublish_record(uuid)


async def delete_record(uuid: str):
    """Deletes the record, a record GeoNetwork does not know counts as deleted."""
    async with geonetwork_api(uuid) as client:
        response = await client.delete(f"records/{uuid}")
        if response.status_code == httpx.codes.NOT_FOUND:
            return
        response.raise_for_status()


def create_search_query(term: str, uuids: list[str], size: int) -> dict:
    """Builds the Elasticsearch query for the GeoNetwork search api.

    The term is matched as prefix (type ahead) against the fields the GeoNetwork UI uses
    for its full text search. The records are restricted to the given uuids before the
    search, so paging and counts stay correct.

    Args:
        term: The search term as typed by the user.
        uuids: The uuids of the records the requesting user may find.
        size: The maximum number of hits.

    Returns:
        The query as dict.
    """
    return {
        "size": size,
        "_source": ["uuid", "resourceTitleObject"],
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": term,
                            "type": "bool_prefix",
                            "fields": ["resourceTitleObject.*^2", "any.*"],
                            "lenient": True,
                        }
                    }
                ],
                "filter": [{"terms": {"uuid": uuids}}],
            }
        },
    }


async def search_records(term: str, uuids: list[str], size: int) -> list[SearchHit]:
    """Searches the records in GeoNetwork, ordered by relevance.

    Georama searches with its own account, the permissions are applied by restricting
    the uuids.

    Args:
        term: The search term as typed by the user.
        uuids: The uuids of the records the requesting user may find.
        size: The maximum number of hits.

    Returns:
        The hits.
    """
    async with geonetwork_api("search") as client:
        response = await client.post(
            "search/records/_search", json=create_search_query(term, uuids, size)
        )
        response.raise_for_status()
    return [
        SearchHit(
            uuid=hit["_source"]["uuid"],
            title=hit["_source"].get("resourceTitleObject", {}).get("default", ""),
        )
        for hit in response.json()["hits"]["hits"]
    ]
