# Generated by Django 3.1.1 on 2020-09-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscellaneous', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscellaneous',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
