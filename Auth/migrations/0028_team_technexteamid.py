# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-09 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0027_auto_20161104_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='technexTeamId',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]