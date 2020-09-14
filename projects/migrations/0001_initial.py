# Generated by Django 3.1.1 on 2020-09-06 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Draft'), (1, 'Completed')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'noah_projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectPart',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='PART', max_length=512)),
                ('description', models.CharField(max_length=512)),
                ('part_no', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_parts', to='projects.project')),
            ],
            options={
                'db_table': 'noah_project_parts',
                'ordering': ['part_no'],
            },
        ),
        migrations.CreateModel(
            name='ProjectPartBlock',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='BLOCK', max_length=512)),
                ('description', models.CharField(blank=True, max_length=5120)),
                ('block_letter', models.CharField(default='A', max_length=1)),
                ('project_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_part_blocks', to='projects.projectpart')),
            ],
            options={
                'db_table': 'noah_project_part_blocks',
                'ordering': ['block_letter'],
            },
        ),
    ]
