# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0032_final_result_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='final_result',
            name='date_time',
        ),
    ]
