# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 11:08
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='detail'),
        ),
    ]
