# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 11:08
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detail', '0002_auto_20160706_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=128)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='detail')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
