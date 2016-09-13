# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-13 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialty', '0004_auto_20160912_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='есть в этом году')),
                ('form_learning', models.CharField(choices=[('ft', 'очная'), ('pt', 'заочная'), ('ev', 'вечерняя')], max_length=2, verbose_name='форма обучения')),
                ('budgets', models.PositiveSmallIntegerField(verbose_name='количество бюджетных мест')),
                ('requests', models.PositiveSmallIntegerField(verbose_name='поданных заявлений')),
            ],
        ),
        migrations.AddField(
            model_name='speciality',
            name='profile',
            field=models.CharField(choices=[('te', 'технический'), ('na', 'естественно-научный')], default='te', max_length=2, verbose_name='профиль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additional',
            name='speciality',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='specialty.Speciality'),
        ),
    ]