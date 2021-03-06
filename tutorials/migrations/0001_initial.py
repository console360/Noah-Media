# Generated by Django 3.1 on 2020-08-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0002_auto_20200822_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=512)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='videos.video')),
            ],
            options={
                'db_table': 'noah_tutorials',
            },
        ),
    ]
