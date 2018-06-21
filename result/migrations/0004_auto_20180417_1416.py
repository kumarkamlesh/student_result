# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0003_student_branch_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_sem',
            name='course',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE,
                                    to='result.student_course'),
        ),
        migrations.AlterField(
            model_name='student_branch',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE,
                                    to='result.student_course'),
        ),
    ]
