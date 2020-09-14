from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonInfo(models.Model):
    is_deleted = models.BooleanField(default=False)  # Flag to manage user active in the system
    created_at = models.DateTimeField(auto_now_add=True)  # Track when user has been created
    modified_at = models.DateTimeField(auto_now=True)  # Track when user information get updated

    class Meta:
        abstract = True


class MediaFile(CommonInfo):

    class Meta:
        abstract = True

    file_name = models.CharField(_('file name'), max_length=512, default='')
    file_size = models.PositiveBigIntegerField(_('file size in bytes'), default=0)
    file_extension = models.CharField(_('file extension'), max_length=256)
    file_mime_type = models.CharField(_('file mime type'), max_length=256)
    file_creation_date = models.DateTimeField(blank=True, null=True)
    file_modification_date = models.DateTimeField(blank=True, null=True)
    file = models.FileField()
