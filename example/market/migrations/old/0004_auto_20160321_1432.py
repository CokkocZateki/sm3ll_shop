# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20160321_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmarketgroup',
            name='parentGroupID',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.ItemMarketGroup', verbose_name='Parent market group'),
        ),
    ]
