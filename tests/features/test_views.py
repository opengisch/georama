import pytest
from django.urls import reverse

from georama.features.models import PublishedAsOgcApiFeatures

pytestmark = pytest.mark.django_db


class TestFeaturesViews:
    def test_add_published_as_ogc_api_features_view(
        self, client, integrated_project, admin_user_name, admin_password
    ):
        client.login(username=admin_user_name, password=admin_password)
        project = integrated_project

        # Publish project as OGC API Features
        response = client.get(f"/features/publish_as/oapif/{project.id}", follow=True)
        assert response.status_code == 200
        assert b"TestProject" in response.content

        # Visit collection detail JSON endpoint
        published = PublishedAsOgcApiFeatures.objects.get(title="TestPointLayer")
        url = reverse("features:collection-detail", args=(str(published.identifier),))
        response = client.get(url)
        assert response.status_code == 200
        assert response["Content-Type"] == "application/json"

        collection_detail = response.json()
        assert set(collection_detail) == {
            "crs",
            "description",
            "extent",
            "id",
            "itemType",
            "keywords",
            "links",
            "storageCRS",
            "title",
        }

        # Basic metadata
        expected_subset = {
            "crs": [
                "http://www.opengis.net/def/crs/EPSG/0/4326",
                "https://www.opengis.net/def/crs/OGC/0/CRS84",
                "https://www.opengis.net/def/crs/EPSG/0/2056",
            ],
            "description": None,
            "id": str(published.identifier),
            "itemType": "feature",
            "keywords": [],
            "storageCRS": "http://www.opengis.net/def/crs/EPSG/0/4326",
            "title": "TestPointLayer",
        }
        assert expected_subset.items() <= collection_detail.items()

        # Extent
        extent = collection_detail["extent"]
        assert isinstance(extent, dict)
        spatial = extent["spatial"]
        assert isinstance(spatial, dict)
        assert set(spatial) == {"bbox", "crs"}
        assert extent["spatial"]["crs"] == "http://www.opengis.net/def/crs/OGC/1.3/CRS84"

        # Links
        links = collection_detail["links"]
        assert isinstance(links, list)
        self.normalize_links(links, str(published.identifier))
        assert links == [
            {
                "type": "application/json",
                "rel": "root",
                "title": "The landing page of this server as JSON",
                "href": "http://testserver/features?f=json",
            },
            {
                "type": "text/html",
                "rel": "root",
                "title": "The landing page of this server as HTML",
                "href": "http://testserver/features?f=html",
            },
            {
                "type": "application/json",
                "rel": "self",
                "title": "This document as JSON",
                "href": "http://testserver/features/collections/<PROJECT_ID>?f=json",
            },
            {
                "type": "application/ld+json",
                "rel": "alternate",
                "title": "This document as RDF (JSON-LD)",
                "href": "http://testserver/features/collections/<PROJECT_ID>?f=jsonld",
            },
            {
                "type": "text/html",
                "rel": "alternate",
                "title": "This document as HTML",
                "href": "http://testserver/features/collections/<PROJECT_ID>?f=html",
            },
            {
                "type": "application/schema+json",
                "rel": "http://www.opengis.net/def/rel/ogc/1.0/schema",
                "title": "Schema of collection in JSON",
                "href": "http://testserver/features/collections/<PROJECT_ID>/schema?f=json",
            },
            {
                "type": "text/html",
                "rel": "http://www.opengis.net/def/rel/ogc/1.0/schema",
                "title": "Schema of collection in HTML",
                "href": "http://testserver/features/collections/<PROJECT_ID>/schema?f=html",
            },
            {
                "type": "application/schema+json",
                "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables",
                "title": "Queryables for this collection as JSON",
                "href": "http://testserver/features/collections/<PROJECT_ID>/queryables?f=json",
            },
            {
                "type": "text/html",
                "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables",
                "title": "Queryables for this collection as HTML",
                "href": "http://testserver/features/collections/<PROJECT_ID>/queryables?f=html",
            },
            {
                "type": "application/geo+json",
                "rel": "items",
                "title": "Items as GeoJSON",
                "href": "http://testserver/features/collections/<PROJECT_ID>/items?f=json",
            },
            {
                "type": "application/ld+json",
                "rel": "items",
                "title": "Items as RDF (GeoJSON-LD)",
                "href": "http://testserver/features/collections/<PROJECT_ID>/items?f=jsonld",
            },
            {
                "type": "text/html",
                "rel": "items",
                "title": "Items as HTML",
                "href": "http://testserver/features/collections/<PROJECT_ID>/items?f=html",
            },
        ]

    def normalize_links(self, links, identifier):
        """Normalize links for stable comparisons."""

        for link in links:
            link["href"] = link["href"].replace(identifier, "<PROJECT_ID>")

        return sorted(links, key=lambda x: x["href"])
