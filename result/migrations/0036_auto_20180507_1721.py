# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0035_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='save',
            new_name='messaged',
        ),
    ]
