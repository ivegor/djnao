# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialty', '0002_auto_20160912_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciality',
            name='text',
        ),
        migrations.AddField(
            model_name='speciality',
            name='activities',
            field=models.TextField(default='', verbose_name='виды деятельности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speciality',
            name='area',
            field=models.CharField(default='', max_length=255, verbose_name='область профессиональной деятельности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speciality',
            name='qualification',
            field=models.TextField(default='', max_length=255, verbose_name='квалификации'),
            preserve_default=False,
        ),
    ]
