# Generated by Django 3.1.4 on 2021-01-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_listing_realtors'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='listing_photo'),
        ),
    ]
