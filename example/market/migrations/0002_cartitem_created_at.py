# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 17:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_squashed_0010_auto_20160329_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True,),
            preserve_default=False,
        ),
    ]
