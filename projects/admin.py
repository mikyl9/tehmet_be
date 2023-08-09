from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "preview",
        "title",
        "created_at",
    )

    def preview(self, obj):
        if obj.logo:
            return mark_safe('<img src="{}" height="80">'.format(obj.logo.url))
        else:
            return "[no image]"


admin.site.register(Project, ProjectAdmin)
