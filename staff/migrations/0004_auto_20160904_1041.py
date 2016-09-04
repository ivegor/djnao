# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20160903_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ('category', 'order')},
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='teacher_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.BooleanField(choices=[(True, 'мужской'), (False, 'женский')], default=True),
        ),
    ]
