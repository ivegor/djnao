# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160707_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
