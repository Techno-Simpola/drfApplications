# Generated by Django 4.0.2 on 2022-02-13 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='title',
        ),
    ]
