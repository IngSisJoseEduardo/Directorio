# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0009_auto_20161024_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directorio',
            name='eliminado',
        ),
    ]
