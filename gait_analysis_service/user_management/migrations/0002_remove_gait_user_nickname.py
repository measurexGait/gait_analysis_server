# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gait_user',
            name='nickname',
        ),
    ]
