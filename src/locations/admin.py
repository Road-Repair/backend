from django.contrib import admin

from locations.models import FederationEntity, Region, Settlement


@admin.register(FederationEntity)
class AdminFederationEntity(admin.ModelAdmin):
    list_display = ("index", "title", "has_subregions", "projects_create")
    search_fields = ("index", "title")


@admin.register(Region)
class AdminRegion(admin.ModelAdmin):
    list_display = ("title", "has_subregions", "projects_create")
    search_fields = (
        "title",
        "federation_entity__title",
        "federation_entity__index",
    )


@admin.register(Settlement)
class AdminSettlement(admin.ModelAdmin):
    list_display = ("title", "has_subregions", "projects_create")
    search_fields = (
        "title",
        "region__title",
        "region__federation_entity__index",
        "region__federation_entity__title",
    )
