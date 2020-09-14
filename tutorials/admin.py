from django.contrib import admin
from tutorials.models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    fields = ('title', 'video', 'is_deleted')


admin.site.register(Tutorial, TutorialAdmin)
