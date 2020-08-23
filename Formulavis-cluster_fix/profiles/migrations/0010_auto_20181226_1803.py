# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-26 18:03
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20180620_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonfile',
            name='selected_vars',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='jsonfile',
            name='json_format',
            field=models.CharField(choices=[('sat_vis_factor', 'sat_vis_factor'), ('sat_vis_interaction', 'sat_vis_interaction'), ('sat_vis_resolution', 'sat_vis_resolution'), ('raw', 'raw'), ('variables', 'variables'), ('maxsat_vis_factor', 'maxsat_vis_factor'), ('maxsat_vis_interaction', 'maxsat_vis_interaction'), ('maxsat_vis_resolution', 'maxsat_vis_resolution')], max_length=255),
        ),
    ]