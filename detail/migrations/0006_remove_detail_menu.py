# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0005_detail_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='menu',
        ),
    ]