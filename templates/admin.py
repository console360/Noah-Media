from django.contrib import admin
from templates.models import Template, TemplatePart


class TemplatePartInline(admin.TabularInline):
    model = TemplatePart
    fields = ('title', 'description', 'part_no')
    extra = 1


# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    inlines = [TemplatePartInline, ]
    fields = ('title', 'description', 'is_deleted')


admin.site.register(Template, TemplateAdmin)
