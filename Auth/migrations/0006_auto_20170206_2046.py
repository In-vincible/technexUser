# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-06 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_techprofile_notificationtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsors',
            name='order',
            field=models.SmallIntegerField(default=999),
        ),
        migrations.AddField(
            model_name='sponsorshiptype',
            name='order',
            field=models.SmallIntegerField(default=99),
        ),
    ]
