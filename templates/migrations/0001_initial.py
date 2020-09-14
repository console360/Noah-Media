# Generated by Django 3.1 on 2020-08-28 17:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'noah_templates',
            },
        ),
        migrations.CreateModel(
            name='TemplatePart',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='PART', max_length=512)),
                ('description', models.CharField(max_length=512)),
                ('part_no', models.PositiveIntegerField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.template')),
            ],
            options={
                'db_table': 'noah_template_parts',
                'ordering': ['part_no'],
            },
        ),
    ]