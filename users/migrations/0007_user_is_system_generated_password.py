# Generated by Django 3.1.1 on 2020-09-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200824_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_system_generated_password',
            field=models.BooleanField(default=False),
        ),
    ]
