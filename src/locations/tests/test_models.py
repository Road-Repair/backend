from django.test import TestCase

from locations.tests.factories import (
    FederationEntityFactory,
    MunicipalityFactory,
    RegionFactory,
    SettlementFactory,
)


class LocationsModelsTest(TestCase):
    """
    Класс для тестирования моделей приложения locations.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.federal_entity = FederationEntityFactory()
        cls.region = RegionFactory()
        cls.muncipality = MunicipalityFactory()
        cls.settlement = SettlementFactory()

    def test_models_have_correct_object_names(self):
        str_patterns = {
            self.federal_entity.title: str(self.federal_entity),
            self.region.title: str(self.region),
            self.muncipality.title: str(self.muncipality),
            self.settlement.title: str(self.settlement),
        }

        for str_name, obj in str_patterns.items():
            with self.subTest(str_name=str_name):
                self.assertEqual(obj, str_name)

    def test_models_default_values(self):
        self.assertFalse(self.federal_entity.projects_create)
        self.assertFalse(self.region.projects_create)
        self.assertFalse(self.muncipality.projects_create)
        self.assertTrue(self.settlement.projects_create)
        self.assertFalse(self.federal_entity.has_subregions)
        self.assertFalse(self.region.has_subregions)
        self.assertFalse(self.muncipality.has_subregions)
        self.assertFalse(self.settlement.has_subregions)
