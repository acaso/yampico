# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import lists.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.CharField(default=lists.models.generate_uuid, max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.CharField(default=lists.models.generate_uuid, max_length=128, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('marked', models.BooleanField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
            ],
        ),
    ]
