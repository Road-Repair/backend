from rest_framework.test import APIClient, APITestCase

from locations.tests.factories import (
    FederationEntityFactory,
    MunicipalityFactory,
    RegionFactory,
    SettlementFactory,
)
from users.tests.factories import CustomUserFactory


class TestUserFixtures(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.phone = "+71000000001"
        cls.password = "super_password"
        cls.new_password = "new_super_password"
        cls.user = CustomUserFactory()
        cls.user_2 = CustomUserFactory()
        cls.user_3 = CustomUserFactory()
        cls.user_4 = CustomUserFactory(phone=cls.phone, password=cls.password)

        cls.client_1 = APIClient()
        cls.client_1.force_authenticate(cls.user)
        cls.client_2 = APIClient()
        cls.client_2.force_authenticate(cls.user_2)
        cls.client_3 = APIClient()
        cls.client_3.force_authenticate(cls.user_3)
        cls.client_4 = APIClient()
        cls.client_4.force_authenticate(cls.user_4)
        cls.anon_client = APIClient()


class LocationsFixtures(TestUserFixtures):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.federation_entity_1 = FederationEntityFactory()
        cls.federation_entity_2 = FederationEntityFactory()
        cls.region_1_1 = RegionFactory(
            federation_entity=cls.federation_entity_1
        )
        cls.region_1_1 = RegionFactory(
            federation_entity=cls.federation_entity_1
        )
        cls.region_2_1 = RegionFactory(
            federation_entity=cls.federation_entity_2
        )
        cls.region_2_2 = RegionFactory(
            federation_entity=cls.federation_entity_2
        )
        cls.municipality_1 = MunicipalityFactory(region=cls.region_1_1)
        cls.municipality_2 = MunicipalityFactory(region=cls.region_2_1)
        cls.settlement_1 = SettlementFactory(municipality=cls.municipality_1)
        cls.settlement_2 = SettlementFactory(municipality=cls.municipality_2)
