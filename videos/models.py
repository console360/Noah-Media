import uuid
import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from noah.models import MediaFile


# Create your models here.
class Video(MediaFile):

    class Meta:
        db_table = "noah_videos"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    duration = models.PositiveBigIntegerField(_('Video duration in ms'), default=0)
    thumbnail = models.FileField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.file_name = self.file.name
        self.file_size = self.file.size
        _, self.file_extension = os.path.splitext(self.file.name)
        # self.file_mime_type = self.file.content_type
        # self.file_creation_date
        # self.file_modification_date
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.file.name



