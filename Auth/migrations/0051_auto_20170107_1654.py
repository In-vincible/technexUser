# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-07 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0050_auto_20170107_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]
