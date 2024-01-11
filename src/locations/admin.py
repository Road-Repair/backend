from django.contrib import admin

from locations.models import FederationEntity, Municipality, Region, Settlement


@admin.register(FederationEntity)
class AdminFederationEntity(admin.ModelAdmin):
    list_display = ("index", "title")
    search_fields = ("index", "title")


@admin.register(Municipality)
class AdminMunicipality(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = (
        "title",
        "region__title",
        "region__federation_entity__index",
        "region__federation_entity__title",
    )


@admin.register(Region)
class AdminRegion(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = (
        "title",
        "federation_entity__title",
        "federation_entity__index",
    )


@admin.register(Settlement)
class AdminSettlement(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = (
        "title",
        "мunicipality__title",
        "мunicipality__region__title",
        "мunicipality__region__federation_entity__index",
        "мunicipality__region__federation_entity__title",
    )
