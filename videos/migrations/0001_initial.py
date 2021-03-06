# Generated by Django 3.1 on 2020-08-22 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(default='', max_length=512, verbose_name='file_name')),
                ('file_size', models.PositiveBigIntegerField(default=0, verbose_name='file_size in kB')),
                ('file_extension', models.CharField(max_length=256, verbose_name='file_extension')),
                ('file_mime_type', models.CharField(max_length=256, verbose_name='file_mime_type')),
                ('file_creation_date', models.DateTimeField(blank=True, null=True)),
                ('file_modification_date', models.DateTimeField(blank=True, null=True)),
                ('file', models.FileField(upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('duration', models.PositiveBigIntegerField(default=0, verbose_name='video_duration in ms')),
            ],
            options={
                'db_table': 'noah_videos',
            },
        ),
    ]
