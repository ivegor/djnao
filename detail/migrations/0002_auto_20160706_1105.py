# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='base_ptr',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
