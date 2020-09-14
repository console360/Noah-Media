from django.db import models

# Create your models here.
from noah.models import CommonInfo
from videos.models import Video


class Tutorial(CommonInfo):
    class Meta:
        db_table = 'noah_tutorials'

    title = models.CharField(max_length=512)
    video = models.ForeignKey(Video, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title





