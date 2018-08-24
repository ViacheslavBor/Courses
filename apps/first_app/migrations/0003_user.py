# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('courses', models.ManyToManyField(related_name='users', to='first_app.Course')),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='first_app.University')),
            ],
        ),
    ]
