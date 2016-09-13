# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('qualification', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('activities', models.TextField()),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]