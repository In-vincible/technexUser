# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-12 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0069_auto_20170112_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentstatus',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.TechProfile'),
        ),
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]
