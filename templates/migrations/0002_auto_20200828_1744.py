# Generated by Django 3.1 on 2020-08-28 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatepart',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template_parts', to='templates.template'),
        ),
    ]