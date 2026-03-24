import pytest

from georama.data_integration.models import Mandant

pytestmark = pytest.mark.django_db


class TestDataIntegrationModels:

    def test_mandant_creation(self):
        mandant = Mandant.objects.create(
            name="forestry",
            description="Forestry Department",
        )
        mandant.save()
        assert mandant.name == "forestry"
        assert mandant.description == "Forestry Department"

        mandants = Mandant.objects.all()
        assert mandants.count() == 1
