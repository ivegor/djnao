# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 08:21
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='news',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='news'),
        ),
    ]
