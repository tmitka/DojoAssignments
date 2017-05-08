# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('cost', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]