from django.contrib import admin

from projects.models import Project, ProjectImage, ProjectStatus


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "number",
        "actual_status",
        "work_type",
    ]
    search_fields = ["number"]
    list_filter = ["actual_status", "work_type"]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    search_fields = ["project__number"]
    list_filter = ["type"]


@admin.register(ProjectStatus)
class StatusOfProjectAdmin(admin.ModelAdmin):
    search_fields = ["project__number"]
