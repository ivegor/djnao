# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0002_auto_20160704_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider'),
        ),
    ]
