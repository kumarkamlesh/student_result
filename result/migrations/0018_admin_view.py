# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-29 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0017_registration_form1_conf_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
