# Generated by Django 3.2.10 on 2022-04-12 11:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://www.pinclipart.com/picdir/middle/181-1814767_person-svg-png-icon-free-download-profile-icon.png', max_length=255, verbose_name='images/'),
        ),
    ]