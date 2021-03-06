# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-15 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_patient', '0014_radiologue_indisponibilites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, null=True)),
                ('radiologue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_patient.Radiologue')),
            ],
        ),
    ]
