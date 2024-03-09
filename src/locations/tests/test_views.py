from http import HTTPStatus

from django.urls import reverse

from core.fixtures import LocationsFixtures
from locations.models import FederationEntity, Region, Settlement


class LocationTests(LocationsFixtures):
    def test_auth_user_get_federation_enteties(self):
        response = self.client.get(reverse("locations:federation_enteties"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.data), FederationEntity.objects.all().count()
        )

    def test_unauth_user_get_federation_enteties(self):
        response = self.anon_client.get(
            reverse("locations:federation_enteties")
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.data), FederationEntity.objects.all().count()
        )

    def test_auth_user_get_regions(self):
        response = self.client.get(reverse("locations:regions"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), Region.objects.all().count())

    def test_unauth_user_get_regions(self):
        response = self.anon_client.get(reverse("locations:regions"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), Region.objects.all().count())

    def test_auth_user_get_settlements(self):
        response = self.client.get(reverse("locations:settlements"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), Settlement.objects.all().count())

    def test_unauth_user_get_settlements(self):
        response = self.anon_client.get(reverse("locations:settlements"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), Settlement.objects.all().count())

    def test_federation_enteties_search(self):
        title_search = self.federation_entity_1.title[1:]
        index_search = self.federation_entity_1.index
        response = self.client.get(
            reverse("locations:federation_enteties")
            + f"?search={title_search}"
        )
        self.assertEqual(
            len(response.data),
            FederationEntity.objects.filter(
                title__contains=title_search
            ).count(),
        )

        response_2 = self.client.get(
            reverse("locations:federation_enteties")
            + f"?search={index_search}"
        )
        self.assertEqual(
            len(response_2.data),
            FederationEntity.objects.filter(
                index__contains=index_search
            ).count(),
        )

    def test_region_search(self):
        title_search = self.region_1_1.title[1:]
        response = self.client.get(
            reverse("locations:regions") + f"?search={title_search}"
        )
        self.assertEqual(
            len(response.data),
            Region.objects.filter(title__contains=title_search).count(),
        )

    def test_settlements_search(self):
        title_search = self.settlement_1.title[1:]
        response = self.client.get(
            reverse("locations:settlements") + f"?search={title_search}"
        )
        self.assertEqual(
            len(response.data),
            Settlement.objects.filter(title__contains=title_search).count(),
        )

    def test_region_filter(self):
        fed_ent_title = self.federation_entity_1.title
        fed_ent_index = self.federation_entity_1.index
        fed_ent_id = self.federation_entity_1.id
        response = self.client.get(
            reverse("locations:regions")
            + f"?federation_entity_title={fed_ent_title}"
        )
        self.assertEqual(
            len(response.data),
            Region.objects.filter(
                federation_entity__title__exact=fed_ent_title
            ).count(),
        )
        response_1 = self.client.get(
            reverse("locations:regions")
            + f"?federation_entity_index={fed_ent_index}"
        )
        self.assertEqual(
            len(response_1.data),
            Region.objects.filter(
                federation_entity__index__exact=fed_ent_index
            ).count(),
        )
        response_2 = self.client.get(
            reverse("locations:regions") + f"?federation_entity={fed_ent_id}"
        )
        self.assertEqual(
            len(response_2.data),
            Region.objects.filter(
                federation_entity__id__exact=fed_ent_id
            ).count(),
        )

    def test_settlements_filter(self):
        region_title = self.region_1_1.title
        region_id = self.region_2_1.id
        response = self.client.get(
            reverse("locations:settlements") + f"?region_title={region_title}"
        )
        self.assertEqual(
            len(response.data),
            Settlement.objects.filter(
                region__title__exact=region_title
            ).count(),
        )
        response_1 = self.client.get(
            reverse("locations:settlements") + f"?region={region_id}"
        )
        self.assertEqual(
            len(response_1.data),
            Settlement.objects.filter(region__id__exact=region_id).count(),
        )
