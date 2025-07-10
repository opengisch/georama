import pytest
from playwright.sync_api import expect

from tests.conftest import ADMIN_PASS, ADMIN_USER

pytestmark = pytest.mark.django_db()


def test_publish_project(page):
    # Visit admin panel and log in
    page.goto("/")
    page.get_by_role("link", name="Admin Page").click()
    page.get_by_role("textbox", name="Username").fill(ADMIN_USER)
    page.get_by_role("textbox", name="Password").fill(ADMIN_PASS)
    page.get_by_role("button", name="Log in").click()

    # Integrate project
    page.get_by_role("link", name="Projects", exact=True).click()
    page.get_by_role("link", name="Qgis Projects").click()
    page.get_by_role("link", name="integrate").click()

    # Publish as OGC API Features
    page.get_by_role("link", name="Published as ogc api featuress").click()
    page.get_by_role("link", name="Add published as ogc api").click()
    page.get_by_role("link", name="publish", exact=True).click()
    page.locator("#id_form-0-public").click()
    page.get_by_role("button", name="Save").click()

    # Publish WMS Layer
    page.get_by_role("link", name="WMS Layers").first.click()
    page.get_by_role("link", name="Add WMS Layer").click()
    page.get_by_role("link", name="publish", exact=True).click()
    page.locator("#id_form-0-public").click()
    page.get_by_role("button", name="Save").click()

    link = page.get_by_role("link", name="WMS Capabilities")
    url = link.get_attribute("href")
    response = page.request.get(url)
    assert response.status == 200

    # Publish theme
    page.get_by_role("link", name="Themes").click()
    page.get_by_role("link", name="Publish from Project").click()
    page.get_by_role("link", name="publish", exact=True).click()

    # Visit GeoGirafe
    page.goto("http://localhost:9308/?map_x=2623556&map_y=1195642&map_zoom=0")
    page.get_by_role("button", name="menu-icon Themen").click()
    page.get_by_role("button", name="Icon for TestProject").click()
    page.get_by_role("button", name="Expand/Collapse button").click()
    page.get_by_title("Hintergrundkarte auswählen").click()
    page.get_by_role("button", name="basemap-icon OpenStreetMap").click()

    canvas = page.locator("canvas")
    expect(canvas).to_be_visible()