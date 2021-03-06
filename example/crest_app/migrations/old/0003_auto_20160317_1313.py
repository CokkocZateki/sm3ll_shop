# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crest_app', '0002_auto_20160317_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='eveuser',
            name='_alliance_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eveuser',
            name='_alliance_name',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='eveuser',
            name='_character_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eveuser',
            name='_character_name',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='eveuser',
            name='_corporation_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eveuser',
            name='_corporation_name',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
