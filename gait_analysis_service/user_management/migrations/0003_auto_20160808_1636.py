# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-08 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_remove_gait_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gait_user',
            name='sex',
            field=models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=2, null=True, verbose_name='性别'),
        ),
    ]
