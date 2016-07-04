# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h3', models.CharField(max_length=255)),
                ('p', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(height_field=500, upload_to='slider')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]