# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-06 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nat_id',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]
