# Generated by Django 3.1.4 on 2020-12-27 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtors',
            old_name='hired_date',
            new_name='hire_date',
        ),
    ]
