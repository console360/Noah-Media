# Generated by Django 3.1.1 on 2020-09-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20200824_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='videos/thumbnails'),
        ),
    ]