# Generated by Django 3.1 on 2020-08-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20200824_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]