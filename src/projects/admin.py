from django.contrib import admin

from projects.models import Project, ProjectImage, ProjectStatus


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "number",
        "actual_status",
        "work_type",
    ]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectStatus)
class StatusOfProjectAdmin(admin.ModelAdmin):
    pass
