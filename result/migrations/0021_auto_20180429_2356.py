# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-29 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0020_auto_20180429_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mca_2nd',
            name='rollno',
        ),
        migrations.RemoveField(
            model_name='mca_2nd',
            name='student_name',
        ),
    ]
