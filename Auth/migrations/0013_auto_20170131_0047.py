# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-30 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0012_auto_20170131_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizteam',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.quiz'),
        ),
    ]
