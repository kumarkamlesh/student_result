# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0002_auto_20180412_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_branch',
            name='course',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE,
                                    to='result.student_course'),
        ),
    ]
