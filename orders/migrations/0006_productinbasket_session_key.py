# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productinbasket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=12, null=True),
        ),
    ]