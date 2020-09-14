from django.contrib import admin
from videos.models import Video


class VideoAdmin(admin.ModelAdmin):
    fields = ('file', 'thumbnail', 'is_deleted')


admin.site.register(Video, VideoAdmin)
