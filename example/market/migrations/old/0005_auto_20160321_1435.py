# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20160321_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmarketgroup',
            name='parentGroupID',
            field=models.IntegerField(verbose_name='Parent market group id'),
        ),
    ]
