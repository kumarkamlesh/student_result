# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 18:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0013_auto_20180428_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mca_3rd_s',
            old_name='seminar',
            new_name='seminar3',
        ),
    ]
