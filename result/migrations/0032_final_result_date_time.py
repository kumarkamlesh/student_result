# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0031_remove_final_result_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='final_result',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]