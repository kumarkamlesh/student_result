# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-29 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0022_auto_20180430_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mca_4th',
            name='rollno',
        ),
        migrations.RemoveField(
            model_name='mca_4th',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='mca_5th',
            name='rollno',
        ),
        migrations.RemoveField(
            model_name='mca_5th',
            name='student_name',
        ),
    ]