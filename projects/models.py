import uuid
from django.db import models

# Create your models here.
from noah.models import CommonInfo
from users.models import User
from videos.models import Video


class ProjectManager(models.Manager):

    def init_project(self, template, user):
        project = self.create(title=template.title, description=template.description, user=user)
        return project

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Project(CommonInfo):
    class Meta:
        db_table = 'noah_projects'

    PROJECT_STATUS_DRAFT = 0
    PROJECT_STATUS_COMPLETED = 1
    STATUS_CHOICES = ((PROJECT_STATUS_DRAFT, 'Draft'), (PROJECT_STATUS_COMPLETED, 'Completed'))

    objects = ProjectManager()

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    status = models.PositiveIntegerField(default=PROJECT_STATUS_DRAFT, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_projects')

    # video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='user_videos', null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectPartManager(models.Manager):

    def init_project_part(self, template_part, project):
        project_part = self.create(title=template_part.title, description=template_part.description,
                                   part_no=template_part.part_no, project=project)
        return project_part

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class ProjectPart(CommonInfo):
    class Meta:
        db_table = 'noah_project_parts'
        ordering = ['part_no']

    objects = ProjectPartManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512, default="PART")
    description = models.CharField(max_length=512)
    part_no = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_parts')

    def __str__(self):
        return f"{self.title} {self.part_no}"


class ProjectPartBlockManager(models.Manager):

    def init_project_part_block(self, project_part):
        project_part_block = self.create(project_part=project_part)
        return project_part_block

    def create_project_part_block(self, project_part, block_letter):
        project_part_block = self.create(project_part=project_part, block_letter=block_letter)
        return project_part_block

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class ProjectPartBlock(CommonInfo):
    class Meta:
        db_table = 'noah_project_part_blocks'
        ordering = ['block_letter']

    objects = ProjectPartBlockManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512, default="BLOCK")
    description = models.CharField(max_length=5120, blank=True)
    block_letter = models.CharField(default='A', max_length=1)
    project_part = models.ForeignKey(ProjectPart, on_delete=models.CASCADE, related_name='project_part_blocks')

    def __str__(self):
        return f"{self.title} {self.block_letter}"
