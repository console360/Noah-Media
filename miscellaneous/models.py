from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from noah.models import CommonInfo
from django.utils.text import slugify


class Miscellaneous(CommonInfo):
    """
    for miscellaneous features like terms and conditions, privacy policy etc
    """
    class Meta:
        db_table = 'miscellaneous'

    title = models.CharField(max_length=255)
    content = RichTextField(blank=False, null=False)
    slug = models.SlugField(unique=True, default='', editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
