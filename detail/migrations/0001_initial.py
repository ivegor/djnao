# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 10:46
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_remove_base_fav_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Base')),
                ('name', models.CharField(max_length=128)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'abstract': False,
            },
            bases=('base.base',),
        ),
    ]