# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 19:00
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0003_auto_20160704_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='slider'),
        ),
    ]
