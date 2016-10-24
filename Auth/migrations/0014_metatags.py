# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-24 21:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0013_auto_20161001_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.ParentEvent')),
            ],
        ),
    ]
