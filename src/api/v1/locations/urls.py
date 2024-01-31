from django.urls import path

from api.v1.locations.views import (
    FederationEntityView,
    MunicipalityView,
    RegionView,
    SettlementView,
)

app_name = "locations"

urlpatterns = [
    path(
        "federation_enteties/",
        FederationEntityView.as_view(),
        name="federation_enteties",
    ),
    path("regions/", RegionView.as_view(), name="regions"),
    path("municipalities/", MunicipalityView.as_view(), name="municipalities"),
    path("settlements/", SettlementView.as_view(), name="settlements"),
]
