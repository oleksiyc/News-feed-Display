# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingscalculator', '0009_auto_20170202_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='final_capital',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
