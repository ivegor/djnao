# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-13 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0008_auto_20160913_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='documents',
            field=models.ManyToManyField(blank=True, to='documents.Document'),
        ),
    ]
