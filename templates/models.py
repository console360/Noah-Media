import uuid
from django.db import models

# Create your models here.
from noah.models import CommonInfo


class Template(CommonInfo):
    class Meta:
        db_table = 'noah_templates'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class TemplatePart(CommonInfo):
    class Meta:
        db_table = 'noah_template_parts'
        ordering = ['part_no']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512, default="PART")
    description = models.CharField(max_length=512)
    part_no = models.PositiveIntegerField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='parts')

    def __str__(self):
        return self.title
