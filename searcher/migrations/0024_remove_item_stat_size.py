# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-12 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0023_item_stat_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stat_size',
        ),
    ]
