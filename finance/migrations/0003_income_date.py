# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-11 06:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20180110_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 1, 11, 6, 22, 35, 296343, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
