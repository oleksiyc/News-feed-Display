# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingscalculator', '0004_auto_20170124_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='interest_rate',
            field=models.IntegerField(default=3.5, verbose_name='Interest rate (annual)'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='number_of_years',
            field=models.IntegerField(default=5, verbose_name='Number of Years'),
        ),
    ]
