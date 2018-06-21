# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-12 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration_form1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('dob', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('rollno', models.CharField(max_length=25)),
                ('branch', models.CharField(max_length=25)),
                ('bday', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
            ],
        ),
    ]
