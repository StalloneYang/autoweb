# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetask', '0012_auto_20180112_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantastconfig',
            name='plan_info',
            field=models.ManyToManyField(to='timetask.TotalProjects', verbose_name='\u81ea\u52a8\u5316\u9879\u76ee'),
        ),
    ]