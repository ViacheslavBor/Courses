# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='first_app.University'),
        ),
    ]
