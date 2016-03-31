# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvType',
            fields=[
                ('typeID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('typeName', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('mass', models.FloatField()),
                ('volume', models.FloatField()),
                ('capacity', models.FloatField()),
                ('portionSize', models.FloatField()),
                ('raceID', models.IntegerField()),
                ('basePrice', models.FloatField()),
                ('published', models.SmallIntegerField(verbose_name='Whether or not this item has been published')),
                ('iconID', models.FloatField()),
                ('soundID', models.IntegerField()),
                ('graphicID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('groupID', models.IntegerField(primary_key=True, serialize=False)),
                ('categoryID', models.IntegerField()),
                ('groupName', models.CharField(max_length=128)),
                ('iconID', models.IntegerField()),
                ('useBasePrice', models.SmallIntegerField()),
                ('anchored', models.SmallIntegerField()),
                ('anchorable', models.SmallIntegerField()),
                ('fittableNonSingleton', models.SmallIntegerField()),
                ('published', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemMarketGroup',
            fields=[
                ('marketGroupID', models.IntegerField(primary_key=True, serialize=False)),
                ('parentGroupID', models.IntegerField()),
                ('marketGroupName', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('iconID', models.IntegerField()),
                ('hasTypes', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='invtype',
            name='itemgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.ItemGroup', verbose_name='The related Item Group (groupID)'),
        ),
        migrations.AddField(
            model_name='invtype',
            name='itemmarketgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.ItemMarketGroup', verbose_name='The related market Group (marketGroupID)'),
        ),
    ]
