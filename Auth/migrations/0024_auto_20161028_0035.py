# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-28 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0023_techprofile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='techprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='techprofile',
            name='referral',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='techprofile',
            name='technexId',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
