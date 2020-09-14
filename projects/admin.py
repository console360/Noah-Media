from django.contrib import admin

# Register your models here.
from projects.models import Project, ProjectPart, ProjectPartBlock


class ProjectPartBlockInline(admin.TabularInline):
    model = ProjectPartBlock
    extra = 0


class ProjectPartInline(admin.StackedInline):
    model = ProjectPart
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectPartInline, ]
    pass


# admin.site.register(Project, ProjectAdmin)
