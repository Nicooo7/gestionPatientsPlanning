# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-11 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_patient', '0013_auto_20180810_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiologue',
            name='indisponibilites',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]