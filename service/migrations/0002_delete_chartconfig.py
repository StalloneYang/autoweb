# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-27 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChartConfig',
        ),
    ]
